# RESTAPI-CRUD
Simple users management REST API implement with fastAPI and sqlite relational database. 

## How to run?

### Without Docker version

In order to run the code without problems, when cloning the repo, make sure it's inside the folder and then install the dependencies (I recommend [reading](https://docs.python.org/3/tutorial/venv.html) how to create a virtual environment to isolate the dependencies of this project from your python environment) with a command in the console:

```bash
cd RESTAPI_CRUD/ && python3 -m pip install -r requirements.txt
```

After installing the dependencies, you can run the server by executing the command in the console:

```bash
cd backend/ && python3 -m uvicorn main:app --reload
```

### With Docker version

First make sure you have docker installed on your computer, if not you can see the [documentation to install it](https://docs.docker.com/engine/install/).

After this, we must execute the command:

```bash
cd RESTAPI_CRUD/ && docker build -t test .
```

Finally to run the app in the container exposing port 8000 we will use the command:

```bash
docker run -it --name testcontainer -p 8000:8000 test
```

## How to use it?
You can use an application for API testing and management or you can use the documentation built into the fastAPI framework.

To access this we must access:
**localhost:HOSTPORT/docs**

- By default HOSTPORT = 8000, then it will suffice to enter [**localhost:8000/docs**](http://localhost:8000/docs)

Anyway the root path '/' of the same port, will redirect us to the documentation automatically.

From here we can see the documentation of each of the routes, their use, an example of what they should return to us and we can even test them from "Try it out".

All necessary API documentation is provided in /docs, use it