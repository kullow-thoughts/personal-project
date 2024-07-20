from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
from config import db


bcrypt = Bcrypt()

# User model
class User(db.Model, SerializerMixin):
    '''Represents a user in the system.'''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)

    # Relationships
    libraries = db.relationship('Library', back_populates='user')

    # Association
    books = association_proxy('libraries', 'book', creator=lambda book_object: Library(book=book_object))

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, the_password):
        pass_hash = bcrypt.generate_password_hash(the_password.encode('utf-8'))
        self._password_hash = pass_hash.decode('utf-8')

    def authenticate(self, the_password):
        return bcrypt.check_password_hash(self._password_hash, the_password)

    @validates('username')
    def validate_username(self, key, the_username):
        if len(the_username) < 1:
            raise ValueError('The username should not be empty')
        return the_username

    @validates('email')
    def validate_email(self, key, the_email):
        if len(the_email) < 1:
            raise ValueError('Email address should not be empty')
        return the_email

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

    def __repr__(self):
        return f"<User {self.id} : {self.username}, {self.email}>"

# Book model
class Book(db.Model, SerializerMixin):
    '''Represents a book in the system.'''
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    image_url = db.Column(db.String)

    # Relationships
    libraries = db.relationship('Library', back_populates='book')

    # Association
    users = association_proxy('libraries', 'user', creator=lambda user_object: Library(user=user_object))

    @validates('title')
    def validate_title(self, key, the_title):
        if len(the_title) < 1:
            raise ValueError("A book must have a title")
        return the_title

    def __repr__(self):
        return f"<Book {self.id}: {self.title} - {self.image_url}>"

# Author model
class Author(db.Model, SerializerMixin):
    '''Represents an author in the system.'''
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)
    biography = db.Column(db.String)

    # Relationships
    libraries = db.relationship('Library', back_populates='author')

    # Association proxy
    books = association_proxy('libraries', 'book', creator=lambda book_obj: Library(book=book_obj))

    @validates('name')
    def validate_name(self, key, the_author_name):
        if len(the_author_name) < 1:
            raise ValueError("The author's name can't be empty")
        return the_author_name

    @validates('contact')
    def validate_contact(self, key, the_contact):
        if len(the_contact) < 1:
            raise ValueError("The author's contact can't be empty")
        return the_contact

    def __repr__(self):
        return f"<Author {self.id}: {self.name}, Contact: {self.contact}, Image URL: {self.image_url}, Biography: {self.biography}>"

# Genre model
class Genre(db.Model, SerializerMixin):
    '''Represents a genre in the system.'''
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    # Relationships
    libraries = db.relationship('Library', back_populates='genre')

    # Association
    books = association_proxy('libraries', 'book', creator=lambda book_obj: Library(book=book_obj))

    @validates('name')
    def validate_name(self, key, the_genre_name):
        if len(the_genre_name) < 1:
            raise ValueError('The Genre must have a name')
        return the_genre_name

    @validates('type')
    def validate_type(self, key, the_genre_type):
        if the_genre_type not in ['Fiction', 'Non-Fiction']:
            raise ValueError('Genre type must be either "Fiction" or "Non-Fiction"')
        return the_genre_type

    def __repr__(self):
        return f"<Genre {self.id}: {self.name}, Type: {self.type}>"

# Library model
class Library(db.Model, SerializerMixin):
    '''Represents a library entry.'''
    __tablename__ = 'libraries'

    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    author = db.relationship('Author', back_populates='libraries')
    user = db.relationship('User', back_populates='libraries')
    genre = db.relationship('Genre', back_populates='libraries')
    book = db.relationship('Book', back_populates='libraries')
