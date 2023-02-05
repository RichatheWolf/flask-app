from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [{ "id":1, "name":"Alice", "done":False, "number":8743770912}, {"id":2, "name":"Natalie", "done":False, "number":4084882349]

@app.route("/add-data", methods=["POST"])

def add_contact():
    if not request.json:
        return jsonify({
            "status":"error"
            "message":"Please provide the data."
        }, 400)
        contact = { 'id': contacts[-1]['id'] + 1, 'name': request.json['name'], 'number': request.json.get('number', ""), 'done': False }
        contacts.append(contact)
        return jsonify({
            "status":"success",
            "message":"contact added successfully!"
        }, 200)