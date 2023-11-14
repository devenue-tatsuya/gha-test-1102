from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/heroes", methods=['GET'])
def hoge():
    return 'hoge'
