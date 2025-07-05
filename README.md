LibraryManagementSystem:

Setup:
1. install the git repo
2. in command prompt run python -m venv venv (or create a virtual envrionment your preferred way)
3. install the dependencies in requirements.txt
4. create your .env
    - DEBUG - set True or False, depending on testing or hosting respectively
    - SECRET_KEY - generate a secret key or make your own
    - DATABASE_URL - create or find a host and edit this example with your information: 'postgres://user:password@host:port/dbname
5. If creating and using a locally hosted database, run:
    - `python manage.py makemigrations library_manager`
    - `PS>python manage.py migrate`
6. start server with: `python manage.py runserver`

Other:
  - admin privileges:
      - to create an admin use: `python manage.py createsuperuser` and fill out the username and password fields

Assignment 2 additions:
CRUD Model: Books
URL for model: /library/
operations:
library/ - shows the list of books, contains links to details for every book and for staff has link for the add book option
library/<isbn>/ - shows the details for the book for the isbn or pk (primary key) given, staff have the update/edit and delete links for the book on this page
library/<isbn>/update/ - allows editing of the book of the given isbn/pk
library/<isbn>/delete/ - allows the deletion of the book of the given isbn/pk
library/create/ - allows the creation of a new book
