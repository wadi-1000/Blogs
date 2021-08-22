from flask import render_template,request,redirect,url_for
from . import main



# Views
@main.route('/')
def index():
    '''
    View function that returns homepage
    '''
    title = 'Zuess'
    return render_template('index.html', title = title)


@main.route('/about')
def about():
    '''
    View function that returns about page
    '''
    title = 'Zuess'
    return render_template('about.html', title = title)

@main.route('/post')
def post ():
    '''
    View function that returns postt page for posting blogs
    '''
    title = 'Zuess'
    return render_template('post.html', title = title)

@main.route('/contact')
def contact():
    '''
    View function that returns contact page
    '''
    title = 'Zuess'
    return render_template('contact.html', title = title)

@main.route('/add')
def add():
    '''
    View function that returns form to add a post
    '''
    title = 'Zuess'
    return render_template('add.html', title = title)
