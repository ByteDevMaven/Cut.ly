from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os 
from app.utils import UrlShortener
  
file_path = os.path.abspath(os.getcwd())+"/urlshortener.db"
  
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path 
db = SQLAlchemy(app) 

url_shortener = UrlShortener()
  

from app import routes 