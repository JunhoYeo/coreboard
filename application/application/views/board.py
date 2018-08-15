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

        # form -> DB
        newpost = Post(title=title, article=article)
        db.session.add(newpost)
        db.session.commit()
        print(Post.query.all())

        return redirect(url_for('view'))
    return render_template('board/write.html')

@app.route('/view')
def view():
    try:
        page = int(request.args.get('page'))
        if page < 1: 
            return redirect('/view?page=1') 
    except:
        page = 1
    per_page = 5
    posts = Post.query.order_by(Post.time.desc()).paginate(page, per_page, error_out=False)
    if not posts.items:
        return redirect('/view?page=1')
    return render_template('board/view.html', page=page, posts=posts)

@app.route('/article/<post_id>')
def article(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template('board/article.html', post=post)
