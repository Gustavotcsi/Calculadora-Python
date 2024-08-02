import tkinter as tk
from math import sqrt

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'C',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            b = tk.Button(self, text=button, width=10, height=3, command=action)

            b.grid(row=row_val, column=col_val, padx=5, pady=5)

            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif key == "C":
            self.entry.delete(0, tk.END)
        elif key == "sqrt":
            try:
                result = sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        elif key == "pow":
            try:
                self.entry.insert(tk.END, "**")
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        else:
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
