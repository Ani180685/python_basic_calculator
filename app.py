def addition(terms):
    res = 0
    for i in range(0, terms):
        num = int(input("Enter number to add: "))
        res += num
    return res


def subtract(terms):
    res = 0
    for i in range(0, terms):
        num = int(input("Enter a number to subtract: "))
        res -= num
    return res


def multiply(terms):
    res = 1
    for i in range(0, terms):
        num = int(input("Enter a number to multiply: "))
        res *= num
    return res


def division(terms):
    res = 1
    for i in range(0, terms):
        num = int(input("Enter a number to divide: "))
        res /= num
    return res


def main():
    print("Welcome to the calculator app")
    print("Simple Calculator App")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Choose your option: ")
    terms = int(input("Enter number of terms: "))

    if choice == '1':
        print(f"\nSum: {addition(terms)}")
    elif choice == '2':
        print(f"\nResult: {subtract(terms)}")
    elif choice == '3':
        print(f"\nProduct: {multiply(terms)}")
    elif choice == '4':
        print(f"\nResult: {division(terms)}")


main()
