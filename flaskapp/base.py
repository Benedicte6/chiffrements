import mysql.connector
from flask import Flask
app=Flask(__name__)

def connector():
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='essaie'
)
    return db

