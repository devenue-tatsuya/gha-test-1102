from flask import Flask
from flask import make_response, request
from flask_cors import CORS

from db.core import get_database_config

app = Flask(__name__)
CORS(app)


@app.route("/api/heroes", methods=['GET'])
def get_heroes():
    connection = get_database_config()
    cursor = connection.cursor()

    sql = "select * from heroes"
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return make_response(result)

@app.route("/api/heroes", methods=['POST'])
def create_hero():
    connection = get_database_config()
    cursor = connection.cursor()

    sql = "INSERT INTO heroes (name) VALUES (%s)"
    cursor.execute(sql, (request.json['name']['userName']))
    connection.commit()

    cursor.close()
    connection.close()

    return make_response({})