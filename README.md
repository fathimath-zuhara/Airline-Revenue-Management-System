# Airline-Revenue-Management-System

Project Description:

The Aeroplan Revenue Management System is a Flask-based web application developed to calculate airline revenue based on passenger counts, flight distance, and aircraft type.
The system calculates base revenue per kilometer for Economy, Business, and First Class passengers and applies business conditions such as surcharge, discount, and aircraft bonus.

This project was developed as part of the Mini Project: Airplane Revenue System Assignment.

Technologies Used:

2.1 Python 3
2.2 Flask (Backend Framework)
2.3 HTML5 (Frontend Templates)
2.4 CSS3 (Styling)
2.5 Jinja2 (Template Engine)

Functional Features

3.1 Revenue Calculation

# Base Revenue = Passengers × Distance × Rate

Rates used in the system:

Economy: 5 per km
Business: 8 per km
First Class: 12 per km

3.2 Business Logic Conditions

- 10 percent surcharge if total passengers exceed 300
- 5 percent discount if distance exceeds 5000 km
- ₹100,000 bonus if aircraft is A380 and passengers exceed 250

3.3 Application Pages

Login Page
Registration Page
Revenue Input Page (Index Page)
Result Page
Logout Navigation

3.4 Input Validation

Passenger counts must be positive integers
Distance must be greater than zero
Password must contain:
Minimum 8 characters
At least one letter
At least one number
At least one special character
Both frontend and backend validation are implemented.

Project Structure

Airplane_Project/

app.py
requirements.txt
README.md
templates/

  - login.html

  - register.html

  - index.html

  - result.html
    
static/

  - style.css

# How to Run the Project

5.1 Install Python 3.x

5.2 Open Command Prompt inside the project folder

5.3 Install dependencies:

pip install -r requirements.txt

5.4 Run the application:

python app.py

5.5 Open the application in a browser:

http://127.0.0.1:5000

Default Login Credentials

Username: Admin
Password: Admin@123

Assignment Objectives Covered

7.1 Flask backend routing
7.2 HTML templates with Jinja2
7.3 CSS styling for layout and forms
7.4 Revenue calculation using conditional if-else logic
7.5 Input validation
7.6 Modular function for revenue calculation
7.7 Error handling messages
7.8 Navigation bar with logout functionality

Conclusion

This project successfully implements the Airplane Revenue System as specified in the assignment. It demonstrates understanding of Flask routing, template rendering, form handling, conditional business logic, validation, and frontend styling.

Author

Mini Project Submission – Airplane Revenue System
Developed using Flask, HTML, and CSS.
