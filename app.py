import tkinter as tk
from tkinter import messagebox
import random

class ShowMovieGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("TV Show and Movie Generator")

        # Create and place widgets
        self.label_type = tk.Label(root, text="Type (TV Show/Movie):")
        self.label_type.grid(row=0, column=0, padx=10, pady=10)

        self.entry_type = tk.Entry(root)
        self.entry_type.grid(row=0, column=1, padx=10, pady=10)

        self.label_genre = tk.Label(root, text="Genre (e.g., Comedy, Drama):")
        self.label_genre.grid(row=1, column=0, padx=10, pady=10)

        self.entry_genre = tk.Entry(root)
        self.entry_genre.grid(row=1, column=1, padx=10, pady=10)

        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=2, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=2, column=1, padx=10, pady=10)

        self.button_add = tk.Button(root, text="Add", command=self.add_name)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_generate = tk.Button(root, text="Generate", command=self.generate_name)
        self.button_generate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.text_result = tk.Text(root, height=2, width=30)
        self.text_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Initialize data structures
        self.data = {
            "TV Show": {},
            "Movie": {}
        }

    def add_name(self):
        type_name = self.entry_type.get().strip()
        genre = self.entry_genre.get().strip()
        name = self.entry_name.get().strip()
        
        if not type_name or not genre or not name:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        if type_name not in self.data:
            messagebox.showerror("Input Error", "Type must be 'TV Show' or 'Movie'.")
            return

        if genre not in self.data[type_name]:
            self.data[type_name][genre] = []
        
        self.data[type_name][genre].append(name)
        messagebox.showinfo("Success", f"Added {name} as a {type_name} of genre {genre}.")
        self.entry_type.delete(0, tk.END)
        self.entry_genre.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)

    def generate_name(self):
        type_name = self.entry_type.get().strip()
        genre = self.entry_genre.get().strip()

        if type_name not in self.data:
            messagebox.showerror("Input Error", "Type must be 'TV Show' or 'Movie'.")
            return
        
        if genre not in self.data[type_name]:
            messagebox.showerror("Input Error", f"No {type_name} names available for genre {genre}.")
            return

        if not self.data[type_name][genre]:
            messagebox.showerror("No Data", f"No {type_name} names available for genre {genre}.")
            return

        name = random.choice(self.data[type_name][genre])
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, name)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowMovieGenerator(root)
    root.mainloop()
