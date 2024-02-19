"""this module contains code for calculator controller"""


from calculator_view import CalculatorView
from calculator_model import CalculatorModel


class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)  # Pass master and controller to view

    def update_display(self, value):
        current_input = self.view.input_var.get()
        if value == '=':
            try:
                result = eval(current_input)
                self.view.set_display_text(str(result))
                self.model.history_value.append(current_input + '=' + str(result))
            except:
                self.view.input_var.set("Error: Invalid input")
        elif value == 'del':
            if value.endswith("sqrt("):
                de = current_input.strip("sqrt(")
                self.view.input_var.set(de)
            elif value.endswith("log10("):
                de = current_input.strip("log10(")
                self.view.input_var.set(de)
            else:
                self.view.input_var.set(current_input[:-1])
        elif value == 'clr':
            self.view.input_var.set("")
        elif value == '(':
            self.view.input_var.set(current_input + '(')
        elif value == ')':
            self.view.set_display_text(current_input + ')')
        elif value == 'log':
            self.view.set_display_text(current_input + 'log10(')
        elif value == 'sqrt':
            self.view.set_display_text(current_input + 'sqrt(')
        elif value == '^':  # Add this condition for x^y
            self.view.set_display_text(current_input + '**')
        elif value == '%':  # Add this condition for modulo
            self.view.set_display_text(current_input + '%')
        elif value == 'history':
            self.model.history()
        else:
            self.view.set_display_text(current_input + str(value))

    def run(self):
        self.view.mainloop()
