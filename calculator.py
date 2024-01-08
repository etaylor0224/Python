def add(x, y):
    return x + y

def subtract(x,y):
    return x -y
def mulitply(x,y):
    return x*y
def divide(x,y):
    return x / y


while True:
    choice = input("Please choose add(1), subtract(2), multiply(3), or divide(4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))

        except ValueError:
            print("Invalid input")
        if choice == '1':
            print(f"{num1} + {num2} =", add(num1,num2))
        elif choice == '2':
            print(f"{num1} - {num2} =", subtract(num1, num2))
        elif choice == '3':
            print(f"{num1} * {num2} =", mulitply(num1, num2))
        elif choice == '4':
            print(f"{num1} / {num2} =", divide(num1,num2))
        next_cal = input("Another calculation? yes/no:  ")
        if next_cal == ("no"):
            break
        else:
            print("Let's Go")