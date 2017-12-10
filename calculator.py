num1 = int(input("Enter a number (Not a decimal):"))
print("")
num2 = int(input("Enter another number (Not a decimal):"))
print("")
operation = input("Enter '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division,")

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

