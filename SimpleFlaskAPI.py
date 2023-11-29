# Basic Flask Application.
# Flask is the server that is running our API

# starting by importing our DEPENDENCIES. Using jsonify to create a json response
from flask import Flask, request, jsonify

# now to create the application
app = Flask(__name__)


# Need to create a root. Essentially an endpoint or location on our API to get some kind of data. To create root we
# define python function. Inside this function we have data the user can access when they reach this root. add a
# decorator @ to make accessible.
@app.route("/get-user/<user_id>") # Path parameter is a dynamic value that can pass the value of a url that can give access inside of our root.
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200
                                    # Jsonify very similar to a python dictionary. Using Flask we create a dictionary then jsonify that dictionary
                                    # allows flask to parse this value and return it as json data.
                                    # 200 is common http status code of success
# whenever we are accessing a route we can use something called a QUERY Parameter
# its an extra value that is included in the main path.

# Post Route
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201
                                # receive json data from user

# Whenever we are working with an API we are working with HTTP.
# There are several ROOTS we can use to and mark them with different methods
# Most common methods are GET POST PUT DELETE
# Very similar to SQL.
# GET: Requests data
# POST creates a resource
# PUT updates a resource
# DElETE deletes a resource.

# will run application using this if statement and the app.run will run our flask server
if __name__ == "__main__":
    app.run(debug=True)
