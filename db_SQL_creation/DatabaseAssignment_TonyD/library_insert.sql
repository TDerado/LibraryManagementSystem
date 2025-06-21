INSERT INTO Books (ISBN, title, genre, publication_year, lang, qty) VALUES 
('978-0-06-093546-7', 'To Kill a Mockingbird', 'Fiction', 1960, 'eng', 5),
('978-0-54-507881-8', 'Tunnels', 'Fantasy', 2009, 'eng', 1),
('978-0-06-240985-0', 'Go Set a Watchman', 'Fiction', 2015, 'eng', 2),
('978-0-74-327356-5', 'The Great Gatsby', 'Tragedy', 2004, 'eng', 2),
('978-1-66-808933-0', 'Never Flinch', 'Horror', 2025, 'eng', 2);

INSERT INTO Authors (author_id, first_name, last_name) VALUES
(1, 'Harper', 'Lee'),
(2, 'Roderick', 'Gordon'),
(3, 'Brian', 'Williams'),
(4, 'Francis', 'Fitzgerald'),
(5, 'Stephen', 'King');

INSERT INTO Publishers (publisher_id, publisher_name) VALUES
(1, 'Harper Perennial'),
(2, 'Scholastic, Incorporated'),
(3, 'HarperCollins'),
(4, 'Heinemann'),
(5, 'Scribner');

INSERT INTO BookAuthors (ISBN, author_id) VALUES
('978-0-06-093546-7', 1),
('978-0-54-507881-8', 2),
('978-0-54-507881-8', 3),
('978-0-06-240985-0', 1),
('978-0-74-327356-5', 4),
('978-1-66-808933-0', 5);

INSERT INTO BookPublishers (ISBN, publisher_id) VALUES
('978-0-06-093546-7', 1),
('978-0-54-507881-8', 2),
('978-0-06-240985-0', 3),
('978-0-06-240985-0', 4),
('978-0-74-327356-5', 5),
('978-1-66-808933-0', 5);

INSERT INTO Members (member_id, first_name, last_name, email, password, membership_date) VALUES
(1, 'Tony', 'Derado', 'tonyderado@yahoo.com', 'SOME_HASHED_VALUE', '2020-01-01'),
(2, 'Charle', 'Antonio', 'Cantonio@gmail.com', 'TEST', '2022-03-11'),
(3, 'Hugh', 'James', 'Hjames@gmail.com', '123', '1999-01-01');

INSERT INTO Loans (loan_id, member_id, ISBN, loan_date, return_date) VALUES
(1, 1, '978-0-06-093546-7', '2021-02-02', '2021-03-02'),
(2, 1, '978-0-54-507881-8', '2021-02-02', '2021-03-02'),
(3, 2, '978-0-74-327356-5', '2024-10-12', '2021-11-12'),
(4, 3, '978-0-74-327356-5', '2025-08-13', '2021-08-13');