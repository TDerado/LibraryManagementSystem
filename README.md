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

Orchestration:

- changes to django:
    - added HealthCheckView(APIView) with permissions AllowAny that returns a 200 when accessed
    - added the healthCheckView to urls

- setting up:
    - this setup uses minkube to locally test orchestration, to use a server make take services like EKS which will incur costs to run
    - install minikube with https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download for your OS
    - also get kubectl on https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/ make sure to use the guide for your OS
    - if you plan to use helm best to install now as well: https://helm.sh/docs/intro/install/ scroll down till your OS instructions
    - start minikube with `minikube start` or `minikube start --driver=docker` if want to use docker (be sure docker desktop is running for this)
    - create a secret file for both postgres.env and the app.env (names are not concrete and files with be deleted later)
      - the postgres file should contain `POSTGRES_PASSWORD=<put_password_here>` and be created using the command `kubectl create secret generic postgres-secret --from-env-file=postgres.env` change last part to the file name used
      - the app secrets need the SECRET_KEY, DATABASE_URL, and if using google auth also the GOOGLE_CLIENT_ID, and GOOGLE_CLIENT_SECRET. the database url should be changed to have host as postgres-service or what name is used in postgres-service.yaml example (postgres://user:pass@postgres-service:5432/dbname) then use `kubectl create secret generic app-secret --from-env-file=app.env` again with the file annme as your temporary file
      - preferrably delete temp secret files now
    - using git bash terminal connect to minkube with eval $(minikube -p minikube docker-env) and build the image using `docker build -t <image-name:tag> .` the current image name used is `library_management_system:latest` and is set in app-deployment.yaml, so if you use a different name be sure to update the yaml file as well
    - use `kubectl apply -f k8s/postgres-pvc.yaml -f k8s/postgres-deployment.yaml -f k8s/postgres-service.yaml -f k8s/app-configmap.yaml -f k8s/app-deployment.yaml -f k8s/app-service.yaml` to run all yaml files or each can be done separately
    - use kubectl get pods to see the app deployment names
    - after postgres pod is ready run the migrate command on any of the app's pods - `kubectl exec <your-app-pod-name-here> -- python manage.py migrate`
    - after the migrate is complete wait for the app pods to be ready as well
    - the service can be accessed with multiple methods:
      - `minikube service app-service --url` (the `app-service` name is set in app-service.yaml if not found check there)
      - kubectl get svc app-service (same blurb as above)
      - kubectl port-forward service/app-service 8000:80 (fallback with port forwarding)
- Helm:
    - using helm first run `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
    - then `helm repo update`
    - then install `helm install prom-stack prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --version 72.0.1` change version to latest on artifacthub for kube-prometheus-stack
    - check the new monitoring pods with `kubectl get pods -n monitoring`
    - when they are ready, use `kubectl get svc -n monitoring` to find the name of grafana and run `kubectl get secret --namespace monitoring prom-stack-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo` if grafana isnt named prom-stack-grafana change the name used in this command to match it. ps. run in the git bash terminal if you are having issues
    - port forward grafana with `kubectl port-forward --namespace monitoring svc/prom-stack-grafana 3000:80` (again if the name is different change it to match)
    - open the monitoring website with `http://localhost:3000`
    - login with username: admin and the password you got earlier

- extra:
    - scaling: use `kubectl scale deployment app-deployment --replicas=3` to change the replicas amount to a desired number (note any reset or applying the app-deployment.yaml again will revert to the amount stated in app-deployment.yaml)
    - update: yaml updates will be rolling updates, run a kubectl apply on a changed file and with `kubectl rollout status deployment/app-deployment` you can watch the pods update/terminal and create new ones.
    - roll back: `kubectl rollout undo deployment/app-deployment` (again, if you changed the name app-deployment, change it here too)
