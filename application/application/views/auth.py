from application import app
from application.database import *
from flask import (
    render_template, 
    redirect, 
    request, 
    session, 
    url_for
)

def is_authentificated():
    try:
        if session['logged_in'] == True:
            return True
        else: return False
    except: 
        return False

@app.route('/')
def home():
    if is_authentificated():
        return render_template('index.html')
    return render_template('mainpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if is_authentificated():
        return redirect(url_for('home'))
    if request.method == 'POST':
        # check password -> (username, logged_in -> session)
        username = request.form.get('id')
        password = request.form.get('password')
        password_valid = User.query.filter_by(username=username, password=password).first()

        if not password_valid: # password is invalid
            return render_template('login.html')
        
        session['username'] = username
        session['logged_in'] = True
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    if not is_authentificated():
        return redirect(url_for('home'))
    # logged_in -> False
    del(session['username'])
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if is_authentificated():
        return redirect(url_for('home'))
    if request.method == 'POST':
        # input from form
        username = request.form.get('id')
        password = request.form.get('password')
        email = request.form.get('email')

        # form -> DB
        newuser = User(username=username, email=email, password=password)
        db.session.add(newuser)
        try:
            db.session.commit()
        except: # check duplicate
            return render_template('signup.html')
        return redirect(url_for('login'))
    return render_template('signup.html')
