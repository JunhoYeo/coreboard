from application import app
from application.database import *
from flask import (
    render_template, 
    redirect, 
    request, 
    session, 
    url_for, 
    send_from_directory
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # check password -> (username, logged_in -> session)
        username = request.form.get('id')
        password = request.form.get('password')
        print([username, password])
        password_valid = User.query.filter_by(username=username, password=password).first()
        print(password_valid)

        if not password_valid: # password is invalid
            return render_template('login.html')
        
        session['username'] = username
        session['logged_in'] = True
        print('success')
        return redirect(url_for('home'))
    try:
        if session['logged_in'] == True:
            return redirect(url_for('home'))
    except: pass
    return render_template('login.html')

@app.route('/logout')
def logout():
    # logged_in -> False
    del(session['username'])
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # input from form
        username = request.form.get('id')
        password = request.form.get('password')
        email = request.form.get('email')
        
        # form -> DB

        # Need to check duplicate

        newuser = User(username=username, email=email, password=password)
        db.session.add(newuser)
        db.session.commit()
        # print(User.query.all())
        # print([[user.username, user.password] for user in User.query.all()])
        
        return redirect(url_for('login'))
    # print(User.query.all())
    try:
        if session['logged_in'] == True:
            return redirect(url_for('home'))
    except: pass
    return render_template('signup.html')
