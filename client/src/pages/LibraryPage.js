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
    event.target.reset(); // Reset the form after submission
  };

  // Function to add a book to the library
  const handleAddToLibrary = (book) => {
    const bookToAdd = { ...book, likes: 0, comments: [] }; // Initialize likes and comments
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
      <form onSubmit={handleAddBook}>
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
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            {book.title} - {book.genre} - {book.author_name}{' '}
            <button onClick={() => handleAddToLibrary(book)}>Add to Library</button>
            <button onClick={() => handleRemoveFromBooks(book.id)}>Remove</button>
          </li>
        ))}
      </ul>
      <h3>Library</h3>
      <ul>
        {library.map((book) => (
          <li key={book.id}>
            {book.title} - {book.genre} - {book.author_name}{' '}
            <div>
              Likes: {book.likes}{' '}
              <button onClick={() => handleAddLike(book.id)}>❤️</button>
            </div>
            {book.comments.length > 0 && (
              <ul>
                {book.comments.map((comment, index) => (
                  <li key={index}>{comment}</li>
                ))}
              </ul>
            )}
            <input
              type="text"
              placeholder="Add comment..."
              onKeyDown={(e) => {
                if (e.key === 'Enter') {
                  handleAddComment(book.id, e.target.value);
                  e.target.value = '';
                }
              }}
            />
            <button onClick={() => handleRemoveFromLibrary(book.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BookshelfPage;
