import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBook } from '@fortawesome/free-solid-svg-icons';
import './Navbar.css'; //create a separate CSS file

function Navbar() {
  return (
    <nav className="navbar">
      <ul className="navList">
        <li className="navItem">
          <Link to="/" className="navLink">
            <FontAwesomeIcon icon={faBook} className="navIcon" /> Home
          </Link>
        </li>
        <li className="navItem">
          <Link to="/library" className="navLink">
            <FontAwesomeIcon icon={faBook} className="navIcon" /> Library
          </Link>
        </li>
        <li className="navItem">
          <Link to="/authors" className="navLink">
            <FontAwesomeIcon icon={faBook} className="navIcon" /> Authors
          </Link>
        </li>
        <li className="navItem">
          <Link to="/genres" className="navLink">
            <FontAwesomeIcon icon={faBook} className="navIcon" /> Genres
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
