import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except:
        messagebox.showerror("Error", "Enter valid number")
        return

    characters = string.ascii_letters

    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += "!@#$%^&*"

    password = "".join(random.choice(characters) for _ in range(length))
    result_var.set(password)

    check_strength(password)

def check_strength(password):
    strength = 0

    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*" for c in password):
        strength += 1
    if len(password) >= 10:
        strength += 1

    if strength == 1:
        strength_label.config(text="Weak", fg="red")
    elif strength == 2:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# UI Setup
root = tk.Tk()
root.title("Pro Password Generator")
root.geometry("350x350")
root.config(bg="#121212")

tk.Label(root, text="🔐 Password Generator",
         font=("Segoe UI", 16, "bold"),
         bg="#121212", fg="white").pack(pady=10)

# Length input
tk.Label(root, text="Password Length", bg="#121212", fg="white").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "8")

# Options
numbers_var = tk.IntVar(value=1)
symbols_var = tk.IntVar(value=1)

tk.Checkbutton(root, text="Include Numbers",
               variable=numbers_var,
               bg="#121212", fg="white",
               selectcolor="#121212").pack()

tk.Checkbutton(root, text="Include Symbols",
               variable=symbols_var,
               bg="#121212", fg="white",
               selectcolor="#121212").pack()

# Generate button
tk.Button(root, text="Generate",
          bg="#28a745", fg="white",
          command=generate_password).pack(pady=10)

# Result
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30).pack()

# Strength
strength_label = tk.Label(root, text="", bg="#121212", fg="white")
strength_label.pack(pady=5)

# Copy button
tk.Button(root, text="Copy",
          bg="#007bff", fg="white",
          command=copy_password).pack(pady=10)

root.mainloop()
