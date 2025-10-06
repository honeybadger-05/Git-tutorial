import math
from datetime import datetime

class AdvancedCalculator:
    def __init__(self, user, log_file="calc_history.txt"):
        self.user = user
        self.log_file = log_file

    def log_operation(self, operation, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {operation} = {result}\n"
        with open(self.log_file, "a") as file:
            file.write(entry)
        print(f"[SAVED TO FILE] {entry.strip()}")

    def power(self, base, exponent):
        result = math.pow(base, exponent)
        self.log_operation(f"{base}^{exponent}", result)
        return result

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Modulus by zero is not allowed")
        result = a % b
        self.log_operation(f"{a} % {b}", result)
        return result

    def hypotenuse(self, a, b):
        result = math.hypot(a, b)
        self.log_operation(f"hypotenuse({a}, {b})", result)
        return result

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = math.factorial(n)
        self.log_operation(f"{n}!", result)
        return result


if __name__ == "__main__":
    calc = AdvancedCalculator("Manoj")
    calc.power(2, 5)
    calc.modulus(25, 6)
    calc.hypotenuse(3, 4)
    calc.factorial(5)
