import React, { useState } from 'react';
import AuthorDetails from './AuthorDetails';

function AuthorCard({ author }) {
  const [showDetails, setShowDetails] = useState(false);

  const handleClick = () => {
    setShowDetails(!showDetails);
  };

  return (
    <div className="author-card">
      {/* Debugging: Check if image_url is being passed correctly */}
      <img src={author.image_url} alt={author.name} style={{ width: '100px', height: 'auto' }} />
      <h4>{author.name}</h4>
      <button onClick={handleClick}>
        {showDetails ? 'Hide Details' : 'View Details'}
      </button>
      {showDetails && <AuthorDetails authorId={author.id} />}
    </div>
  );
}

export default AuthorCard;
