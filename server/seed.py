from faker import Faker
from config import db, app
from models import User, Book, Author, Genre, Library

fake = Faker()

def seed():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Seed Users
        try:
            users = []
            for _ in range(10):
                user = User(
                    username=f"user{_}",
                    email=f"user{_}@example.com",
                    password_hash="password"
                )
                users.append(user)
                db.session.add(user)
            db.session.commit()  # Commit after adding users
            print("Users seeded successfully.")
        except Exception as e:
            print(f"Error seeding users: {e}")

        # Custom authors with biographies
        try:
            custom_authors = [
                {
                    "name": "J.K. Rowling",
                    "contact": "123-456-7890",
                    "image_url": "https://hips.hearstapps.com/hmg-prod/images/gettyimages-1061157246.jpg",
                    "biography": "J.K. Rowling is a British author, best known for writing the Harry Potter series."
                },
                {
                    "name": "George R.R. Martin",
                    "contact": "098-765-4321",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Portrait_photoshoot_at_Worldcon_75%2C_Helsinki%2C_before_the_Hugo_Awards_%E2%80%93_George_R._R._Martin.jpg/1200px-Portrait_photoshoot_at_Worldcon_75%2C_Helsinki%2C_before_the_Hugo_Awards_%E2%80%93_George_R._R._Martin.jpg",
                    "biography": "George R.R. Martin is an American novelist and short story writer, known for his series 'A Song of Ice and Fire'."
                },
                {
                    "name": "Colleen Hoover",
                    "contact": "456-789-0123",
                    "image_url": "https://pyxis.nymag.com/v1/imgs/367/e84/c467f83008dec699caafbc88ee61945c89-colleen-hoover.1x.rsquare.w1400.jpg",
                    "biography": "Colleen Hoover is an American author known for her contemporary romance novels."
                },
                {
                    "name": "J.R.R. Tolkien",
                    "contact": "456-789-0123",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRk1ZoZBuBEpqeSWK7TzHDZlTikHdwWtNaJcA&s",
                    "biography": "J.R.R. Tolkien was an English writer and philologist, famous for 'The Hobbit' and 'The Lord of the Rings'."
                },
                {
                    "name": "Agatha Christie",
                    "contact": "321-654-0987",
                    "image_url": "https://oldtowncrier.com/wp-content/uploads/2020/09/last-word-agatha-christie.jpg",
                    "biography": "Agatha Christie was an English writer known for her 66 detective novels and 14 short story collections."
                },
                {
                    "name": "Stephen King",
                    "contact": "654-321-9870",
                    "image_url": "https://cdn.britannica.com/20/217720-050-857D712B/American-novelist-Stephen-King-2004.jpg",
                    "biography": "Stephen King is an American author of horror, supernatural fiction, suspense, and fantasy novels."
                },
                {
                    "name": "Rupi Kaur",
                    "contact": "789-012-3456",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Rupi_Kaur_by_Baljit_Singh.jpg/640px-Rupi_Kaur_by_Baljit_Singh.jpg",
                    "biography": "Rupi Kaur is a Canadian poet, illustrator, and author known for her poetry collections."
                },
                {
                    "name": "Mark Twain",
                    "contact": "012-345-6789",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSz8g2XupaXJRkpo0bDoKqDTDfHIEKhxO9vJw&s",
                    "biography": "Mark Twain was an American writer, humorist, and lecturer, known for 'The Adventures of Tom Sawyer' and 'Adventures of Huckleberry Finn'."
                },
                {
                    "name": "Ernest Hemingway",
                    "contact": "987-654-3210",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxkEIOE4TBldZEnaMpBLrgYdfxUd8OdODSMw&s",
                    "biography": "Ernest Hemingway was an American novelist and short story writer, noted for his terse prose style."
                },
                {
                    "name": "F. Scott Fitzgerald",
                    "contact": "567-890-1234",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFottH9Y4vpQ1YfwtWbyqkQRX-4ISMhQw6xA&s",
                    "biography": "F. Scott Fitzgerald was an American novelist and short story writer, best known for 'The Great Gatsby'."
                },
                {
                    "name": "Charles Dickens",
                    "contact": "234-567-8901",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtio4DVSb7DrhqI-w0nGLgRL9vQF08vSWWIw&s",
                    "biography": "Charles Dickens was an English writer and social critic, known for his novels including 'A Tale of Two Cities' and 'Great Expectations'."
                },
                {
                    "name": "Virginia Woolf",
                    "contact": "789-012-3456",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCSyAbSacGNXsuWM4SmPCkoCfH_zvLaS-DMw&s",
                    "biography": "Virginia Woolf was an English writer and modernist, known for her novels such as 'Mrs Dalloway' and 'To the Lighthouse'."
                },
                {
                    "name": "J.D. Salinger",
                    "contact": "345-678-9012",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDHSkFFew9pekDytsmnMYhjLlzy4fxmsBowQ&s",
                    "biography": "J.D. Salinger was an American writer known for his novel 'The Catcher in the Rye'."
                },
                {
                    "name": "Kurt Vonnegut",
                    "contact": "234-567-8902",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMFUY03pz25iupBbAS-8sPjmxtx1_gbZh3aw&s",
                    "biography": "Kurt Vonnegut was an American writer known for his satirical novels, including 'Slaughterhouse-Five'."
                },
                {
                    "name": "Margaret Atwood",
                    "contact": "345-678-9013",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2tvES5rVN8jQ1KiJz6eGcTcSYtEu0ubZwOw&s",
                    "biography": "Margaret Atwood is a Canadian poet, novelist, and critic known for 'The Handmaid's Tale'."
                },
                {
                    "name": "Isabel Allende",
                    "contact": "456-789-0124",
                    "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKKHLqOoWoChMh08Mrh6ypo295IMQEzyAUWA&s",
                    "biography": "Isabel Allende is a Chilean-American writer known for her novels 'The House of the Spirits' and 'Of Love and Shadows'."
                },
            ]

            authors = []
            for author_data in custom_authors:
                author = Author(
                    name=author_data["name"],
                    contact=author_data["contact"],
                    image_url=author_data["image_url"],
                    biography=author_data.get("biography", "")
                )
                authors.append(author)
                db.session.add(author)
            db.session.commit()  # Commit after adding authors
            print("Authors seeded successfully.")
        except Exception as e:
            print(f"Error seeding authors: {e}")

        # Seed Genres
        try:
            genres = [
                Genre(name="Fantasy", type="Fiction"),
                Genre(name="Mystery", type="Fiction"),
                Genre(name="Horror", type="Fiction"),
                Genre(name="Romance", type="Fiction"),
                Genre(name="Adventure", type="Fiction"),
                Genre(name="Classics", type="Fiction"),
                Genre(name="Historical", type="Fiction"),
                Genre(name="Non-Fiction", type="Non-Fiction"),
                Genre(name="Science Fiction", type="Fiction"),
                Genre(name="Biography", type="Non-Fiction")
            ]
            for genre in genres:
                db.session.add(genre)
            db.session.commit()  # Commit after adding genres
            print("Genres seeded successfully.")
        except Exception as e:
            print(f"Error seeding genres: {e}")

        # Seed Books
        try:
            books_data = [
                {"title": "Harry Potter and the Sorcerer's Stone", "content": "A young boy discovers he is a wizard and attends a magical school.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_gyoMNBA1L1gMH9O8aTDyxwCeqvrwS6i0Ng&s"},
                {"title": "A Game of Thrones", "content": "The first book in the 'A Song of Ice and Fire' series.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0L2o3Cg4zy1qQAAcR-RxAf5XjC7oNH-I3tw&s"},
                {"title": "Verity", "content": "A romantic thriller that delves into a writer's struggles.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx-MtrupHeh-IlTCld7LP3EzMzHT73txjXPA&s"},
                {"title": "The Hobbit", "content": "A prelude to the 'Lord of the Rings' series, following Bilbo Baggins's adventures.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3n8O8R8PYybDp0DhMkM6qM0tmU6O57Hh34Q&s"},
                {"title": "Murder on the Orient Express", "content": "A detective novel by Agatha Christie featuring Hercule Poirot.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHDkC59ow9gVnP58C5kxaMOyxDETnGFs81eA&s"},
                {"title": "The Shining", "content": "A horror novel by Stephen King set in a haunted hotel.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8Orz9ZXjxD-s6tH3cABVV5klzRHJ1btAMog&s"},
                {"title": "Milk and Honey", "content": "A collection of poetry and prose by Rupi Kaur.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm1LwSEmIq8pE4yyg9LYAqYXZ0JkKjDCuZiw&s"},
                {"title": "The Adventures of Tom Sawyer", "content": "A classic novel by Mark Twain following the adventures of a young boy.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1-0kZ7fG1rIg9erDhnU9JSHBZxiSwgLWS_w&s"},
                {"title": "The Old Man and the Sea", "content": "A novella by Ernest Hemingway about an aging fisherman's struggle.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS43Gfwtovbn5tkIGJIkOye-K3s_M7M_vH-dw&s"},
                {"title": "The Great Gatsby", "content": "A novel by F. Scott Fitzgerald about the Jazz Age in the 1920s.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHdZDLx4A9TI82d0ndc_iIuGbYNnJw4Fg93w&s"},
                {"title": "Great Expectations", "content": "A novel by Charles Dickens about a young orphan's growth and personal development.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1ZKojUkK7JwR5RzMNU8-VeEb71mgsXe8k_A&s"},
                {"title": "Mrs. Dalloway", "content": "A novel by Virginia Woolf focusing on a day in the life of Clarissa Dalloway.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_ViZLmnK9dXjxFlVjjU5tZMbjvw1FrIjbg&s"},
                {"title": "The Catcher in the Rye", "content": "A novel by J.D. Salinger about a teenager's experiences in New York City.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe8guD05vwe5VXq32k66trOdF1fN7-RMo7Kw&s"},
                {"title": "Slaughterhouse-Five", "content": "A novel by Kurt Vonnegut about the bombing of Dresden in World War II.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRV_cRZ5XtRAXgW70g9FNUi3gR63h_MW4rJ2Q&s"},
                {"title": "The Handmaid's Tale", "content": "A dystopian novel by Margaret Atwood about a totalitarian regime.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi_H__ZBRX37wghFFwsde_gmiF-pS4hM7D0g&s"},
                {"title": "The House of the Spirits", "content": "A novel by Isabel Allende that blends magical realism with family saga.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbsRSelMbPo4JvVggLSEkpNNnDNlo4VJDNFg&s"},
                {"title": "Beloved", "content": "A novel by Toni Morrison about the legacy of slavery.", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaELnRGHgHs4JvHOce8UsQ7v_YxEgVvt24GA&s"}
            ]

            books = []
            for book_data in books_data:
                book = Book(
                    title=book_data["title"],
                    content=book_data.get("content", ""),
                    image_url=book_data["image_url"]
                )
                books.append(book)
                db.session.add(book)
            db.session.commit()  # Commit after adding books
            print("Books seeded successfully.")
        except Exception as e:
            print(f"Error seeding books: {e}")

        # Seed Libraries
        try:
            # Make sure these lists are not empty
            genres = Genre.query.all()
            authors = Author.query.all()
            books = Book.query.all()
            users = User.query.all()

            if genres and authors and books and users:
                for _ in range(20):
                    library = Library(
                        notes="This is a note.",
                        genre_id=fake.random_element(elements=[genre.id for genre in genres]),
                        author_id=fake.random_element(elements=[author.id for author in authors]),
                        book_id=fake.random_element(elements=[book.id for book in books]),
                        user_id=fake.random_element(elements=[user.id for user in users])
                    )
                    db.session.add(library)
                db.session.commit()  # Commit after adding libraries
                print("Libraries seeded successfully.")
            else:
                print("Error: One or more lists are empty.")
        except Exception as e:
            print(f"Error seeding libraries: {e}")

        print("Seeding completed!")

if __name__ == '__main__':
    seed()
