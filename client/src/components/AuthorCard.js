import React from 'react';
import { Link } from 'react-router-dom';
// import { useEffect } from 'react';

function AuthorCard({ author }) {

  
  return (
    <div className="author-card">
      <h3>{author.name}</h3>
      <h3>{author.contact}</h3>
      {/* <Link to={`http://127.0.0.1:5555/authors/${author.id}`}>View Details</Link> */}
    
    </div>
  );
}

export default AuthorCard;