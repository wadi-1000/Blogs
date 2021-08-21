from flask import render_template
from . import main


# Views
@main.route('/')
def index():
    '''
    View function that returns homepage
    '''
    return render_template('index.html')


@main.route('/about')
def about():
    '''
    View function that returns about page
    '''
    return render_template('about.html')

@main.route('/post')
def post ():
    '''
    View function that returns postt page for posting blogs
    '''
    render_template('post.html')

@main.route('/contact')
def contact():
    '''
    View function that returns contact page
    '''
    return render_template('contact.html')