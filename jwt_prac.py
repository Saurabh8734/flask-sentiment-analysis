from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] =  'Saurabh'
jwt = JWTManager(app)


users  = {
    "Saurabh" : "Saurabh23"
    }

@app.route('/login', methods = ['POST'])

def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Checking user is exits and password is correct
    if username not in users[username] != password:
        return jsonify({"msg" : "Incorrect username or password"}), 401
    
    # Generating JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token = access_token)

@app.route('/protected', methods =['GET'])
@jwt_required()

def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as = current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
