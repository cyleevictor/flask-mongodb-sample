# Build a simple web application with Flask and MongoDB

This simple web application is part of a Food Ordering System that aim at allowing customers to order food and beverage in a restaurant.

This is the backend service to provide a RESTFul API to handle the life cycle of the orders.

The application is built using Python [Flask](https://palletsprojects.com/p/flask/) and web application, and use the [MongoDB Atlas](https://palletsprojects.com/p/flask/) cloud service (Free tier) as the database.
<br/>

## Technology
- Python (3.x)
- Flask (1.1.2)
- MongoDB Atlas
- Mongoengine (0.20.0)
- PyMongo

## Setup

### Prerequisite
[Python](https://www.python.org/) (3.x), pip and virtualenv is installed in your local machine  
 
#### Install From requirements.txt
>To install all the python dependencies, run:
```
pip install -r requirements.txt
``` 
---
If you want to install the dependencies one by one, please follow the steps here:
#### Install Flask
```
pip install flask
```

#### Install Mongoengine
```
pip install mongoengine
```

#### Connect to MongoDB Atlas
Follow the guide in [Mongodb Atlas](https://docs.atlas.mongodb.com/getting-started/) website to:
- Create an Atlas Account and Cluster
- Setup Connectivity to Atlas

#### Install the Python driver for MongoDB Atlas
```
pip install pymongo[snappy,gssapi,srv,tls]
```
>Note: If you failed to install snappy successfully, please ensure the Snappy C library is installed. 
If you have brew running on your mac,
```
brew install snappy
```
Detail could be find [here](https://stackoverflow.com/questions/11416024/error-installing-python-snappy-snappy-c-h-no-such-file-or-directory)


#### Install unittest
```
pip install unittest
```  
  
  
#### Update Connection String to MongoDB
>Open app/data/conn.py. Update username and password
```
CONNECTION_STRING = "mongodb+srv://<username>:<password>@cluster0.vxluc.mongodb.net/core?retryWrites=true&w=majority"
```
<br/>

## Launching the application
```
$ python app/main.py
```

You should see something like this in your console:
```
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```


## Running the Unit test from command link
```
$python -m unittest tests/test_order.py
```