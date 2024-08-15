# Task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")
    return library

new_book = (input("Name of the book: "), input("Author: "))

library = add_book(library, new_book)

print("\nThe library has been updated:", library)



