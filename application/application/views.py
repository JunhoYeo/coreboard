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

        if (not username) or (not email): # blank
            return render_template('login.html')

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([username]), User.password.in_([password]))
        password_valid = query.first()
        if not password_valid: # password is invalid
            return render_template('login.html')
        
        session['username'] = username
        session['logged_in'] = True
        return redirect(url_for('home'))
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
        Session = sessionmaker(bind=engine)
        s = Session()
        user = User(username, email, password)
        s.add(user) # 입력한 정보의 유저 추가
        s.commit()

        return redirect(url_for('login'))
    return render_template('signup.html')
