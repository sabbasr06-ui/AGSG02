def display_menu():
    print("\n======= Personal Library Manager =======")
    print("1. Add a book title")
    print("2. remove a book title")
    print("3. list all book titles")
    print("4. search a book title")
    print("5. exit")

def main():
    display_menu()

    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the book title:")
        title = input("Enter the Author:")
        title = input("Enter the Year:")

        book[title] = {
            "Author": author,
            "Year": year
        }
        print("Book added.")

    if __name__ == "__main__":
        main()