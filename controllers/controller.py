from flask import render_template, redirect, request
from app import app
from models.library import *
from models.book import *

@app.route('/library', methods =["GET"])
def index():
    return render_template('index.html', title="Library", books=books)

@app.route('/library/<index>', methods =['GET'])
def single_book(index):
    book = books[int(index)]
    return render_template('base.html', title="Library", book=book)

@app.route('/library/addedbooks', methods = ['POST'])
def add_book():
    book_author = request.form['author']
    book_title = request.form['title']
    book_genre = request.form['genre']
    new_book = Book(book_author, book_title, book_genre, False)
    add_new_book(new_book)
    return redirect("/library")

@app.route("/library/delete/<index>", methods = ["GET", "POST"])
def remove(index):
     removing_book = books[int(index)]
     remove_book(removing_book)
     return redirect("/library")

# @app.route("/library/checkout/<index>", methods = ["POST"])
# def checkbox_checkout():
#     checkout_book = books[int(index)]
#     ()

