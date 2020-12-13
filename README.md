# Weather RESTful api

A realtime weather RESTful service.  
An API with a simple web interface to tech you how to use it.  
Built with fastAPI.

# Main ideas implemented

- Async / await functionality support.
- In memory cashing "this was done mainly to avoid having to setup a server for the service to run".
- Request handling.
- Request parameters validation and error handling.
- Security process implementation.

# How to run

### Install requirements

```shell script
pyhton3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
```

### Run in terminal

```shell script
uvicorn main:api
```

### Run with Pyhton

```shell script
python3 main.py
```