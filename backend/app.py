from flask import Flask, render_template, request, flash, redirect, url_for, session
import requests
from flask_mysqldb import MySQL
from datetime import datetime, tzinfo
import json
import config # Move to gitignore
import madgrades as mg


app = Flask(__name__)
app.secret_key = config.secret

# Config DB
app.config['MYSQL_HOST'] = 'host'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'pw'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    """ 
    """
    return "Test" 

@app.route('/course/<cName>', methods=['GET','POST'])
def coursePage(cName):
    """
    """
    return "Test"

@app.route('/professor/<pUID>', methods=['GET','POST'])
def professorPage(pUID):
    """
    """
    search = pUID # TODO
    pass


if __name__ == '__main__':
    app.run(debug=True, port = 5000)