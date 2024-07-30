import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Calculator")
        self.geometry("400x600")
        self.configure(bg="lightgray")

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
            tk.Button(self, text=button, font=self.button_font, command=action, bg="white").grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Adding the "=" button across the last row
        tk.Button(self, text='=', font=self.button_font, command=lambda: self.click_event('='), bg="white").grid(row=row_val, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Configuring grid weights for resizing
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(row_val + 1):  # Including row for "=" button
            self.grid_rowconfigure(i, weight=1)

    def click_event(self, key):
        if key == "=":
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
