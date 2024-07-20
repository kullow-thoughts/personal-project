import React, { useState, useEffect } from 'react';
import AuthorCard from '../components/AuthorCard';
import './AuthorsPage.css';  // Import your CSS file

function AuthorsPage() {
  const [authors, setAuthors] = useState([]);

  useEffect(() => {
    fetch('/authors')
      .then(response => response.json())
      .then(data => setAuthors(data))
      .catch(error => console.error('Error fetching authors:', error));
  }, []);

  return (
    <div className="authors-page">
      <h2>Authors</h2>
      <div className="author-card-container">
        {authors.map(author => (
          <AuthorCard key={author.id} author={author} />
        ))}
      </div>
    </div>
  );
}

export default AuthorsPage;
