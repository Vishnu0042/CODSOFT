import tkinter as tk
from tkinter import font, Menu
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vishnu Calculator")
        self.geometry("400x600")
        self.configure(bg="lightgray")
        self.history = []
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.button_font = font.Font(family='Arial', size=18)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            btn = tk.Button(self, text=button, font=self.button_font, command=action, bg="white")
            btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        equal_btn = tk.Button(self, text='=', font=self.button_font, command=lambda: self.click_event('='), bg="white")
        equal_btn.grid(row=row_val, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        equal_btn.bind("<Enter>", self.on_enter)
        equal_btn.bind("<Leave>", self.on_leave)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(row_val + 1):
            self.grid_rowconfigure(i, weight=1)
        menubar = Menu(self)
        themes_menu = Menu(menubar, tearoff=0)
        themes_menu.add_command(label="Light Mode", command=self.light_mode)
        themes_menu.add_command(label="Dark Mode", command=self.dark_mode)
        menubar.add_cascade(label="Themes", menu=themes_menu)
        self.config(menu=menubar)
        history_btn = tk.Button(self, text="History", font=self.button_font, command=self.show_history, bg="white")
        history_btn.grid(row=row_val+1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        history_btn.bind("<Enter>", self.on_enter)
        history_btn.bind("<Leave>", self.on_leave)
    def click_event(self, key):
        if key == "=":
            try:
                result = str(eval(self.display.get()))
                self.history.append(self.display.get() + " = " + result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)
    def light_mode(self):
        self.configure(bg="lightgray")
        self.display.configure(bg="white", fg="black")
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="white", fg="black")
    def dark_mode(self):
        self.configure(bg="black")
        self.display.configure(bg="gray", fg="white")
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg="gray", fg="white")
    def on_enter(self, e):
        e.widget['background'] = 'lightblue'
    def on_leave(self, e):
        e.widget['background'] = 'white' if self.cget("bg") == "lightgray" else 'gray'
    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("History")
        history_window.geometry("300x400")
        history_text = tk.Text(history_window, font=("Arial", 14))
        history_text.pack(expand=True, fill='both')
        for entry in self.history:
            history_text.insert(tk.END, entry + "\n")
if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()