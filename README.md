# ContactSearchAPI-v1.0
## - Task 1

ContactSearchAPI is using Django web framework to provide an API for the consumer to search contacts.

## INSTALLATION

Installation instructions are available for LINUX/UNIX or MacOSX only. The entire implementation was tested on the MacOSX. 

### 1. Install Python 3.5 and pip3
(https://www.python.org/downloads/) 

### 2. Working on a python virtualenv (optional)
(https://docs.python-guide.org/dev/virtualenvs/)

###	3. Download the package as a zipped folder or git clone from the github as following:-
```
$ git clone https://github.com/sarauny/ContactSearchAPI.git
```

###	4. Download necessary python packages
```
$ cd ContactSearchAPI
$ pip3 install -r requirement/base.txt
```


### 5 create data models
```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

### 6. Import data from the csv files (optional - db.sqlite3 provided)
```
$ ./manage.py import_company_from_csv csv_data/company.csv
$ ./manage.py import_contact_from_csv csv_data/contact.csv
```

## API TESTING

### 1. Starting development server at port 8000, http://127.0.0.1:8000/
```
$ ./manage.py runserver
```

### 2. Testing with specific url parameters

1. Fetch list of contacts:  
The endpoint should be able to fetch list of all contacts without applying any filters.  
Endpoint: /contacts  
eg @ (http://127.0.0.1:8000/contacts)

2) Fetch specific contact:  
This endpoint can fetch a specific contact given its id  
Endpoint: /contacts/1  
eg @ (http://127.0.0.1:8000/contacts/101)  

3) Filter contacts based on company  
The endpoint should be able to fetch contacts of a particular company  
Endpoint: /contacts?company_id=1  
eg @ (http://127.0.0.1:8000/contacts?company_id=11)

4) Filter contacts by company revenue:  
The endpoint should be able to fetch contacts based on company revenue.  
This is an inequality filter which should be applied as greater than or equal to.  
Endpoint: /contacts?revenue_gte=100000   
eg @ (http://127.0.0.1:8000/contacts?revenue_gte=5000000)

5) Filter contacts based on contact name:  
The endpoint should be able to fetch contacts based on contact name  
Endpoint: /contacts?name=John%20Doe (Fetch contacts where name='John Doe')  
eg @ (http://127.0.0.1:8000/contacts?name=Kristina%20Rodgers)


Personal opinions on questions that you may be interested.  
1. Which database engine you choose and why?
>>> I chose sqlite as the database (db) engine mainly for the convenience of early development and protoyping purpose. The sqlite db (single db file) can be transferred easily and plug-and-play conveniently through the python sqlite connector without much hasles. However, if the data is confidential, i would be more prone to use either PostgreSQL or mysql that allows granular settings of admin and users permissions for accessing the database. MongoDB is will be more useful for unstructured or document-oriented data. We are dealing with structured data in this study, hence, either sqlite, postgresql, mysql could be easier to use (eg. convenient in querying with high speed).

>>>PostgreSQL is an object-relational database management system with an emphasis on extensibility and standards compliance. PostgreSQL is ACID-compliant (lock and safe for post request activities), transactional, has updatable and materialized views, triggers, and foreign keys. It also supports functions and stored procedures. MySQL is a relational database management system. It has InnoDB that may be ACID-compliant, too. 

2. Which web framework you choose and why?
>>> I chose Django with the following reasons. http://www.mindfiresolutions.com/blog/2018/05/flask-vs-django/. Of course i world love to learn a tool or framework that works well for big and small projects.

3. Briefly describe the architecture of your application?
>>> All the querying jobs are created under an app called "search" in this project. I tried to follow the recommended Django best practice as much as possible. Of course one of the key advantages of Django framework is the granulity control of individual apps (minimum function for each app) under a project. Adding and removing an app is as easy as removing it from the list INSTALLED_APPS in the settings.py file. 