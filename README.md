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

additions:

CRUD Model: Books

URL for model: /library/

operations:

- library/ - shows the list of books, contains links to details for every book and for staff has link for the add book option
- library/<isbn>/ - shows the details for the book for the isbn or pk (primary key) given, staff have the update/edit and delete links for the book on this page
- library/<isbn>/update/ - allows editing of the book of the given isbn/pk
- library/<isbn>/delete/ - allows the deletion of the book of the given isbn/pk
- library/create/ - allows the creation of a new book

DRF 1:
- django rest framework added
- URL for API 'http://127.0.0.1:8000/api/': books/ and members/
- testing
    - python manage.py runserver
    - add data using admin or staff level user
    - check `http://127.0.0.1:8000/api/books` to see books
    - check `http://127.0.0.1:8000/api/books/<isbn>` as staff to edit books
    - check `http://127.0.0.1:8000/api/members` to see member information (should probably be staff only in the future)
    - check `http://127.0.0.1:8000/api/members/<id>` as owner to edit member info (cannot delete)

DRF 2:
- usings filters:
    - filters: needs exact name of book or author (firstname)
    - search: matches given text with either title, author (first and last name), or publisher
    - ordering: can order by titles or genres, either acsending and descending
- pagination change be changed for books by adding page_size after books/ -> `books/?page_size=<number>`
- only staff can create/edit/delete books, while users can only view. Users can edit their own member information, but cannot delete it.
- testing:
    - python manage.py runserver
    - check api/books/ as nonuser, user, and admin/staff
    - see CRUD options available for each
    - check api/members/<member_id> for non owner and owner (created when user signs up, matches sign up email)

Deployment:

- process:
    - create an IAM Role with the `AmazonEC2ContainerRegistryReadOnly` policy
    - (AWS) build an image with `docker build -t myapp .`
    - adding tag `docker tag myapp:latest <repo-AWS-URI>/<AWS-repo-name>:latest`
    - pushing the image to ECR `docker push <repo-AWS-URI>/<AWS-repo-name>:latest`
    - start a EC2 instance, set up security rules to allows you to access ssh, TCP for port 8000 from anywhere to allow web traffic and HTTP/S from anywhere
    - select the IAM in the advanced details
    - connect to the instance and install docker and docker compose
    - upload the docker-compose.yml and .env files with scp to the EC2 instance
    - modify env variables to fit the EC2 ip for allowed hosts and CSRF_TRUSTED_ORIGINS and set DEBUG to False
    - modify the docker-compose.yml image to use the ECR image and remove the migrate part of command and the mounted volume for the web service
    - run `docker compose up -d`
    - run `docker compose exec web python manage.py migrate to set up the database`
    - server should be running and viewable from https://<EC2-public-ip>:8000 (/library or /api is recommended as homepage does not display anything)
    - docker compose down to stop the server

    test server ip (down): https://18.223.110.101