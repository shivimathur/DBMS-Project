
# Parousia

An Attendance Management System

Parousia provides an Efficient Real-Time Attendance Marking Interface with facilities to add a new user, collect photos of the sudents, track attendance, view student details as well as change the passowrd of your account. It is equipped with security measures to ensure only authorized personnel can add new users or access sensitive information from the database. 
MySQL is used to create and manage a secure database to store the information of the user. 

# Getting Started

This project was coded purely in Python using the VSCode complier. In order to begin navigating the application, simply run the home.py file. This will load the home screen of the application.

To access the student portals, please login with the roll number and password of any student. These can be found in the database. 

To access the admin portal, please enter the username "admin" and password "admin".
(In order to change these settings, please enter the new username and password in line 68 in the login.py file.)

In order to create the user details table, please run the file titled "User Details Table.sql" in the MySQL workbench. 

## User Interface

In the project directory, you can run:

### Home Page:
Contains the "Record Attendance" button to mark attendance and the "LOGIN" button to visit the Login page. 
*![](https://lh4.googleusercontent.com/zmQmQFBt9Yxk5ymRoIEURWGMNfOpwgIn2f4yPORUXFvNTWyw5a9Nup8k3xD0uI3XUWetBukzsj5aFbjZ96lDw4hne2evbItDMc3tEqDqitJ_g7GUE38T-9O_aesFo3bzdGWcZKaiZx0H3mu7_gpSHw)**

### Login Page:
Contains text boxes to enter roll number/username and passoword.
Also contains a "Forgot Passoword" button to reset password if needed. 
**![](https://lh5.googleusercontent.com/Qxsea1ECs6npm_tN2lvfi-TprTnDbUWQJSZsN0YbEZ1bZq5kKKFICJPCUivneO7Cfiajd-bhkdxyp0TBMpcYTxtAy0JAu14rmUiEh1TNmfoY6VbM7PBP4hFNoerEihbog8yObPnZMUu7fKGLLgNOew)**
### Student Portal:
Contains options for students to enter their details, view their attendance record, as well as contact the helpdesk.
**![](https://lh5.googleusercontent.com/ljwL6M74jLwnZt1N18mvzifJZ5gO0J__rRQYpf6uCadGpvnKZUdFW68O6xOt2FsvlYUN6aOAFFkFs26OemK11Ub5npjqhn_yhwY4fWLMaRWmE61vELZMEDBsagwm9fygCoJoAoQBLA_eqA-zNP4aSg)**

### Admin Portal:
Contains buttons to train the machine learning model with the faces of the students, as well as to create new users.
**![](https://lh5.googleusercontent.com/SlmjFvBZ-wkJRvXDQf-JaOoDmAO2KBC6T8xz064sNDrsUcnHR7H8tYeGEWG0z78zyrZ6Bv7X4aMwGekkSWjwo_oNLhpooPlm8OtcfayBMpq1oHpkC3-fgi-UMPOwn2nJad1Qho30O6aCJQtr5hZUOQ)**

#### Details about the buttons and the features they provide have been mentioned in the PowerPoint Presentation [here](https://docs.google.com/presentation/d/1OofOVJxsYGDUSE9mAuSKVmc7j9wqD0u2PBT7uJYNjfU/edit?usp=sharing)

### Instructions to create the database

Please download the MySQL workbench in order to create the database table.
Link for download:https://www.mysql.com/products/workbench/

Once the workbench has been installed, please run the file titled "User Details Table.sql" to create a Schema and a table with the same name as in the code. 

Once created, the database should also contain the current registered users. Incase this data is not avaliable, it can be found in the "INSERT INTO" statement in the "User Details Table.sql" file.

Once this is completed, depending on the host, username, and password of the MySQL connection, these variables may have to be updated in the code files. The current values of these variables are in host="localhost",user="root",password="mysqlroot"

In case these values need to be changed, simply click on the search icon in VSCode and enter the following line : (host="localhost",user="root",password="mysqlroot",database="mydata")
You may then copy the same line in the replace bar (directly below the search bar) and change the values of these variables. 
Once that is done, simply click the "replace all" option to change the values of these variables throughout the code. 

The line numbers of these lines in the code are:

line 112 in course_details_student_page.py

line 87 in home.py

lines 73,102,125 in login.py

line 130 in new_user.py

line 80,94 in student_details_admin_page.py
