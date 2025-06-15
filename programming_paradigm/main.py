# import sys
# from robust_division_calculator import safe_divide
# def main():
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <numerator> <denominator>")
#         sys.exit(1)

#     numerator = sys.argv[1]
#     denominator = sys.argv[2]

#     result = safe_divide(numerator, denominator)
#     print(result)
# if __name__ == "__main__":
#     main()

from library_management import Library, Book
def main():
    library = Library()

    # Adding books to the library
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    library.add_book(book1)
    library.add_book(book2)

    # Listing available books
    print("Available books in the library:")
    library.list_available_books()

    # Checking out a book
    print("\nChecking out '1984':")
    library.check_out_book("1984")
    library.list_available_books()

    # Returning a book
    print("\nReturning '1984':")
    library.return_book("1984")
    library.list_available_books()

    # Trying to check out a book that is already checked out
    print("\nChecking out '1984' again:")   
    library.check_out_book("1984")
    library.list_available_books()
    # Trying to return a book that was not checked out
    print("\nReturning '1984' again:")
    library.return_book("1984")
    library.list_available_books()
if __name__ == "__main__":
    main()  