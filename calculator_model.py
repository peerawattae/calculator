"""this module contain code for calculator_model"""
import tkinter as tk
from tkinter import ttk
class CalculatorModel:
    def __init__(self):
        self.history_value = []

    def evaluate_expression(self, expression):
        try:
            result = eval(expression)
            self.history_value.append(expression + ' = ' + str(result))
            return str(result)
        except Exception as e:
            return "Error: " + str(e)

    def history(self):
        self.root = tk.Tk()
        self.root.title("History")

        # create frame for history
        self.historyframe = ttk.Frame(self.root)
        self.historyframe.grid(row=5, column=5, ipadx=20, ipady=40, sticky=tk.NSEW)
        self.history_text = tk.Text(self.historyframe, height=10, width=30)
        self.history_text.grid(row=1, column=1, columnspan=5, rowspan=10, sticky=tk.NSEW)
        button = ttk.Button(self.historyframe, text="copy", )
        button.grid(row=5, column=3, padx=1, pady=1, ipady=1, ipadx=2, sticky=tk.NSEW)
        for item in self.history_value:
            self.history_text.insert(tk.END, item + "\n")
        self.pack()
