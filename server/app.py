from flask import Flask
from flask import make_response, request
from flask_cors import CORS
import pymysql

from db.core import get_database_config

app = Flask(__name__)
CORS(app)

connection =  pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        db='hero',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.route("/api/heroes", methods=['GET'])
def get_heroes():
    with getConnection().cursor() as cursor:
        sql = "select * from heroes"
        cursor.execute(sql)
        result = cursor.fetchall()

        return make_response(result)

@app.route("/api/heroes", methods=['POST'])
def create_hero():
    connection =  pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        db='hero',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO heroes (name) VALUES (%s)"
            cursor.execute(sql, (request.json['name']['userName']))
            connection.commit()

    return make_response('hoge')

