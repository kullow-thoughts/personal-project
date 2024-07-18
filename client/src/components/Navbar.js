import React from 'react';
import { Link } from 'react-router-dom';

const navbarStyle = {
  backgroundColor: 'aquablue',
  padding: '20px 430px',
};

const ulStyle = {
  display: 'flex',
  listStyle: 'none',
  padding: 0,
  margin: 0,
};

const liStyle = {
  marginRight: '35px',
};

const linkStyle = {
  textDecoration: 'none',
  color: 'black',  // Aqua white color for the text
};

const hoverStyle = {
  color: 'blue',  // Color for hover state
};

function Navbar() {
  return (
    <nav style={navbarStyle}>
      <ul style={ulStyle}>
        <li style={liStyle}><Link to="/" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>Home</Link></li>
        <li style={liStyle}><Link to="/library" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>Library</Link></li>
        <li style={liStyle}><Link to="/authors" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>Authors</Link></li>
        <li style={liStyle}><Link to="/genres" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>Genres</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;