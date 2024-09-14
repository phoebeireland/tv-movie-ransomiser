from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the data
data = {
    "TV Show": {},
    "Movie": {}
}

@app.route('/add', methods=['POST'])
def add_name():
    content = request.json
    type_name = content.get('type')
    genre = content.get('genre')
    name = content.get('name')
    
    if not type_name or not genre or not name:
        return jsonify({"error": "All fields are required."}), 400

    if type_name not in data:
        return jsonify({"error": "Type must be 'TV Show' or 'Movie'."}), 400

    if genre not in data[type_name]:
        data[type_name][genre] = []

    data[type_name][genre].append(name)
    return jsonify({"message": f"Added {name} as a {type_name} of genre {genre}."}), 200

@app.route('/generate', methods=['GET'])
def generate_name():
    type_name = request.args.get('type')
    genre = request.args.get('genre')

    if type_name not in data:
        return jsonify({"error": "Type must be 'TV Show' or 'Movie'."}), 400
    
    if genre not in data[type_name]:
        return jsonify({"error": f"No {type_name} names available for genre {genre}."}), 400

    if not data[type_name][genre]:
        return jsonify({"error": f"No {type_name} names available for genre {genre}."}), 400

    import random
    name = random.choice(data[type_name][genre])
    return jsonify({"name": name}), 200

if __name__ == "__main__":
    app.run(debug=True)
