import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import GenresPage from './pages/GenresPage';
import AuthorsPage from './pages/AuthorsPage';
import BookDetailsPage from './pages/BookDetailsPage';// Corrected import path
import LibraryPage from './pages/LibraryPage';
import './index.css'; // Optional: if you have a CSS file for App component

function App() {
  return (
    <div className="App">
      <Navbar />
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/register" component={RegisterPage} />
        <Route path="/genres" component={GenresPage} />
        <Route path="/authors" component={AuthorsPage} />
        <Route path="/book/:id" component={BookDetailsPage} />
        <Route path="/library" component={LibraryPage} />
      </Switch>
    </div>
  );
}

export default App;