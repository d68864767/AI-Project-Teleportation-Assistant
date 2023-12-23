```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this!
jwt = JWTManager(app)

users = {
    "admin": generate_password_hash("admin")  # This is just for demonstration. Never store passwords in plaintext!
}

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username in users and check_password_hash(users.get(username), password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@app.route('/api/teleport', methods=['POST'])
@jwt_required
def teleport():
    from ai_control_center import AIControlCenter

    video_path = request.json.get('video_path', None)
    destination_coordinates = request.json.get('destination_coordinates', None)

    if not video_path or not destination_coordinates:
        return jsonify({"msg": "Missing parameters"}), 400

    ai_control_center = AIControlCenter('path_to_your_model.h5')
    ai_control_center.select_object(video_path)
    ai_control_center.set_destination(destination_coordinates)
    ai_control_center.initiate_teleportation(video_path)

    return jsonify({"msg": "Teleportation initiated"}), 200

if __name__ == "__main__":
    app.run(debug=True)
```
