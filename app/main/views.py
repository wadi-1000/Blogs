from flask import render_template,request,redirect,url_for,request,flash
from . import main
from ..models import Blogpost,db,User,Comment
from datetime import datetime
from flask_login import login_required,current_user
from app.requests import get_quotes, repeat_get_quotes
from .forms import CommentForm


# Views
@main.route('/')
def index():
    '''
    View function that returns homepage
    '''
    title = 'Zuess'
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    quote = get_quotes()
    quotes = repeat_get_quotes(1, get_quotes)
    return render_template('index.html', title = title, posts = posts, quotes = quotes)


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
    post_id = Blogpost.query.get(post_id)
    if post.user != current_user:
        abort(403)
    post.delete()
    flash("You have deleted your Blog succesfully!")
    
    return redirect(url_for('main.index'))

@main.route('/comment/<int:post_id>', methods = ['POST','GET'])
def comment(post_id):
    form = CommentForm()
    blog = Blogpost.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,post_id = post_id)
        new_comment.save_c()
        return redirect(url_for('.comment', post_id = post_id))
    return render_template('comment.html', form =form,  all_comments=all_comments)



# @main.route('/comments/<post_id>' , methods = ['Post','Get'])
# @login_required
# def comments(post_id):
#     blog = Blog.query.filter_by(id = post_id).first()
#     comment = Comment.query.filter_by(post_id = post.id).order_by(Comment.posted.desc())
#     return render_template('comment.html', blog = blog, comments = comments)