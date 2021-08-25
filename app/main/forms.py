from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import Required
from ..models import Comment



class CommentForm(FlaskForm):
    comment=TextAreaField('Blog comment.',validators = [Required()])
    submit = SubmitField('Submit')