#############################
# Main file running the API #
#############################

# --- Debug version problems ---
import sys
print("Python version: " + sys.version + "\n")

# --- REST API creation ---
from flask import Flask                                                         # Basic module
from flask_restful import Api, Resource, reqparse, abort                        # The flask API module, resources, arguments parser and abort method
from flask_restful import fields, marshal_with                                  # The ???, and the decorator to format our objects
from flask_sqlalchemy import SQLAlchemy                                         # SQL database management


# --- Initializing the app and the DB ---
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# --- Create the model of the database ---
class ClientModel(db.Model):
    # Define the fields
    id     = db.Column(db.Integer, primary_key=True)                            # Precise that the ID is the primary key (Unique Identifiant)
    name   = db.Column(db.String(100), nullable=False)                          # 100 is the maxt length of the String
    gender = db.Column(db.String(100), nullable=False)                          # 'nullable=False' means we always need a name
    age    = db.Column(db.Integer, nullable=False)

    # Wrapper called when trying to print such model (not mandatory), using fStrings (need Python version > 3.6)
    def __repr__(self):
        return f"Client(name = {name}, gender = {gender}, age = {age})"

#db.create_all() # Run it only once to first create the DB (otherwise it will overwrite)

# --- ARGS Parsers Creation ---
# Define the required arguments when requesting at PUT client endpoint (every information is required)
client_put_args = reqparse.RequestParser()
client_put_args.add_argument("name",   type=str, help="Name of the client is required",   required=True)
client_put_args.add_argument("gender", type=str, help="Gender of the client is required", required=True)
client_put_args.add_argument("age",    type=int, help="Age of the client is required",    required=True)
# Define the required arguments when requesting at PATCH client endpoint (Not all information is required)
client_update_args = reqparse.RequestParser()
client_update_args.add_argument("name",   type=str, help="Name of the client is required")
client_update_args.add_argument("gender", type=str, help="Gender of the client is required")
client_update_args.add_argument("age",    type=int, help="Age of the client is required")

# --- Main Resource class ---
# Client class inheriting from Flask resource class
# In this class we define 4 basic endpoints: GET, PUT, PATCH and DELETE
class Client(Resource):

    # --- Serialazing dictionnary creation ---
    # Create a dictionnary defining how to serialize the data in a json format
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'gender': fields.String,
        'age': fields.Integer
    }

    @marshal_with(resource_fields) # Precise that the return object will be formatted as resource_fields
    def get(self, client_id):
        # Return an instance of the ClientModel class (Filter all the ClientModel by id and return the first one)
        result = ClientModel.query.filter_by(id=client_id).first()
        if not result: # (does not exist)
            abort(404, message=f"Could not find client with that id: N°{client_id}.")
        return result

    @marshal_with(resource_fields)
    def put(self, client_id):
        # Check that the id does not already exist
        result = ClientModel.query.filter_by(id=client_id).first()
        if result: # (exist)
            abort(409, message=f"Client id: N°{client_id} already taken.")

        # Dictionnary with all the values passed in
        args = client_put_args.parse_args()
        # Create a model with the data
        client = ClientModel(id = client_id, name=args['name'], gender=args['gender'], age=args['age'])
        # Add it to the DB (temporarily)
        db.session.add(client)
        # Push it permanently
        db.session.commit()
        return client, 201

    @marshal_with(resource_fields)
    def patch(self, client_id): # update? (Modify an object without giving all the information)
        # Check client exists
        result = ClientModel.query.filter_by(id=client_id).first()
        if not result:
            abort(404, message=f"Client id: N°{client_id} doesn't exist, cannot update.")

        args = client_update_args.parse_args()
        if args['name']: # Check there is a name field in args (there is always one but we check it is not none)
            result.name = args['name']
        if args['gender']:
            result.gender = args['gender']
        if args['age']:
            result.age = args['age']

        # db.session.add(result) not necessary because already in the database
        db.session.commit()
        return result

    def delete(self, client_id):
        # Check client exists
        result = ClientModel.query.filter_by(id=client_id).first()
        if not result:
            abort(404, message=f"Client id: N°{client_id} doesn't exist, cannot delete.")
        # Delete his data and return NO JSON response
        ClientModel.query.filter_by(id=client_id).delete()
        db.session.commit()
        return '', 204


# --- Add the resource client/<client_id> to the api ---
api.add_resource(Client, "/client/<int:client_id>")

# --- Run the app ---
if __name__ == "__main__":
    app.run(debug=True)
