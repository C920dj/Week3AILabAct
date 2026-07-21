def check_borrowing(overdue_books, status):
    """
    overdue_books: bool (True if student has overdue books)
    status: str ("active" or "suspended")
    """

    if overdue_books:
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Borrowing allowed"


def run_kiosk():
    successful_borrowers = 0

    while True:
        name = input("Enter student name (or 'exit' to quit): ").strip()

        if name.lower() == "exit":
            break

        overdue_input = input("Do you have overdue books? (yes/no): ").strip().lower()
        status_input = input("What is your status? (active/suspended): ").strip().lower()

        overdue_books = (overdue_input == "yes")

        result = check_borrowing(overdue_books, status_input)

        if result == "Borrowing allowed":
            
            try:
                num_books = int(input("How many books would you like to borrow? "))
            except ValueError:
                print("Invalid number entered. Defaulting to 0 books.")
                num_books = 0

            if num_books <= 0:
                print(f"{name}, you entered 0 (or fewer) books. No books will be borrowed.")
            elif num_books > 3:
                print(f"{name}, you can only borrow up to 3 books at a time. Limiting to 3.")
                successful_borrowers += 1
            else:
                print(f"{name}, you may borrow {num_books} book(s). Enjoy!")
                successful_borrowers += 1
        else:
            print(f"{name}: {result}")

        print("-" * 40)

    print(f"\nSession ended. Total students who successfully borrowed books: {successful_borrowers}")


run_kiosk()

# 6. What if a student types "Yes" instead of "yes"?

# Python sees "Yes" and "yes" as different because of the capital letter.
# If the code only checks for "yes", then typing "Yes" or "YES" wont match.
# Thats why using .lower() is important. It changes everything into lowercase
# first, so no matter how the student types it, the program will still work.

# 7. Why check overdue books before status?

# I think overdue books should be checked first because if a student has overdue
# books, they should not be allowed to borrow anymore even if their account is active.
# If the status gets checked first, the program might miss the overdue books
# and give the wrong result. So its better to check the overdue books first.

# 8. What about 0 books?

# If the student enters 0 books, it means they are not really borrowing anything.
# Their account is still okay if they have no overdue books and their status is active,
# but theres nothing to borrow. So the program just tells them no books were borrowed
# and it doesnt count them as a successful borrower.
