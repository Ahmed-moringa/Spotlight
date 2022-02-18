# Spotlight

>[Ahmed Mohamed](https://github.com/Ahmed-moringa)  
  
# Description  
This is an application that will allow a user to post a project they have created and get it reviewed by his/her peers.

## Screenshots 
###### Home page
 
[![aww.png](https://i.postimg.cc/vTgY5vVV/aww.png)](https://postimg.cc/8fGgSMwp)

## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects 
* Search for projects 
* View projects overall score
* View my profile page
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Ahmed-moringa/Spotlight.git 
```
##### Navigate into the folder 
 ```bash 
cd Spotlight
```
##### Install and activate Virtual Environment
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make Migrations  
 ```bash 
python manage.py makemigrations spotlight
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python](https://www.python.org/)  
* [Django](https://docs.djangoproject.com/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [ahmed.mohamed@student.moringaschool.com]  
  
## License 

* Copyright (c) 2022 **Ahmed Mohamed**