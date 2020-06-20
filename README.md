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
