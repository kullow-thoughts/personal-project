#!/usr/bin/env python3
from flask import request, make_response, jsonify, session
from flask_restful import Resource
from flask_migrate import Migrate
from config import app, db, api
from models import User, Book, Library, Author, Genre

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Signup(Resource):

    def post(self):
        data = request.get_json()
        new_username = data.get('username')
        new_email = data.get('email')
        new_password = data.get('password')

        if len(new_username) < 1:
            response_dict = {"error" : "Username can't be empty"}
            return make_response(jsonify(response_dict), 422)
        elif User.query.filter(User.username == new_username).first():
            response_dict = {"error" : "Username must be unique"}
            return make_response(jsonify(response_dict), 422)
        else:
            new_validated_username = new_username

        if len(new_email) < 1:
            response_dict = {"error" : "Email must not be empty"}
            return make_response(jsonify(response_dict), 422)
        elif User.query.filter_by(email = new_email).first():
            response_dict = {"error" : "Email must be unique"}
            return make_response(jsonify(response_dict), 422)
        else:
            new_validated_email = new_email
        
        new_user = User(
            username = new_validated_username,
            email = new_validated_email
        )

        new_user.password_hash = new_password

        db.session.add(new_user)
        db.session.commit()

        new_user_dict = new_user.to_dict()
        response = make_response(jsonify(new_user_dict), 201)
        return response

class Login(Resource):

    def post(self):
        data = request.get_json()
        the_email = data.get('email')
        the_password = data.get('password')
        user = User.query.filter(User.email == the_email).first()

        if user and user.authenticate(the_password):
            session['user_id'] = user.id
            user_dict = user.to_dict()
            return make_response(jsonify(user_dict), 200)
        else:
            response_body = {"error" : "Wrong Password/email"}
            response = make_response(jsonify(response_body), 401)
            return response

class Refresh(Resource):
    def get(self):
        user = User.quer.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict()
        else:
            resp_dict = {"error" : "Please login"}
            response = make_response(jsonify(resp_dict), 401)
            return response
        
class Logout(Resource):
    def delete(self):
        session["user_id"] = None
        return make_response(jsonify({}), 204)

    
class Books(Resource):

    ##GET ALL BOOKS
    def get(self):
        # if "user_id" not in session:
        #     body = {"error" : "Please login"}
        #     return make_response(jsonify(body), 403)
        
        book_list = [book.to_dict(rules=('-libraries',)) for book in Book.query.all()]
        response = make_response(jsonify(book_list), 200)
        return response
    
    ##ADD A BOOK
    def post(self):
        data = request.get_json()
        new_title = data.get('title')
        # new_genre = data.get('genre')
        # new_author_name = data.get('author_name')
        new_content = data.get('content')
        new_image_url = data.get('image_url')

        ##validate title
        if len(new_title) < 1:
            resp_dict = {"error" : "Book title can't be empty"}
            return make_response(jsonify(resp_dict), 422)
        else:
            new_validated_title = new_title

        ##validate author
        # if len(new_author_name) < 1:
        #     response_body = {"error" : "A book must have an author"}
        #     response = make_response(jsonify(response_body), 422)
        #     return response
        # else:
        #     new_validated_author_name = new_author_name
        
        
        new_book = Book(
            title = new_validated_title,
            # genre = new_genre,
            image_url = new_image_url,
            content = new_content
            # author_name = new_validated_author_name
        )

        if not new_book:
            resp_dict = {"error" : "Unprocessable entry"}
            response = make_response(jsonify(resp_dict), 422)
            return response
        else:
            db.session.add(new_book)
            db.session.commit()

            new_book_dict = new_book.to_dict(rules=('-libraries',))
            response = make_response(jsonify(new_book_dict), 201)
            return response
    
class BookById(Resource):


    ##GET A SINGLE BOOK
    def get(self, the_id):
        book = Book.query.filter(Book.id == the_id).first()
        if not book:
            resp_dict = {"error" : "Book wasn't found"}
            response = make_response(jsonify(resp_dict), 404)
            return response
        else:
            book_dict = book.to_dict(rules=('-libraries', ))
            response = make_response(jsonify(book_dict), 200)
            return response
        
    ##EDIT A SINGLE BOOK (PATCH)
    def patch(self, the_id):
        data = request.get_json()
        book = Book.query.filter(Book.id == the_id).first()
        if not book:
            resp_dict = {"error" : "Book wasn't found"}
            return make_response(jsonify(resp_dict), 404)
        else:
            for attr in data:
                setattr(book, attr, data.get(attr))

            db.session.add(book)
            db.session.commit()

            book_dict = book.to_dict(rules=('-libraries', ))
            response = make_response(jsonify(book_dict), 200)
            return response
    
    ##DELETE A SINGLE BOOK
    def delete(self, the_id):
        book = Book.query.filter(Book.id == the_id).first()
        if book:
            db.session.delete(book)
            db.session.commit()

            return make_response(jsonify({}), 204)
        else:
            return make_response(jsonify({"error" : "Book wasn't found"}), 404)

###> From Front<#############
class Users(Resource):
    def get(self):
        user_list = [user.to_dict() for user in User.query.all()]
        response = make_response(jsonify(user_list), 200)
        return response
    
    def post(self):
        data = request.get_json()
        new_username = data.get('username')
        new_email = data.get('email')
        new_password = data.get('password')
        

        if len(new_username) < 1:
            response_dict = {"error" : "Username can't be empty"}
            return make_response(jsonify(response_dict), 422)
        elif User.query.filter(User.username == new_username).first():
            response_dict = {"error" : "Username must be unique"}
            return make_response(jsonify(response_dict), 422)
        else:
            new_validated_username = new_username

        if len(new_email) < 1:
            response_dict = {"error" : "Email must not be empty"}
            return make_response(jsonify(response_dict), 422)
        elif User.query.filter_by(email = new_email).first():
            response_dict = {"error" : "Email must be unique"}
            return make_response(jsonify(response_dict), 422)
        else:
            new_validated_email = new_email
        
        new_user = User(
            username = new_validated_username,
            email = new_validated_email
        )

        new_user.password_hash = new_password

        db.session.add(new_user)
        db.session.commit()

        new_user_dict = new_user.to_dict()
        response = make_response(jsonify(new_user_dict), 201)
        return response


class UserById(Resource):
    def get(self, the_id):
        user = User.query.filter(User.id == the_id).first()
        if user:
            user_dict = user.to_dict()
            response = make_response(jsonify(user_dict), 200)
            return response
        else:
            resp_dict = {"error" : "user not found"}
            return make_response(jsonify(resp_dict), 404)


api.add_resource(UserById, '/api/users/<int:the_id>')

class UserLibrary(Resource):
    def get(self, the_user_id):
        user = User.query.filter(User.id == the_user_id).first()
        library_books = [
            {
                'id': library.id,
                'book': {
                    'id': library.book.id,
                    'title': library.book.title,
                    'author_name': library.book.author_name,
                    'genre': library.book.genre,
                    'image_url': library.book.image_url,
                },
                'note': library.notes
            }
            for library in user.libraries
        ]
        return make_response(jsonify(library_books), 200)
    
api.add_resource(UserLibrary, '/api/users/<int:the_user_id>/library')

class AddNoteToBook(Resource):
    def post(self, book_id):
        data = request.get_json()
        new_note = data.get('note')

        if not new_note:
            return {'message': 'Note cannot be blank'}, 422

        library = Library.query.filter_by(book_id = book_id).first()

        library.notes = new_note
        db.session.commit()

        resp_dict = {'id': library.id, 'note': library.notes}
        return make_response(jsonify(resp_dict))

api.add_resource(AddNoteToBook, '/api/library/<int:book_id>/add_note')

    
class Genres(Resource):

    def get(self):
        # if "user_id" not in session:
        #     body = {"error" : "Please login"}
        #     return make_response(jsonify(body), 403)
        genre_list = [genre.to_dict(rules=('-libraries', )) for genre in Genre.query.all()]
        response = make_response(jsonify(genre_list), 200)
        return response
    def post(self):
        data = request.get_json()
        new_name = data.get('name')
        new_type = data.get('type')

        if len(new_name) < 1:
            resp_dict = {"error" : "Genre name can't be empty"}
            response = make_response(jsonify(resp_dict), 422)
            return response
        else:
            new_validated_name = new_name

        if len(new_type) < 1:
            resp_dict = {"error" : "Genre type cannot be empty"}
            response = make_response(jsonify(resp_dict), 422)
            return response
        elif new_type not in ('Fiction', 'Non-Fiction'):
            resp_dict = {"error" : "Genre type can be either fiction or not"}
            response = make_response(jsonify(resp_dict), 422)
            return response
        else:
            new_validated_type = new_type

        new_genre = Genre(
            name = new_validated_name,
            type = new_validated_type  
        )

        db.session.add(new_genre)
        db.session.commit()

        response_dict = new_genre.to_dict(rules=('-libraries', ))
        response =  make_response(jsonify(response_dict), 201)
        return response
    
class GenreById(Resource):
    def get(self, the_id):
        genre = Genre.query.filter(Genre.id == the_id).first()
        if not genre:
            body = {"error" : "Genre not found"}
            resp = make_response(jsonify(body), 404)
            return resp
        genre_dict = genre.to_dict(rules=('-libraries', ))
        response = make_response(jsonify(genre_dict), 200)
        return response
    
    def patch(self, the_id):
        genre = Genre.query.filter(Genre.id == the_id).first()
        data = request.get_json()

        if not genre:
            return make_response(jsonify({"error" : "Genre not found"}), 401)

        for attr in data:
            setattr(genre, attr, data.get(attr))
        
        db.session.add(genre)
        db.session.commit()

        genre_dict = genre.to_dict(rules=('-libraries', ))
        response = make_response(jsonify(genre_dict), 200)
        return response
    
    def delete(self, the_id):
        genre = Genre.query.filter(Genre.id == the_id).first()

        db.session.delete(genre)
        db.session.commit()

        return make_response(jsonify({}), 204)
    
class Authors(Resource):
    def get(self):
        # if "user_id" not in session:
        #     body = {"error" : "Please login"}
        #     return make_response(jsonify(body), 403)
        author_list = [author.to_dict(rules=('-libraries', )) for author in Author.query.all()]
        response = make_response(jsonify(author_list), 200)
        return response
    def post(self):
        data = request.get_json()
        new_name = data.get('name')
        new_contact = data.get('contact')

        if len(new_name) < 1:
            resp_dict = {"error" : "Author name cannot be blank"}
            response = make_response(jsonify(resp_dict), 422)
            return response
        else:
            new_validated_name = new_name
        
        if len(new_contact) < 1:
            resp_dict = {"error" : "Author contact cannot be blank"}
            response = make_response(jsonify(resp_dict), 422)
            return response
        else:
            new_validated_contact = new_contact
        
        new_author = Author(
            name = new_validated_name,
            contact = new_validated_contact
        )

        db.session.add(new_author)
        db.session.commit()

        new_author_dict = new_author.to_dict(rules=('-libraries', ))
        response = make_response(jsonify(new_author_dict), 201)
        return response

class AuthorsById(Resource):
    def get(self, the_id):
        author = Author.query.filter(Author.id == the_id).first()
        if author:
            author_dict = author.to_dict(rules=('-libraries', ))
            response = make_response(jsonify(author_dict), 200)
            return response
        else:
            resp_dict = {"error" : "Author Not Found"}
            return make_response(jsonify(resp_dict), 404)
    
    def patch(self, the_id):
        author = Author.query.filter(Author.id == the_id).first()
        if not author:
            resp_dict = {"error" : "Author Not Found"}
            return make_response(jsonify(resp_dict), 404)
        else:
            data = request.get_json()
            for attr in data:
                setattr(author, attr, data.get(attr))
            
            db.session.add(author)
            db.session.commit()

            author_dict = author.to_dict(rules=('-libraries', ))
            response = make_response(jsonify(author_dict), 200)
            return response
    def delete(self, the_id):
        author = Author.query.filter(Author.id == the_id).first()
        if not author:
            resp_dict = {"error" : "Author Not Found"}
            return make_response(jsonify(resp_dict), 404)
        else:
            db.session.delete(author)
            db.session.commit()

            return make_response(jsonify({}), 204)
        
class UserBooks(Resource):
    def get(self):
        # if 'user_id' not in session:
        #     body = {"error" : "Please login"}
        #     response = make_response(jsonify(body), 403)
        #     return response
        user = User.query.filter(User.id == session.get('user_id')).first()
        book_list =  user.books

        book_dict = [book.to_dict(rules=('-libraries', )) for book in book_list]
        resp = make_response(jsonify(book_dict), 200)
        return resp
    
class GenreBooks(Resource):
    def get(self, the_id):
        genre = Genre.query.filter(Genre.id == the_id).first()
        if genre:
            book_list = [book.to_dict(rules=('-libraries', )) for book in genre.books]
            response = make_response(jsonify(book_list), 200)
            return response
        
class AuthorBooks(Resource):
    def get(self, the_id):
        author = Author.query.filter(Author.id == the_id).first()
        if author:
            book_list = [book.to_dict(rules=('-libraries', )) for book in author.books]
            response = make_response(jsonify(book_list), 200)
            return response
        


        

api.add_resource(AuthorBooks, '/authors/<int:the_id>/books') # a list of book by an author
api.add_resource(GenreBooks, '/genres/<int:the_id>/books') # a list of books in a genre
api.add_resource(UserBooks, '/user/books')
api.add_resource(AuthorsById, '/authors/<int:the_id>')
api.add_resource(GenreById, '/genres/<int:the_id>')
api.add_resource(Signup, '/signup') ##remove if we adopt front /api/users
api.add_resource(Login, '/login')
api.add_resource(Refresh, '/confirm_session')
api.add_resource(Logout, '/logout')
api.add_resource(Books, '/books')
api.add_resource(BookById, '/books/<int:the_id>')
api.add_resource(Genres, '/genres')
api.add_resource(Authors, '/authors')

###>>> from the front-end guyz
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(port=5555, debug=True)