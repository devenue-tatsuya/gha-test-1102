import pymysql

def get_database_config():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        db='hero',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

    return db