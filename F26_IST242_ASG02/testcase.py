from Personal_library import book, add_book


def test_add_book():
    book.clear()

    add_book("The Hobbit", "J.R.R. Tolkien", "1937")

    assert "The Hobbit" in book
    assert book["The Hobbit"]["Author"] == "J.R.R. Tolkien"
    assert book["The Hobbit"]["Year"] == "1937"


def test_add_multiple_books():
    book.clear()

    add_book("The Hobbit", "J.R.R. Tolkien", "1937")
    add_book("Harry Potter", "J.K. Rowling", "1997")

    assert "The Hobbit" in book
    assert "Harry Potter" in book
    assert len(book) == 2


def test_book_information():
    book.clear()

    add_book("1984", "George Orwell", "1949")

    assert book["1984"]["Author"] == "George Orwell"
    assert book["1984"]["Year"] == "1949"


def test_duplicate_book():
    book.clear()

    add_book("The Hobbit", "J.R.R. Tolkien", "1937")
    add_book("The Hobbit", "J.R.R. Tolkien", "1937")

    assert len(book) == 1