from decimal import Decimal

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: Decimal, b: Decimal) -> Decimal:
        result = a + b
        self.history.append((a, b, '+', result))
        return result

    def subtract(self, a: Decimal, b: Decimal) -> Decimal:
        result = a - b
        self.history.append((a, b, '-', result))
        return result

    def multiply(self, a: Decimal, b: Decimal) -> Decimal:
        result = a * b
        self.history.append((a, b, '*', result))
        return result

    def divide(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append((a, b, '/', result))
        return result

    def clear_history(self):
        self.history.clear()

    def get_history(self):
        return self.history
