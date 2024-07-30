import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password(max_length):
    if max_length <= 0:
        return ""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(max_length))
    return password
def on_generate_button_click():
    try:
        max_length = int(length_entry.get())
        if max_length <= 0:
            raise ValueError("Length must be a positive integer")
        password = generate_password(max_length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter a valid number for length.\nError: {e}")
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")
background_color = "#f0f8ff"
button_color = "#4caf50"
button_text_color = "#ffffff"
label_color = "#333333"
entry_bg_color = "#ffffff"
entry_fg_color = "#000000"
result_bg_color = "#e6f9ff"
app.configure(bg=background_color)
length_label = tk.Label(app, text="Enter Maximum Password Length:", font=("Helvetica", 16, "bold"), bg=background_color,
                        fg=label_color)
length_label.pack(pady=10)
length_entry = tk.Entry(app, font=("Helvetica", 16), bg=entry_bg_color, fg=entry_fg_color, bd=2, relief="groove")
length_entry.pack(pady=10)
generate_button = tk.Button(app, text="Generate Password", font=("Helvetica", 16), bg=button_color,
                            fg=button_text_color, width=20, height=2, relief="raised", command=on_generate_button_click)
generate_button.pack(pady=15)
result_label = tk.Label(app, text="", font=("Helvetica", 16), bg=result_bg_color, fg=label_color, bd=2, relief="solid",
                        padx=10, pady=10)
result_label.pack(pady=15)
app.mainloop()