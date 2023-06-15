from models.book import *

book1 = Book("The Shining", "Stephen King", "Horror", False)
book2 = Book("AC Revelation", "Oliver Bowden", "Fantasy", False)
book3 = Book("Fairytales", "Angela Carters", "Childrens", True)
books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def remove_book(book):
    books.remove(book)




    

