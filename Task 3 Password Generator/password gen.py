import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase  
 
    if use_uppercase:
        characters += string.ascii_uppercase
    
    if use_numbers:
        characters += string.digits
    
    if use_special_chars:
        characters += string.punctuation
   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def submit():
    try:
        length = int(length_entry.get()) 
        if length < 8:
            messagebox.showerror("Error", "Password length should be at least 8 characters")
            return
        
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_special_chars = special_chars_var.get()
        
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        
        password_label.config(text="Generated Password: " + password)
    
    except ValueError:
        messagebox.showerror("Error", "Password length should be a number")


root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Use Uppercase Letters", variable=uppercase_var)
uppercase_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Use Numbers", variable=numbers_var)
numbers_checkbox.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Use Special Characters", variable=special_chars_var)
special_chars_checkbox.pack()

submit_button = tk.Button(root, text="Generate Password", command=submit)
submit_button.pack()

password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

root.mainloop()
