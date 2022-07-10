# Hi

Welcome to the project repository for handling Branches and Pulls requests.

This project is developed with the technologies of ReactJs for the FrontEnd, Django Rest Framework for the BackEnd and Postgres for the database.

# Deployment Instructions

First of all download the repository. At the end of the download it should be known that in the file located in `backgitpython/backgitpython/settings.py` an important variable is found which is the following `URL_REPOSITORY_REMOTE` this variable is for the remote repository that you want to clone for testing, it is currently pointing to `https://github.com/FlatDigital/fullstack-interview-test.git`.

To be able to deploy the project you must have installed docker and docker-compose.
To create the images it must be located in the root folder where the file is located docker-compose.yml and run the following command:
`sudo docker-compose build`

Once the creation of the images is finished you must run the following command for the lifting of the containers:
`sudo docker-compose up –d` 
or 
`sudo docker-compose up` (if you want to see the logs of the containers).

At the end of the lifting of the containers you can see the status of the same by running the following command:
`sudo docker ps`

You should visualize the execution of 3 containers one for the frontend, another for the backend and one for the database.

Before entering the web page you need to run the following command for the creation of the tables in the database this is executed every time the images of the containers are created:
`sudo docker-compose run back-gitpython python ./backgitpython/manage.py migrate`

In the console you should see some messages with the creation of the tables in the database and now if you can access the web page.

To access the website you must enter the following address:
`http://localhost:3000/`

To access the REST service of the application you must enter the following address:
`http://localhost:8000/`

And ready you will have the project fully deployed.

I hope it meets the requirements. Thank you and see you later.
