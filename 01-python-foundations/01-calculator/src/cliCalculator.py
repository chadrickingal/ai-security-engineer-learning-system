# CLI Simple Calculator 
# use function to separate the calculation logic

# Addition
def add(firstNumber, secondNumber):
    total = firstNumber + secondNumber
    return total

# Subtraction
def sub(firstNumber, secondNumber):
    total = firstNumber - secondNumber
    return total

# Multiplication
def mult(firstNumber, secondNumber):
    total = firstNumber * secondNumber
    return total

# Division
def div(firstNumber, secondNumber):
    total = firstNumber / secondNumber
    return total

# Output Function to print the results
def operation_Output(operator, firstNumber, secondNumber):
    match operator:
        case '+':
            print("\nAddition (+)")
            print(f"Result: {firstNumber} {operator} {secondNumber} = {add(firstNumber,secondNumber)}")
        case '-':
            print("\nSubtraction (-)")
            print(f"Result: {firstNumber} {operator} {secondNumber} = {sub(firstNumber,secondNumber)}")
        case '*': 
            print("\nMultiply (*)")
            print(f"Result: {firstNumber} {operator} {secondNumber} = {mult(firstNumber,secondNumber)}")
        case '/':
            print("\nDivision (/)")
            print(f"Result: {firstNumber} {operator} {secondNumber} = {div(firstNumber,secondNumber)}")
        case _:
            print("Result Not Found [404]")

# Inputs with error handling 
while True:

    try:
        print("============================")
        print("CLI Simple calculator")
        print("============================")
        print("\nNumbers")
        firstNumber = int(input(": "))
        secondNumber = int(input(": "))

        print("\nOperator |+|-|*|/|")
        operator = input(": ")

        operation_Output(operator, firstNumber, secondNumber)

        choice = input("\nCalculate again? [Y/n]\n:")
        if choice.lower() == "n":
            break
        elif choice.lower() == 'y':
            continue
        else: 
            print("Input Not Found [404]")
        
    except ValueError:
        print("\nInvalid Inputs\n")
    except ZeroDivisionError:
        print("\nUndefined\n")


