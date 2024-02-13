import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("350x200")
        self.master.configure(bg="#f0f0f0")

        self.label_length = tk.Label(self.master, text="Password Length:", bg="#f0f0f0", fg="#333333", font=("Arial", 12))
        self.label_length.pack(pady=(20, 5))

        self.entry_length = tk.Entry(self.master, font=("Arial", 12))
        self.entry_length.pack()

        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password, bg="#007bff", fg="#ffffff", font=("Arial", 12), padx=10, pady=5)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.master, text="", bg="#f0f0f0", fg="#333333", font=("Arial", 12, "bold"))
        self.password_label.pack()

    def generate_password(self):
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                messagebox.showerror("Error", "Length must be a positive integer.")
                return
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text="Generated Password: " + password)
        except ValueError:
            messagebox.showerror("Error", "Length must be a positive integer.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
