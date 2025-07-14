# 100 Days of Code Day 89: To-Do List Application (New Year's Goal Tracking)
Day 89 called for the creation of a *to-do list website*. My spin on this project created a **goal-tracking website** for an individual user. The website has four different goal categories; however, they can be changed out to align with whatever someone wants to track.
## Modules Used
### Pandas
**Pandas** is used in this project to read the data stored in the newyearsgoals.db database file. This data is then displayed on the website's index page.
### Os & Dotenv
**Os** and **dotenv** are used to manage the Flask app key used in this project.
### Flask & Flask Bootstrap
**Flask** and **flask bootstrap** are used to render elements of the web app and the routes used in this project.
### SQL Alchemy
**SQLAlchemy** is used to interact with the newyearsgoal.db file. This includes adding entries, editing entries, and deleting entries from the file. If the file does not exist, the file is created at the start of main.py
### Flask Forms
**Flask Forms** is used to create the forms used in this project. The forms are created in a file called forms.py. The forms are then imported into main.py. Both the AddGoal and EditGoal forms contain several fields, including string fields, select fields, and submit fields. 
## Project Files
### Newyearsgoals.db 
The **newyearsgoal.db** file is the database file used in this project. It is used to track the goals added by the user. The database contains four tables: Personal, Professional, Learning, and Financial. These tables are used to categorize the types of goals added by the user. 
### Static Folder
The static folder contains the images (checkmark icon) and the CSS styling elements used on this website. 
### Templates Folder
The templates folder contains the HTML pages used to render the website. This includes the home page as well as the forms page, which renders the add/edit form. 
### Forms.py
The **forms.py** file contains the two forms created for this project. Add and edit. These forms are imported into main.py.
### Main.py
**Main.py** contains all the logic used for this project. The file can be broken into the following areas:
-	Importing modules and setting up constants
-	Database creation
-	Flask routing
## Project Walkthrough
When the website is first started, the project creates the newyearsgoals.db file if it does not already exist. If the file exists, then the database data is loaded and displayed on the website’s home page. 

After creating the database, the next part is managing the Flask routes used in the project. The following subsections provide an overview of the routes used on this website.
### Routes
#### Home Page
The home page displays the goals added by the user. Along with the goal, the goal’s progress is also displayed, along with the option to “quick complete” a goal.
#### Add a Goal
When a user clicks on Add Resolution/Goal, they are taken to the add goal page. On this page, the add form is displayed and the user can add a new goal. This page allows the user to select the following:
-	Goal category (dropdown)
-	Goal description (text) 
-	Steps to complete the goal (text)
-	Target completion date (text)
-	Status (dropdown)
#### Edit and Delete Goals
When a user clicks on a goal to edit it, the page goal.html template file is used to display the **EditForm form**.  Data for the selected goal is pulled from the database file for the user to edit. Those changes are then updated on the selected goal and reflected on the website’s home page.
#### “Quick Completing” Goals
When a user clicks the “**quick complete**” option next to a goal. The goal’s status is changed to complete and the home page is reloaded.
## Project Screenshots
Screenshots for this project can be found under the [screenshots folder](100DaysofCode-New-Years-Goals/screenshots). The screenshots added include pictures of the home page as well as the add/edit page. 
### Areas for Improvement
 This project hits all the checkmarks for what I wanted to achieve, but there are areas for improvement, including the following (from *revisionideas.txt*):
1. Add error checking to check if the goal already exists and warn the user.
2. Add a login screen and options to allow multiple users with unique goals.
3. Revise the code so that it is not over 400 lines long. Without spacing and notes could probably shave off 50+ lines.