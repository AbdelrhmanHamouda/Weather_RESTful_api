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

# Available endpoints 
```shell
# Get all available reports 
> GET /api/reports
# Post a new custom report
> POST /api/reports
# Get forecast for a specific location
> GET /api/weather/

```

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

### Run the terminal utility
```shell
python3 bin/reportapp.py
```