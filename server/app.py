from flask import Flask
from flask import make_response
from flask_cors import CORS

from db.core import get_database_config

app = Flask(__name__)
CORS(app)

@app.route("/api/heroes", methods=['GET'])
def get_heroes():
    cursor = get_database_config()
    sql = "select * from heroes"
    cursor.execute(sql)
    result = cursor.fetchall()

    return make_response(result)
