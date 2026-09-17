

book = {}

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
        Author = input("Enter the Author:")
        Year = input("Enter the Year:")

        book[title] = {
            "Author": Author,
            "Year": Year
        }
        print("Book added.")
    if choice == "2":
        title = input("Enter the book title to remove:")
        if title in book:
            del book[title]
            print("book removed")
        else:
            print("error: enter the correct book title")
    

if __name__ == "__main__":
    main()