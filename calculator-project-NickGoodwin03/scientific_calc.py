from simple_calc import Calculator  # importing the Calculator base-class
import math


class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()

    # =============================================================================
    #     ^     for a ^ b
    #     %     for a mod b
    #     r     for the bth root of a (a ^ (1/b))
    #     !     for a factorial
    #     sin   for sin(a) in radians
    #     cos   for cos(a) in radians
    #     tan   for tan(a) in radians
    #     ln    for ln(a) (log base e of a)
    # =============================================================================

    def sci_calculate(self):
        if self.operation in '+-*/':
            super().calculate()

        # Scientific calculator operations
        elif self.operation == "^":
            self.result = self.num1 ** self.num2
        elif self.operation == "%":
            self.result = self.num1 % self.num2
        elif self.operation == "r":
            self.result = self.num1 ** (1/self.num2)
        elif self.operation == "!":
            self.result = math.factorial(self.num1)
        elif self.operation == "sin":
            self.result = math.sin(self.num1)
        elif self.operation == "cos":
            self.result = math.cos(self.num1)
        elif self.operation == "tan":
            self.result = math.tan(self.num1)
        elif self.operation == "ln":
            self.result = math.log(self.num1)
        else:
            print('Invalid operation')

    def get_nums(self):
        # Check if the operation is unary or binary (i.e. has 2 operands)
        # If it is unary, you only need to get and set num1
        # If it is binary, get and set num2
        # '!', 'sin', 'cos', 'tan', 'ln' are unary
        # '^', 'r', '%', '+', '-', '*', and '/' are binary
        if self.operation in '+-*/^r%':
            num1 = int(input('Enter first number: '))
            num2 = int(input('Enter second number: '))
            self.set_num1(num1)
            self.set_num2(num2)
        elif self.operation in '!sincostanln':
            num1 = int(input('Enter first number: '))
            self.set_num1(num1)
        else:
            print('Invalid operation')

    def get_user_input_operation(self):
        operation = input(
            'Simple Operators (+, -, *, /)\nScientific Operators (^, r, %, !, sin, cos, tan, ln)\nEnter operation: ')
        return operation

    def run(self):
        while self.on:
            self.set_operation()
            self.get_nums()
            self.sci_calculate()
            print(self.result)
            self.continue_prompt()
        print('Goodbye')


def main():
    calc = ScientificCalculator()
    calc.run()


if __name__ == '__main__':
    main()
