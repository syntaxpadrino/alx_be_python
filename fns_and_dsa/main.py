from arithmetic_operations import perform_operation
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    try:
        result = perform_operation(num1, num2, operation)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()