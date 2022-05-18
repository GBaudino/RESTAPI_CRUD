# RESTAPI-CRUD
Simple users management REST API implement with fastAPI and sqlite relational database. 

### How to run?

In order to run the code without problems, when cloning the repo, make sure it's inside the folder and then install the dependencies (I recommend [reading](https://docs.python.org/3/tutorial/venv.html) how to create a virtual environment to isolate the dependencies of this project from your python environment) with a command in the console:

**python3 -m pip install -r requirements.txt**

After installing the dependencies, you can run the server by executing the command in the console:

**python3 -m uvicorn main:app --reload**

### How to use it?
You can use an application for API testing and management or you can use the documentation built into the fastAPI framework.

To access this we must access:
**localhost:HOSTPORT/docs**

- By default HOSTPORT = 8000, then it will suffice to enter [**localhost:8000/docs**](http://localhost:8000/docs)

From here we can see the documentation of each of the routes, their use, an example of what they should return to us and we can even test them from "Try it out"

The routes available in our REST API are / and /users. The latter includes GET, POST, PUT and DELETE methods to obtain, create, update and delete users respectively.

There are two GET methods, one consulting only /users that will return all the users loaded in the database and another consulting /users/{id} that returns the user that matches the id in question (if it exists).

Then, for PUT there is only the possibility of creating a new user from the /users route and for the UPDATE and DELETE methods there are the functionalities of updating and deleting a user from its id using /users/{id} (if it exists).

Anyway this and more is implied in the corresponding documentation, use it.