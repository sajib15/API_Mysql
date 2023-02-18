from flask import Flask,request,json,jsonify
from flask_mysqldb import MySQLdb
import mysql.connector
app = Flask(__name__)



@app.route('/home/<string:column_name>', methods=['GET'])
def welcome(column_name):
    cur =  mysql.connector.connect(host="localhost",user="root",database="voipdata")
    mycursor = cur.cursor()
    mycursor.execute('select '+column_name+' from margedata')
    db=mycursor.fetchall()
    rv=jsonify(db)
    with open("sample.json", "w") as outfile:
        json.dump(db, outfile)
    
    return rv



if __name__ == '__main__':
    app.run(debug=True)

