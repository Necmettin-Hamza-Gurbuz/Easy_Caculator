def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
    print(num1, "+", num2, "=", addition(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid input")
