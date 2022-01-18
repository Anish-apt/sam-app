def add(num1, num2):
	return num1 + num2


def subtract(num1, num2):
	return num1 - num2


def multiply(num1, num2):
	return num1 * num2


def divide(num1, num2):
	return num1 / num2

def lambda_handler(event, context):
    
	op = event['op']
	number_1 = int(event['a'])
	number_2 = int(event['b'])

	if op == '+':
		print(number_1, "+", number_2, "=",
						add(number_1, number_2))

	elif op == '-':
		print(number_1, "-", number_2, "=",
						subtract(number_1, number_2))

	elif op == '*':
		print(number_1, "*", number_2, "=",
						multiply(number_1, number_2))

	elif op == '/':
		print(number_1, "/", number_2, "=",
						divide(number_1, number_2))
