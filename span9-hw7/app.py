import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# determine the directory of the script so that the sqlite database
# file can be referenced with a relative path ("library.db")
appdir = os.path.abspath(os.path.dirname(__file__))

# configure app’s database access
app.config["SQLALCHEMY_DATABASE_URI"] = \
	f"sqlite:///{os.path.join(appdir, 'library.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize the SQLAlchemy database adaptor
db = SQLAlchemy(app)

# [[ Define Models Here ]]

books = db.Table('books',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    middlename = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    books = db.relationship('Book', secondary=books, lazy='subquery', backref=db.backref('authors',lazy=True))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

# drop any existing tables in the database
db.drop_all()

# create all the tables necessary according to my db.Model subclasses
db.create_all()


book_1 = Book(id="1", title="Don Quixote", isbn="1001", publisher="asdfghjkl", year="1998" )
book_2 = Book(id="2", title="The Lord of the Rings", isbn="1002", publisher="asdfghjkl", year="1998" )
book_3 = Book(id="3", title="The Hobbit", isbn="1003", publisher="asdfghjkl", year="1998" )
book_4 = Book(id="4", title="The Talisman", isbn="1004", publisher="asdfghjkl", year="1998" )

# define all of your authors (pointing to books)
author_1 = Author(id="12", firstname="Martin1", middlename="Sam1", lastname="Cruise1", dob="1998-10-10", books=[book_1])
author_2 = Author(id="13", firstname="Martin2", middlename="Sam2", lastname="Cruise2", dob="1998-10-11", books=[book_2,book_3])
author_3 = Author(id="14", firstname="Martin3", middlename="Sam3", lastname="Cruise3", dob="1998-10-12", books=[book_4])
author_4 = Author(id="15", firstname="Martin4", middlename="Sam4", lastname="Cruise4", dob="1998-10-13", books=[book_4])


# add all of these items to the database session
db.session.add_all([book_1, book_2, book_3, book_4])
db.session.add_all([author_1, author_2, author_3, author_4])


# commit these changes to the database
db.session.commit()

# Before you hand in your script, double check the contents of library.db to 
# make sure that it matches the examples you added.