Normalization process
unnormalized:
    library management contains tables:
        -Books
            --ISBN (PK)
            --title
            --author_name/s
            --publisher_name/s
            --language
            --genre
            --publication_date
            --loan status
        -Members
            --member_id (PK)
            --first_name
            --last_name
            --email
            --password
            --membership_date
            --loaned_books
            --ISBN
            --loan_date
            --return_date

issues: 
    things like loaned_books and author_name/s and publisher_name/s may need multiple attributes,
    breaking atomicity, this complicates queriying and reading of data as it must be parsed every time.

1NF:
    each row of Books and Members contains only one author/publisher or loaned_book, splitting multiples into new rows
issues:
    mass redundancy of data in rows.
2NF:
    separate attributes to be dependent on the primary key
    create tables separate each multiple attribute (many to many relation)
library management contains tables:
        -Books
            --ISBN (PK)
            --title
            --author_id
            --publisher_id
            --language
            --genre
            --publication_date
            --loan status
        -Authors
            --author_id (PK)
            --first_name
            --last_name
        -Publishers
            --publisher_id (PK)
            --publisher_name
        -Members
            --member_id (PK)
            --first_name
            --last_name
            --email
            --password
            --membership_date
            --ISBN
            --loan_date
            --return_date
issues: redundant rows still persist in books and members

3NF:
create tables for many to many relations to fix redundancy in rows
(final design)
(ps, qty was added incase library as multiple of one book)
library management contains tables:
        -Books
            --ISBN (PK)
            --title
            --language
            --genre
            --publication_date
            --qty
        -Authors
            --author_id (PK)
            --first_name
            --last_name
        -Publishers
            --publisher_id (PK)
            --publisher_name
        -Members
            --member_id
            --first_name
            --last_name
            --email
            --password
            --membership_date
            --isbn
            --loan_date
            --return_date
        -BookAuthors
            --ISBN (PK, FK1)
            --author_id (PK, FK2)
        -BookPublishers
            --ISBN (PK, FK1)
            --publisher_id (PK, FK2)
        -loans
            --loan_id (PK)
            --member_id (FK1)
            --ISBN (FK2)
            --loan_date
            --return_date