-- Creating the DATABASE
CREATE DATABASE libraryManagerDB;

-- DROP current TABLES
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS BookPublishers;
DROP TABLE IF EXISTS BookAuthors;
DROP TABLE IF EXISTS Publishers;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Books;

-- Create Tables
CREATE TABLE Books(
	ISBN VARCHAR(17) PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	genre VARCHAR(50) NOT NULL,
	publication_year INTEGER NOT NULL,
	lang VARCHAR(3) NOT NULL,
	qty INTEGER NOT NULL
);

CREATE TABLE Authors(
	author_id INTEGER PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

CREATE TABLE Publishers(
	publisher_id INTEGER PRIMARY KEY,
	publisher_name TEXT NOT NULL
);

CREATE TABLE BookAuthors(
	ISBN VARCHAR(17) NOT NULL,
	author_id INTEGER NOT NULL,
	PRIMARY KEY (ISBN, author_id),
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN),
	FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE BookPublishers(
	ISBN VARCHAR(17) NOT NULL,
	publisher_id INTEGER NOT NULL,
	PRIMARY KEY (ISBN, publisher_id),
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN),
	FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
);

CREATE TABLE Members(
	member_id INTEGER PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	email VARCHAR(255) NOT NULL,
	password TEXT NOT NULL,
	membership_date DATE NOT NULL
);

CREATE TABLE Loans(
	loan_id INTEGER PRIMARY KEY,
	member_id INTEGER NOT NULL,
	ISBN VARCHAR(17) NOT NULL,
	loan_date DATE NOT NULL,
	return_date DATE NOT NULL,
	FOREIGN KEY (ISBN) REFERENCES Books(ISBN),
	FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- CREATE INDEXES

CREATE INDEX book_name ON Books(title);
CREATE INDEX member_email ON Members(email);
CREATE INDEX Author_name ON Authors(first_name, last_name);