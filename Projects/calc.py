def add(x, y):
    return x + y


def test(x, y):
    return x * y


def divide(x, y):
    return x / y


def sub(x, y):
    return x - y


a = """
    ============L
    # 1. +      O
    # 2. *      R
    # 3. /      E
    # 4. -      N
    ============Z
"""
print(a)

choice = (input("Select the type of calculation "))
num1 = int(input("enter first number "))
num2 = int(input("enter second number "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 * num2)
elif choice == 3:
    print(num1 / num2)
elif choice == 4:
    print(num1 - num2)
else:
    print("Choose from the shown text")
