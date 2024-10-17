# Elimu App
# By Rowland Wanderi
# 17/10/2024

# Project Description

The ElimuApp is designed to simplify the process of managing educational courses. It allows administrators to create and manage courses, assign instructors, and enroll students. The platform supports dynamic course structures, flexible scheduling, and real-time tracking of student progress. Built using Angular for the frontend and a REST API for the backend, this application ensures efficient and streamlined operations for educational institutions.


## Project Structure

- **Frontend:**
  - The `src` folder contains React components, context providers, and CSS styles.
  - Routing is managed using React Router.
  - User authentication is handled using JWT tokens.

- **Backend:**
  - The Flask application is structured with routes, models, and middleware.
  - SQLAlchemy is used for database models, and Flask JWT Extended manages authentication.


## Setup Instructions

1. **Clone the repository:**
 - clone this repo from github and cd into the cloned directory using vs code
    ```bash
    `git clone https://github.com/RowlandWanderi/elimuApp`
    `cd ELIMUAPP` 
    ```
    ```

2. **Install dependencies and run backend:**
- install the dependencies and packages required to run the server . in the terminal enter:

    ```bash
    `pipenv install`
    `pipenv shell`
    `cd server` 
    `flask --debug run`
    ```


3. **Run the application:**
- open a new terminal and then enter the following to install packages and start the front end:
    ```bash
     `cd client` 
    `npm install`
    `npm start`
    ```


    Access the application at `http://localhost:3000`.




## Testing
 
- To test all our deliverables just run the app and test its functionality.

# Known Bugs

-

# Technologies Used

## Frontend
- Context API for state management
- React.js
- React Router
- Bootstrap

## Backend

- Flask (Python)
- Flask SQLAlchemy for database interaction
- Flask JWT Extended for JWT authentication
    


# Contact details

- emails: rowland.wanderi@student.moringaschool.com
- phone numbers: 0718074885


# License

-MIT LICENSE Copyright (c) 2024  Rowland Wanderi