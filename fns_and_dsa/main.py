# from arithmetic_operations import perform_operation
# def main():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

#     try:
#         result = perform_operation(num1, num2, operation)
#         print(f"The result of {operation}ing {num1} and {num2} is: {result}")
#     except ValueError as e:
#         print(e)
# if __name__ == "__main__":
#     main()

from shopping_list_manager import display_menu, add_item, remove_item, view_list

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()

if __name__ == "__main__":
    main()