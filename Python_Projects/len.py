
a = """
    Select operation
    1.Count the input
    """
print(a)

choice = int(input("Select the action to perform "))

if choice == 1:
    User_Text = input(("Please enter the text to count here "))
    print(len(User_Text))
