import React, { useState, useEffect } from 'react';
import './LibraryPage.css';

const BookshelfPage = () => {
  const [books, setBooks] = useState([]);
  const [library, setLibrary] = useState([]);

  useEffect(() => {
    const storedBooks = JSON.parse(localStorage.getItem('books')) || [];
    const storedLibrary = JSON.parse(localStorage.getItem('library')) || [];
    setBooks(storedBooks);
    setLibrary(storedLibrary);
  }, []);

  useEffect(() => {
    localStorage.setItem('books', JSON.stringify(books));
  }, [books]);

  useEffect(() => {
    localStorage.setItem('library', JSON.stringify(library));
  }, [library]);

  // Function to add a new book to the list
  const handleAddBook = (event) => {
    event.preventDefault();
    const newBook = {
      id: Date.now(),
      title: event.target.title.value,
      genre: event.target.genre.value,
      author_name: event.target.author.value,
      likes: 0,
      comments: []
    };
    setBooks([...books, newBook]);
    event.target.reset();
  };

  // Function to add a book to the library
  const handleAddToLibrary = (book) => {
    const bookToAdd = { ...book, likes: 0, comments: [] };
    setLibrary([...library, bookToAdd]);
  };

  // Function to remove a book from the library
  const handleRemoveFromLibrary = (bookId) => {
    const updatedLibrary = library.filter((book) => book.id !== bookId);
    setLibrary(updatedLibrary);
  };

  // Function to remove a book from the books list
  const handleRemoveFromBooks = (bookId) => {
    const updatedBooks = books.filter((book) => book.id !== bookId);
    setBooks(updatedBooks);
  };

  // Function to handle adding a like to a book
  const handleAddLike = (bookId) => {
    const updatedLibrary = library.map((book) =>
      book.id === bookId ? { ...book, likes: book.likes + 1 } : book
    );
    setLibrary(updatedLibrary);
  };

  // Function to add a comment to a book in the library
  const handleAddComment = (bookId, comment) => {
    const updatedLibrary = library.map((book) =>
      book.id === bookId ? { ...book, comments: [...book.comments, comment] } : book
    );
    setLibrary(updatedLibrary);
  };

  return (
    <div className="BookshelfPage">
      <h2>Bookshelf</h2>
      <form className="add-book-form" onSubmit={handleAddBook}>
        <label>
          Title:
          <input type="text" name="title" required />
        </label>
        <label>
          Genre:
          <input type="text" name="genre" required />
        </label>
        <label>
          Author:
          <input type="text" name="author" required />
        </label>
        <button type="submit">Add Book</button>
      </form>
      
      <h3>Books</h3>
      <ul className="books-list">
        {books.map((book) => (
          <li key={book.id} className="book-item">
            <div className="book-info">
              <span className="book-title">{book.title}</span>
              <span className="book-genre">{book.genre}</span>
              <span className="book-author">{book.author_name}</span>
            </div>
            <div className="button-group">
              <button className="add-button" onClick={() => handleAddToLibrary(book)}>Add to Library</button>
              <button className="remove-button" onClick={() => handleRemoveFromBooks(book.id)}>Remove</button>
            </div>
          </li>
        ))}
      </ul>

      <h3>Library</h3>
      <ul className="library-list">
        {library.map((book) => (
          <li key={book.id} className="library-item">
            <div className="book-info">
              <span className="book-title">{book.title}</span>
              <span className="book-genre">{book.genre}</span>
              <span className="book-author">{book.author_name}</span>
            </div>
            <div className="book-actions">
              <div className="likes-section">
                <span>{book.likes} </span>
                <button className="like-button" onClick={() => handleAddLike(book.id)}>❤️</button>
              </div>
              {book.comments.length > 0 && (
                <ul className="comments-list">
                  {book.comments.map((comment, index) => (
                    <li key={index} className="comment-item">{comment}</li>
                  ))}
                </ul>
              )}
              <input
                type="text"
                className="comment-input"
                placeholder="Add comment..."
                onKeyDown={(e) => {
                  if (e.key === 'Enter') {
                    handleAddComment(book.id, e.target.value);
                    e.target.value = '';
                  }
                }}
              />
              <button className="remove-button" onClick={() => handleRemoveFromLibrary(book.id)}>Remove</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookshelfPage;
