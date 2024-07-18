// src/components/BookDetailsModal.js
import React from 'react';
import './BookDetailsModal.css';

const BookDetailsModal = ({ book, onClose }) => {
  if (!book) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-button" onClick={onClose}>X</button>
        <div className="book-details">
          <img src={book.image} alt="Book Cover" className="book-image" />
          <div className="book-info">
            <h2 className="book-title">{book.title}</h2>
            <h3 className="book-author">{book.author}</h3>
            <p className="book-description">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis libero non risus accumsan, at maximus sapien blandit.
            </p>
            <p className="book-details">
              More details about the book can be displayed here, such as genre, publication date, etc.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookDetailsModal;
