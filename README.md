SMARTPARK : Parking Booking System
Programming Languages used in the web application<br>
Frontend : HTML5, CSS3, JavaScript.
Backend : Python, Django framework.
Database : SQLite3.

SmartPark is a parking slot booking system designed to help users easily find and reserve parking spaces. 
The application allows users to search for available parking spots, view details, and book a spot in advance, all through a user-friendly interface.

Table of Contents
Features
Technologies Used
Installation
Usage
Database Structure
Contributing
Contact

Features
User Registration & Login: Secure user authentication and profile management.
Search Functionality: Search for available parking spots by location and date.
Real-Time Availability: Check the availability of parking slots in real-time.
Booking System: Reserve parking spots and receive instant booking confirmation.
User Dashboard: Manage bookings and view history.
Admin Dashboard: Admins can manage parking spots, view all bookings, and perform other administrative tasks.

Technologies Used
Front-End
HTML5: For structuring the web pages.
CSS3: For styling the application and creating a responsive design.
JavaScript: For adding interactivity and handling client-side logic.

Back-End
Python: Programming language used for back-end development.
Django: High-level Python web framework that encourages rapid development and clean, pragmatic design.
SQLite3: Lightweight database used for storing application data.

Installation
Prerequisites
Ensure that you have the following installed on your system:

Python 3.x
SQLite3
Git
Clone the Repository

Copy code
git clone https://github.com/Mukonyole/smart_park.git
cd smartpark

Set Up the Virtual Environment
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies
Copy code
pip install -r requirements.txt

Set Up the Database
1.Migrate the Database: Run the following command to create the necessary database tables:
Copy code
python manage.py migrate
2.Create a Superuser: To access the Django admin panel, create a superuser:
Copy code
python manage.py createsuperuser

Running the Application
1.Start the Django Development Server:
Copy code
python manage.py runserver
2.Open your web browser and navigate to http://127.0.0.1:8000 to access SmartPark.

Usage
User Interface
Home Page: Users can search for available parking spots by entering their desired location and date.
Search Results: Displays a list of available parking spots with detailed information.
Booking: Users can book a selected parking spot and receive an instant booking confirmation.
User Dashboard: Users can view their booking history and manage their profile.
Admin Dashboard: Admins can manage parking spots, view all bookings, and perform administrative tasks.

Booking a Parking Spot
Register or log in to your account.
Use the search bar on the home page to find available parking spots.
Choose a parking spot, select your desired time and date, and proceed to book.
Confirm your booking and receive a booking ID.

Admin Panel
The Django admin panel allows administrators to manage the application, including adding, updating, or removing parking spots and viewing all user bookings.

To access the admin panel, navigate to http://127.0.0.1:8000/admin and log in with your superuser credentials.

Database Structure
The database consists of the following main tables:

Users: Stores user information (username, email, password).
ParkingSpots: Stores details about parking spots (location, price, availability).
Bookings: Stores booking information (user, parking spot, date, time).
Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make your changes and commit them: git commit -m 'Add new feature'.
Push to the branch: git push origin feature-branch.
Open a pull request.

Contact
For any inquiries or feedback, please reach out via emukonyole@gmail.com
