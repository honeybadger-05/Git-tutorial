import math
from datetime import datetime

class Calculator:
    def __init__(self, user):
        self.user = user
        self.history = []

    def log_operation(self, operation, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {operation} = {result}"
        self.history.append(entry)
        print(f"[LOG] {entry}")

    def add(self, a, b):
        result = a + b
        self.log_operation(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.log_operation(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.log_operation(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        self.log_operation(f"{a} / {b}", result)
        return result

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of negative number")
        result = math.sqrt(x)
        self.log_operation(f"√{x}", result)
        return result

    def show_history(self):
        print("\n=== Calculation History ===")
        for entry in self.history:
            print(entry)

if __name__ == "__main__":
    calc = Calculator("Manoj")
    calc.add(10, 20)
    calc.subtract(50, 30)
    calc.multiply(6, 7)
    calc.divide(100, 5)
    calc.square_root(81)
    calc.show_history()