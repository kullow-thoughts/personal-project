import React, { useEffect, useState } from 'react';
import './AuthorDetails.css'; // Import the CSS file

function AuthorDetails({ authorId }) {
  const [authorData, setAuthorData] = useState(null);

  useEffect(() => {
    if (authorId) {
      fetch(`/authors/${authorId}`)
        .then((response) => response.json())
        .then((data) => setAuthorData(data))
        .catch((error) => console.error('Error fetching author data:', error));
    }
  }, [authorId]);

  if (!authorData) return <p>Loading...</p>;

  return (
    <div className="author-details">
      <p>Name: {authorData.name}</p>
      <p>Contact: {authorData.contact}</p>
      <p>Biography: {authorData.biography}</p>
      {/* Add any additional details you want to display */}
    </div>
  );
}

export default AuthorDetails;
