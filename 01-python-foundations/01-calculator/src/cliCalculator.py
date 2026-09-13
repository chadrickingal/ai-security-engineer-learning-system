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

# Choosing operator function based on input
def operation(operator, firstNumber, secondNumber):
    match operator:
        case '+':
            print("\nAddition (+)")
            add(firstNumber, secondNumber)
        case '-':
            print("\nSubtraction (-)")
            sub(firstNumber, secondNumber)
        case '*': 
            print("\nMultiply (*)")
            mult(firstNumber, secondNumber)
        case '/':
            print("\nDivision (/)")
            div(firstNumber, secondNumber)
        case _:
            print("\nOperator not Found [404]")

# Output Function to print the results
def output(operator, firstNumber, secondNumber):
    match operator:
        case '+':
            print(f"Result: {firstNumber} {operator} {secondNumber} = {add(firstNumber,secondNumber)}")
        case '-':
            print(f"Result: {firstNumber} {operator} {secondNumber} = {sub(firstNumber,secondNumber)}")
        case '*': 
            print(f"Result: {firstNumber} {operator} {secondNumber} = {mult(firstNumber,secondNumber)}")
        case '/':
            print(f"Result: {firstNumber} {operator} {secondNumber} = {div(firstNumber,secondNumber)}")
        case _:
            print("Result not Found [404")

# Inputs with error handling main function
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

        operation(operator, firstNumber, secondNumber)
        output(operator, firstNumber, secondNumber)

        choice = input("\nCalculate again? [Y/n] ")
        if choice.lower() == "n":
            break
        elif choice.lower() == 'y':
            continue
        
    except ValueError:
        print("\nInvalid Inputs\n")
    except ZeroDivisionError:
        print("\nUndefined\n")


