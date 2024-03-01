from flask import Flask, request, jsonify 
import requests

app = Flask(__name__)

#GET REST API
@app.route('/getuser/<idmemo>', methods=["GET"])
def get_user(idmemo):
    api_url = "http://localhost:5000/getuser/v1/1"+idmemo
    response = requests.get(api_url)
    return jsonify(response.json())

# # POST REST API
# @app.route('/postuser', methods=["GET"])
# def post_user()
#     data = {"firstname": "Mickylav2", "lastname": "Reginiov2", "email": "mickylag.reginio@gmail.com"}
#     api_url = "http://localhost:5000/postuser"
#     response = requests.post(api_url, json=data)
#     return jsonify(response.json())

#POST REST APIS
@app.route('/putuser', methods=["GET"])
def put_user ():
    data = {"idmemo": "2", "firstname": "Mickyla", "lastname" : "Reginio2", "email":"mickylag.reginio@gmail.com"}
    api_url = "http://localhost/:5000/put_user"
    response = requests.post(api_url, json=data)
    return jsonify (response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
