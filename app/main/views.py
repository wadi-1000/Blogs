from flask import render_template,request,redirect,url_for,request,flash
from . import main
from ..models import Blogpost,db,User,Comment
from datetime import datetime
from flask_login import login_required,current_user
from app.requests import get_quotes


# Views
@main.route('/')
def index():
    '''
    View function that returns homepage
    '''
    title = 'Zuess'
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    quotes = get_quotes()
    return render_template('index.html', title = title, posts = posts, quote = quotes)


@main.route('/about')
def about():
    '''
    View function that returns about page
    '''
    title = 'Zuess'
    return render_template('about.html', title = title)

@main.route('/post/<int:post_id>')
def post (post_id):
    '''
    View function that returns postt page for posting blogs
    '''
    post = Blogpost.query.filter_by(id=post_id).one()
    title = 'Zuess'

    return render_template('post.html', title = title, post=post)



@main.route('/add')
@login_required
def add():
    '''
    View function that returns form to add a post
    '''
    title = 'Zuess'
    return render_template('add.html', title = title)
@main.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()



    return redirect(url_for('main.index'))
@main.route('/post/<post_id>/delete', methods = ['POST'])
@login_required
def delete_post(post_id):
    blog = Blog.query.get(post_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))

@main.route('/comment/<post_id>', methods = ['Post','GET'])
@login_required
def comment(post_id):
    blog = Blogpost.query.get(post_id)
    comment =request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id,id=post_id)
    new_comment.save()
    return redirect(url_for('main.index',id = post_id))