# Simple-Python-API
This project demonstrates a basic Flask API that allows you to retrieve and create user data.

Project: Simple Flask API

Description:

This project demonstrates a basic Flask API that allows you to retrieve and create user data. The API provides two endpoints:

/get-user/<user_id>: Retrieves user data for a specific user ID.

/create-user: Creates a new user and returns the user data.

Prerequisites:

Python 3.x
Flask framework
Installation:

Clone or download the project repository.

Install the required dependencies:

Bash
pip install flask
Use code with caution. Learn more
Usage:

Run the following command to start the Flask server:

Bash
python main.py
Use code with caution. Learn more
The server will run on port 5000 by default. You can access the API endpoints using the following URLs:

http://localhost:5000/get-user/<user_id>
http://localhost:5000/create-user
Replace <user_id> with the desired user ID in the first URL. For the second URL, send a POST request with JSON data containing the user information.

Example Usage:

Retrieving User Data:

Make a GET request to the /get-user endpoint:

Bash
curl -X GET http://localhost:5000/get-user/1
Use code with caution. Learn more
This will return a JSON response with the user data for user ID 1.

JSON
{
  "user_id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
Use code with caution. Learn more
Creating a New User:

Make a POST request to the /create-user endpoint:

Bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane.doe@example.com"}' http://localhost:5000/create-user
Use code with caution. Learn more
This will create a new user and return the user data in JSON format.

JSON
{
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}
