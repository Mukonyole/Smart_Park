SMARTPARK : Parking Booking System<br>
Programming Languages used in the web application<br>
Frontend : HTML5, CSS3, JavaScript.<br>
Backend : Python, Django framework.<br>
Database : SQLite3.<br>

SmartPark is a parking slot booking system designed to help users easily find and reserve parking spaces. <br>
The application allows users to search for available parking spots, view details, and book a spot in advance, all through a user-friendly interface.<br>

Table of Contents<br>
Features<br>
Technologies Used<br>
Installation<br>
Usage<br>
Database Structure<br>
Contributing<br>
Contact<br>

Features<br>
User Registration & Login: Secure user authentication and profile management.<br>
Search Functionality: Search for available parking spots by location and date.<br>
Real-Time Availability: Check the availability of parking slots in real-time.<br>
Booking System: Reserve parking spots and receive instant booking confirmation.<br>
User Dashboard: Manage bookings and view history.<br>
Admin Dashboard: Admins can manage parking spots, view all bookings, and perform other administrative tasks.<br>

Technologies Used<br>
Front-End<br>
HTML5: For structuring the web pages.<br>
CSS3: For styling the application and creating a responsive design.<br>
JavaScript: For adding interactivity and handling client-side logic.<br>

Back-End<br>
Python: Programming language used for back-end development.<br>
Django: High-level Python web framework that encourages rapid development and clean, pragmatic design.<br>
SQLite3: Lightweight database used for storing application data.<br>

Installation<br>
Prerequisites<br>
Ensure that you have the following installed on your system:<br>

Python 3.x<br>
SQLite3<br>
Git<br>
Clone the Repository<br>

Copy code<br>
git clone https://github.com/Mukonyole/smart_park.git<br>
cd smartpark<br>

Set Up the Virtual Environment<br>
Copy code<br>
python3 -m venv venv<br>
source venv/bin/activate  # On Windows: venv\Scripts\activate<br>

Install Dependencies<br>
Copy code<br>
pip install -r requirements.txt<br>

Set Up the Database<br>
1.Migrate the Database: Run the following command to create the necessary database tables:<br>
Copy code<br>
python manage.py migrate<br>
2.Create a Superuser: To access the Django admin panel, create a superuser:<br>
Copy code<br>
python manage.py createsuperuser<br>

Running the Application<br>
1.Start the Django Development Server:<br>
Copy code<br>
python manage.py runserver<br>
2.Open your web browser and navigate to http://127.0.0.1:8000 to access SmartPark.<br>

Usage<br>
User Interface<br>
Home Page: Users can search for available parking spots by entering their desired location and date.<br>
Search Results: Displays a list of available parking spots with detailed information.<br>
Booking: Users can book a selected parking spot and receive an instant booking confirmation.<br>
User Dashboard: Users can view their booking history and manage their profile.<br>
Admin Dashboard: Admins can manage parking spots, view all bookings, and perform administrative tasks.<br>

Booking a Parking Spot<br>
Register or log in to your account.<br>
Use the search bar on the home page to find available parking spots.<br>
Choose a parking spot, select your desired time and date, and proceed to book.<br>
Confirm your booking and receive a booking ID.<br>

Admin Panel<br>
The Django admin panel allows administrators to manage the application, including adding, updating, or removing parking spots and viewing all user bookings.<br>

To access the admin panel, navigate to http://127.0.0.1:8000/admin and log in with your superuser credentials.<br>

Database Structure<br>
The database consists of the following main tables:<br>

Users: Stores user information (username, email, password).<br>
ParkingSpots: Stores details about parking spots (location, price, availability).<br>
Bookings: Stores booking information (user, parking spot, date, time).<br>
Contributing<br>
Contributions are welcome! If you'd like to contribute, please follow these steps:<br>

Fork the repository.<br>
Create a new branch: git checkout -b feature-branch.<br>
Make your changes and commit them: git commit -m 'Add new feature'.<br>
Push to the branch: git push origin feature-branch.<br>
Open a pull request.<br>

Contact<br>
For any inquiries or feedback, please reach out via emukonyole@gmail.com
