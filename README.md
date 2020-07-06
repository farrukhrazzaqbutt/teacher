# teacher
Teachers Directory application with following details:
1. First Name
2. Last Name
3. Profile picture
4. Email Address
5. Phone Number
6. Room Number
7. Subjects taught

The directory allow Teachers to filtered by first letter of last name or by subject.
You can click on a teach in the directory and open up the profile page. From there you
can see all details for the teacher.
An Importer allow Teachers details to be added to the system in bulk. This is secure so only logged in users can run the importer.
if an image is not present for the profile then default placeholder image is shown

# Steps to run this Project:
1. Download this Project and unzip it.
2. Activate the Virtual Environment and Upgrade pip
        •Activate the virtual environment:Scripts\activate.bat
        •Then install all the dependent modules and packages related to the project using command and make sure you are running it in 
        same path where requirement.txt file is present by- pip install -r requirement.txt.
3. We are using MYSql, so we have to change our setting.py file in project
```
	'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'database_name',
	'USER': 'user_name',
	'PASSWORD': password,
	'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
	'PORT': '3306',
	}
```
4. Do all migrations using these commands
>       Python manage.py make makemigartions
>       Python manage.py make migarte
5. now we can run our project
>      python manage.py runserver

These are the steps to run this system.
1)While  i am using Mysql so create the database with name teacher_directory.
	i am using Username root with no password for Mysql database. If your Mysql database have any password so 
	put in settings.py
2)First create a user by register with the system(input username, email and password)
3)login with this email and password.
4)i completed this task in both way
	1)bulk upload:click on bulk upload in side bar and upload csv file. it will automatically upload all teachers record 
	with email as unique.you can see all these recoeds on home page or click on home tab in side bar.
	2)we can also upload all records row wise.It will take rows from file and upload to database.if you want to see these
	records you have to click on view data(by row).
5)search:when you click on home you can see you can search each column of table as you asked in test.
i also did this search by submit the last name and subject you can check on view data(by row) page.
6)if an image is not present for the profile then you should use a default placeholder image.(on profile page
once you click on tech in tables).
7)you can click on tech to see that teacher profile and subjects.
