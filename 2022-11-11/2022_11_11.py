## Python Calculator

# Python has a built-in module called math, which allows us to perform mathematical tasks on numbers.

# The math module has a set of built-in methods that you can use on numbers.

# Calculator interface

# Create a calculator interface

# Import the math module

import math

# Create a function that takes two numbers and an operator as input

def calculator(num1, num2, operator):

        # Create a variable to store the result


        result = 0

        # Check if the operator is +

        if operator == "+":

            # Add the two numbers

            result = num1 + num2

        # Check if the operator is -

        elif operator == "-":

            # Subtract the two numbers

            result = num1 - num2

        # Check if the operator is *

        elif operator == "*":

            # Multiply the two numbers

            result = num1 * num2

        # Check if the operator is /

        elif operator == "/":

            # Divide the two numbers

            result = num1 / num2

        # Check if the operator is %

        elif operator == "%":

            # Divide the two numbers and return the remainder

            result = num1 % num2

        # Check if the operator is ^

        elif operator == "^":

            # Raise num1 to the power of num2

            result = num1 ** num2

        # Check if the operator is sqrt

        elif operator == "sqrt":

            # Return the square root of num1

            result = math.sqrt(num1)

        # Check if the operator is log

        elif operator == "log":

            # Return the log of num1

            result = math.log(num1)

        # Check if the operator is sin

        elif operator == "sin":

            # Return the sine of num1

            result = math.sin(num1)

        # Check if the operator is cos

        elif operator == "cos":

            # Return the cosine of num1

            result = math.cos(num1)

        # Check if the operator is tan

        elif operator == "tan":

            # Return the tangent of num1

            result = math.tan(num1)

        # Check if the operator is floor

        elif operator == "floor":

            # Return the floor of num1

            result = math.floor(num1)

        # Check if the operator is ceil

        elif operator == "ceil":

            # Return the ceiling of num1

            result = math.ceil(num1)

        # Check if the operator is round

        elif operator == "round":

            # Return the rounded value of num1

            result = round(num1)

        # Return the result

        return result


