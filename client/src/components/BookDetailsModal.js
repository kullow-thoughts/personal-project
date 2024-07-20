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
                  An engrossing tale of adventure and intrigue, this book takes you on a journey through a richly detailed world where every page is filled with suspense and excitement. 
                  With memorable characters and a plot that twists and turns, it promises to captivate readers from start to finish. 
                  Whether you're a fan of thrilling mysteries, epic fantasies, or heartfelt dramas, this book offers something for everyone, inviting you to lose yourself in its captivating story.
            </p>

            <p className="book-details">
              More details about the book such as publication date, sales etc, can be found in the genre.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookDetailsModal;
