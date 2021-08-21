from flask import render_template
from . import main


# Views
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post')
def post ():
    render_template('post.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')