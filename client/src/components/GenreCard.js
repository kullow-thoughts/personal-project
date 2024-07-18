import React from 'react';
import { Link } from 'react-router-dom';

function GenreCard({ genre }) {
  return (
    <div className="genre-card">
      <h3>{genre.name}</h3>
      {/* <Link to={`/genre/${genre.id}`}>View Books</Link> */}
      <h3>{genre.type}</h3>
    </div>
  );
}

export default GenreCard;