import tkinter as tk
from tkinter import ttk

class CalculatorView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_components()

    def init_components(self):
        # Create main frame
        # create main frame
        self.mainframe = ttk.Frame(self.master)
        self.mainframe.grid(row=0, column=0, padx=2, pady=2, ipadx=8, ipady=8, sticky=tk.NSEW)

        # Display to show input
        self.input_var = tk.StringVar()
        self.display = ttk.Entry(self.mainframe, textvariable=self.input_var, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=10, sticky=tk.NSEW)

        # Keypad and operator buttons
        self.make_keypad()
        self.make_operator_pad()

    def make_keypad(self):
        # Implement keypad creation
        keyname = [7, 8, 9, 4, 5, 6, 1, 2, 3, '.', 0, '=']
        for k in range(12):
            if keyname[k] == 0:
                col = 1
                row = 3
            else:
                col = k % 3
                row = k // 3
            button = ttk.Button(self.mainframe, text=str(keyname[k]),
                                command=lambda val=keyname[k]: self.controller.update_display(val), width=6)
            button.grid(row=row + 1, column=col, padx=2, pady=2, ipady=5, ipadx=5, sticky=tk.NSEW)
            self.grid_rowconfigure(k, weight=1)
            self.grid_columnconfigure(k, weight=1)

    def make_operator_pad(self):
        # Implement operator pad creation
        operators = ['+', '-', '*', '/', '=', 'clr', 'del', '^', '(', ')']
        for i, op in enumerate(operators):
            button = ttk.Button(self.mainframe, text=op, command=lambda val=op: self.controller.update_display(val), width=4)
            if i >= 5:
                # Buttons in columns 5 and 6
                button.grid(row=i - 4, column=5, padx=1, pady=1, ipady=0.1, ipadx=0.1, sticky=tk.NSEW)
                self.grid_rowconfigure(i - 4, weight=1)
                self.grid_columnconfigure(5, weight=1)  # Adjust column index
            elif i < 5:
                # Buttons in column 4
                button.grid(row=i + 1, column=4, padx=1, pady=1, ipady=5, ipadx=5, sticky=tk.NSEW)
                self.grid_rowconfigure(i + 1, weight=1)
                self.grid_columnconfigure(4, weight=1)  # Adjust column index
        oper = ['log', 'sqrt', '%', 'history']
        for a, op2 in enumerate(oper):
            button2 = ttk.Button(self.mainframe, text=op2, command=lambda val=op2: self.controller.update_display(val), width=5)
            button2.grid(row=a + 1, column=6, padx=1, pady=1, ipady=2, ipadx=2, sticky=tk.NSEW)
            self.grid_rowconfigure(a + 1, weight=1)
            self.grid_columnconfigure(6, weight=1)

    def get_display_text(self):
        return self.input_var.get()

    def set_display_text(self, text):
        self.input_var.set(text)

    def append_to_display(self, text):
        current_text = self.get_display_text()
        self.set_display_text(current_text + text)

    def clear_display(self):
        self.set_display_text("")

    def show_history(self, history):
        # Implement history display
        pass

    def run(self):
        self.mainloop()