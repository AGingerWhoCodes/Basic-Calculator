def StartCalculator():

    num1 = float(input("Enter a number (Not a decimal):"))

    print("")

    num2 = float(input("Enter another number (Not a decimal):"))

    print("")

    operation = input("Enter '+' for addition\n '-' for subtraction \n '*' for multiplication\n and '/' for division\n")



    if operation == '+':

            answer = (num1 + num2)

            print("")

            print(answer)

    elif operation == '-':

            answer = (num1 - num2)

            print("")

            print(answer)

    elif operation == '*':

            answer = (num1 * num2)

            print("")

            print(answer)

    elif operation == '/':

            answer = (num1 / num2)

            print("")

            print(answer)

while(True):
    StartCalculator()
