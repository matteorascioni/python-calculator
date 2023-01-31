#to start use this program please run this commands in order
#1) python3 -m venv venv
#2) pip3 install replit
from replit import clear
from logo import logo

#operations functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#operations dictionary to declare the symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    #extract the symbols from the ditctionary and print it to the user
    for symbol in operations:
        print(symbol)

    #flag for the while cicle
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #checking if the user want to continue with his math operations
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            #if yes replace the previous the new n1 with the previous answer
            num1 = answer
        else:
            # the no stop the while cicle, clear the screen and use recursion to call the calcualtor function to restart all the program from the beginning
            should_continue = False
            clear()
            calculator()

#calling the calculator() to start the program for the first time, then will be thanks to recursion
calculator()