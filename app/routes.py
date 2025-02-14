from flask import render_template, request, redirect, url_for 
from app import app 
from app.models import Shortener 
from app import db, url_shortener

@app.route('/')   
@app.route('/home')
@app.route('/index')  
def index(): 
    urls = Shortener.query.all()
  
    return render_template('index.html', urls=urls)

@app.route('/<short>') 
def redirect_to_original(short):   
    url = Shortener.query.filter_by(short=str(short)).first() 

    if url is None:
        return render_template('error.html')

    url.visits += 1
    db.session.commit() 
  
    return render_template('redirect.html'), {"Refresh": f"3; url={url.original}"} #{"Refresh": "time, url="} sets the Refresh header of the response

@app.route('/add', methods=['POST']) 
def add(): 
    original_url = request.form['url']
    short_url = url_shortener.shorten_url(original_url)
    
    new_url = Shortener(short=short_url, original=original_url) 
    db.session.add(new_url) 
    db.session.commit() 
  
    return redirect(url_for('index'))