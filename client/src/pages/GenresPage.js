import React, { useState, useEffect } from 'react';
import GenreCard from '../components/GenreCard';
import './GenresPage.css';

function GenresPage() {
  const [genres, setGenres] = useState([]);

  useEffect(() => {
    // Fetch genres from backend
    fetch('/genres')
      .then(response => response.json())
      .then(data => setGenres(data))
      .catch(error => console.error('Error fetching genres:', error));
  }, []);

  return (
    <div>
      <h2>***Genres***</h2>
      {genres.map(genre => (
        <GenreCard key={genre.id} genre={genre} />
      ))}
    </div>
  );
}

export default GenresPage;