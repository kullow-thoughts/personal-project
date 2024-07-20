import React, { useState } from "react";
import "./HomePage.css";
import BookDetailsModal from "../components/BookDetailsModal";

const booksData = [
  { title: "It Ends With Us", author: "Colleen Hoover", image: "https://i0.wp.com/natashaisabookjunkie.com/wp-content/uploads/2016/03/itendswithus.jpg?fit=461%2C716&ssl=1" },
  { title: "Atomic Habits", author: "James Clear", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAk0OBDz11_JQCwqiORpIiVHxBwsffFNozOg&s" },
  { title: "Welcome To HorrorLand", author: "GooseBumps", image: "https://m.media-amazon.com/images/I/51EIuqNlXkL._AC_UF1000,1000_QL80_.jpg" },
  { title: "It Starts With Us", author: "Colleen Hoover", image: "https://textbookcentre.com/media/products/Scan_20230131_8.jpg" },
  { title: "Harry Potter And The Philosopher's Stone", author: "J.K. Rowling", image: "https://m.media-amazon.com/images/I/81q77Q39nEL._AC_UF894,1000_QL80_.jpg" },
  { title: "Becoming", author: "Michelle Obama", image: "https://images-na.ssl-images-amazon.com/images/I/81h2gWPTYJL.jpg" },
  { title: "The Great Gatsby", author: "F. Scott Fitzgerald", image: "https://images-na.ssl-images-amazon.com/images/I/81af+MCATTL.jpg" },
  { title: "This Might Get a Little Heavy", author: "Ralphie May", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCb49JkQUJLQ2VeZtgmaluOdNWnomfu-jKNg&s" },
  { title: "My First Love", author: "Ivan Turgenev", image: "https://marketplace.canva.com/EAFtMYVrRvE/1/0/1003w/canva-pink-and-black-simple-romance-book-cover-idri8kiP_ZM.jpg" },
  { title: "The Hobbit", author: "J.R.R. Tolkien", image: "https://images-na.ssl-images-amazon.com/images/I/81t2CVWEsUL.jpg" },
  { title: "Sapiens: A Brief History of Humankind", author: "Yuval Noah Harari", image: "https://images-na.ssl-images-amazon.com/images/I/713jIoMO3UL.jpg" },
  { title: "To Kill a Mockingbird", author: "Harper Lee", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe7FSXuLfWs-b5JyLrZwGsNM6fk0-ikkBV2g&s" },
  { title: "The Chronicles of Narnia", author: "C.S. Lewis", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsbXrEJ2dlo1hXGzh43Uh8mG8wKPJTDZ2hJw&s" },
  { title: "Dead Connection", author: "Alafair Burke", image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3TaSk0nCa4J0k5RFOqvscD8Iq5d_TJJQ4zg&s" },
  { title: "Wicked", author: "Gregory Maguire", image: "https://upload.wikimedia.org/wikipedia/en/7/70/WickedBookCover.jpg" },
];

function HomePage() {
    const [searchTerm, setSearchTerm] = useState("");
    const [filteredBooks, setFilteredBooks] = useState(booksData);
    const [selectedBook, setSelectedBook] = useState(null);
  
    const handleSearch = () => {
      if (searchTerm.trim() === "") {
        setFilteredBooks(booksData);
      } else {
        const results = booksData.filter((book) =>
          book.title.toLowerCase().includes(searchTerm.toLowerCase())
        );
        setFilteredBooks(results);
      }
    };
  
    const handleKeyPress = (event) => {
      if (event.key === "Enter") {
        handleSearch();
      }
    };
  
    const openBookDetails = (book) => {
      setSelectedBook(book);
    };
  
    const closeBookDetails = () => {
      setSelectedBook(null);
    };
  
    return (
      <div className="HomePage">
        <header className="header">
          <h1>Welcome to Bookhub</h1>
          <div className="search-container">
            <input
              type="text"
              placeholder="Search for books..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              onKeyPress={handleKeyPress}
              className="search-bar"
            />
            <button onClick={handleSearch} className="search-button">Search</button>
          </div>
        </header>
  
        <section className="featured-books">
          <h2>Books</h2>
          <div className="books-grid">
            {filteredBooks.map((book, index) => (
              <div key={index} className="book" onClick={() => openBookDetails(book)}>
                <img src={book.image} alt="Book Cover" />
                <h3>{book.title}</h3>
                <p>{book.author}</p>
                <button className="view-details-button" onClick={() => openBookDetails(book)}>
                  View Details
                </button>
              </div>
            ))}
          </div>
        </section>
  
        {selectedBook && <BookDetailsModal book={selectedBook} onClose={closeBookDetails} />}
      </div>
    );
  }
  
  export default HomePage;
