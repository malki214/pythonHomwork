from book import Book
from library import Library
import pytest

myLibrary = Library()


# הוספת ספרים (add_book)
# ✅ בדיקה שהפונקציה מוסיפה ספר חדש לרשימת הספרים במערכת.
@pytest.mark.parametrize("title, author", [("title", "author"), ("", "")])
def test_add_book(title, author):
    new_book = Book(title, author)
    myLibrary.add_book(new_book)
    assert new_book in myLibrary.books


# #  הוספת משתמשים (add_user)
# # ✅ בדיקה שהפונקציה מוסיפה משתמש חדש לרשימת המשתמשים.
@pytest.mark.user
@pytest.mark.parametrize("user_name", ["Malki", "Chani","\ndfg"])
def test_add_user(user_name):
    myLibrary.add_user(user_name)
    assert user_name in myLibrary.users


# # השאלת ספר (check_out_book)
# # ✅ בדיקה שהספר הושאל בהצלחה למשתמש רשום.
def test_check_out_book():
    myLibrary.check_out_book("Malki", myLibrary.books[0])
    assert myLibrary.books[0].is_checked_out
    assert myLibrary.checked_out_books["Malki"] == myLibrary.books[0]


# החזרת ספר (return_book)
# ✅ בדיקה שהספר מוחזר בהצלחה לאחר שהושאל.
@pytest.mark.return_book
def test_return_book():
    book = Book("ttttt", "aaaaa")
    myLibrary.add_book(book)
    myLibrary.add_user("Sara")
    myLibrary.check_out_book("Sara", book)

    myLibrary.return_book("Sara", book)

    assert not book.is_checked_out
    assert "Sara" not in myLibrary.checked_out_books


# חיפוש ספרים (search_books)
# ✅ בדיקה שהפונקציה תומכת בחיפושים חלקיים (חיפוש לפי חלק מהשם).
def test_search_books():
    book = Book("ttttt", "aaaaa")
    myLibrary.add_book(book)
    book2 = Book("dfgdfg", "dfg")
    myLibrary.add_book(book2)
    assert book in myLibrary.search_books("tt")
    assert book2 not in myLibrary.search_books("tt")



