-- to check table values
SELECT * FROM Books;
SELECT * FROM Authors;
SELECT * FROM Publishers;
SELECT * FROM BookAuthors;
SELECT * FROM BookPublishers;
SELECT * FROM Members;
SELECT * FROM Loans;
-- Join examples
-- --Show Books with author's name
SELECT B.title, A.first_name, A.last_name 
FROM Books B 
LEFT JOIN BookAuthors BA ON B.ISBN = BA.ISBN
LEFT JOIN Authors A ON BA.author_id = A.author_id;
-- --Show loan history of member given email (or human readable loan table if you exclude the WHERE)
SELECT M.email, B.title, L.loan_date, L.return_date 
FROM Members M LEFT JOIN Loans L ON M.member_id = L.member_id
LEFT JOIN Books B ON L.ISBN = B.ISBN 
WHERE M.email = 'tonyderado@yahoo.com';
-- --Show Books from given author
SELECT A.first_name, A.last_name, B.title
FROM Authors A LEFT JOIN BookAuthors BA ON A.author_id = BA.author_id
LEFT JOIN Books B ON BA.ISBN = B.ISBN
WHERE A.first_name = 'Harper' AND A.last_name = 'Lee';