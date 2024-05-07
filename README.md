# Rock Climbing Rating Web application
#### Video Demo:  <[Website demo](https://)>
#### Description:
Intro to program:
Project to build an automated webapplication software to store test results and then give a rough grading that a climber could potentially climb. To also give a climbing chat of different skills that represent climbers skills or weaknesses such as flexability.

Database Plan. rc_data
-users stores user id, email, hash, name, age, weight, test scores, climbing rating
-results_rating results.db id, user_id, test 1, test 2, test 3, test 4, timestamp
-results_wheel
-rating_levels which has unique id, score, ratings, levels (Beginer - Ellit)

Function for the Web application.
Main '/'- When logged in takes the user to the main screen where they can see their results in graphs or statments and eventually inbed youtube vids to help.
Register Function - Take user to a main screen where they can fill in out a form and when accepted adds user to db
Login - login registered users into the website
Logout - logout users clearing cookies etc
Change Details - change details for the user such as wieght, age etc.
Tests - Location to add user test results into the website that then adds to the db
Climbing Wheel function - This function of the web app will look at a climbers rating in all areas an then such as flexibilty, finger strength etc. This will be a pie wheel graph with a rating under each skill level.
History - Shows a list of history of training results that a person enters.



list planned features to include:
- [X] Start README
- [X] Get and plan out testing levels for climbing grades.
- [X] Plan db layout
- [X] Plan SQL query code for entering data into our initial data into db
- [] '/'
- [] '/register'
- [] '/login'
- [] '/logout'
- [] '/change_details'
- [] '/tests'
- [] '/climbingwheel'
- [] '/history'
- [] '/other potential features'
- [X] html code made for the following
- [] layout
- [] login
- [] register
- [] layout
- [] change password/change details
- [] history
- [] tests
- [] climbing wheel


