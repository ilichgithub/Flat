# Hi

Welcome to the project repository for handling Branches and Pulls requests.

# Deployment Instructions

To create the images it must be located in the root folder where the file is located docker-compose.yml and run the following command:
`sudo docker-compose build`

Once the creation of the images is finished you must run the following command for the lifting of the containers:
`sudo docker-compose up –d` 

Before entering the web page you need to run the following command for the creation of the tables in the database this is executed every time the images of the containers are created:
`sudo docker-compose run back-gitpython python ./backgitpython/manage.py migrate`


Note: 

1-Important in the root folder of the project the `repository` folder will be created where the cloned project will be located there.

2-In the file located in `backgitpython/backgitpython/settings.py` an important variable is found which is the following `URL_REPOSITORY_REMOTE` this variable is for the remote repository that you want to clone for testing, it is currently pointing to `https://github.com/FlatDigital/fullstack-interview-test.git`.
