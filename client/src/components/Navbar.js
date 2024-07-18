import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBook } from '@fortawesome/free-solid-svg-icons';

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
  color: 'black',
};

const hoverStyle = {
  color: 'blue',
};

function Navbar() {
  return (
    <nav style={navbarStyle}>
      <ul style={ulStyle}>
        <li style={liStyle}>
          <Link to="/" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>
            <FontAwesomeIcon icon={faBook} style={{ marginRight: '5px' }} /> Home
          </Link>
        </li>
        <li style={liStyle}>
          <Link to="/library" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>
            <FontAwesomeIcon icon={faBook} style={{ marginRight: '5px' }} /> Library
          </Link>
        </li>
        <li style={liStyle}>
          <Link to="/authors" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>
            <FontAwesomeIcon icon={faBook} style={{ marginRight: '5px' }} /> Authors
          </Link>
        </li>
        <li style={liStyle}>
          <Link to="/genres" style={linkStyle} onMouseEnter={(e) => e.target.style.color = hoverStyle.color} onMouseLeave={(e) => e.target.style.color = linkStyle.color}>
            <FontAwesomeIcon icon={faBook} style={{ marginRight: '5px' }} /> Genres
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
