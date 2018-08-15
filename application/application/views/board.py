from application import app
from application.database import *
from application.views.auth import is_authentificated
from flask import (
    render_template, 
    redirect, 
    request, 
    session, 
    url_for,
    jsonify
)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if not is_authentificated():
        return redirect(url_for('home'))
    if request.method == 'POST':
        title = request.form.get('title')
        article = request.form.get('article')
        return jsonify({ 'title' : title, 'article' : article })
    return render_template('board/write.html')
