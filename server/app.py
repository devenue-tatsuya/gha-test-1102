from flask import Flask
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

@app.route("/api/heroes", methods=['GET'])
def getHeroes():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='hero',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

    cur = db.cursor()
    sql = "select * from heroes"
    cur.execute(sql)
    result = cur.fetchall()

    return result
