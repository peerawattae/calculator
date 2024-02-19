import tkinter as tk
from tkinter import ttk
from calculator_model import CalculatorModel
from calculator_view import CalculatorView
from calculator_controller import CalculatorController

if __name__ == "__main__":
    app = CalculatorController()
    app.run()