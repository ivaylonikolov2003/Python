book = input()

books_counter = 0
is_book_found = False

curr_book = input()
while curr_book != "No More Books":
    if curr_book == book:
        is_book_found = True
        break

    books_counter += 1
    curr_book = input()

if is_book_found:
    print(f"You checked {books_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_counter} books.")