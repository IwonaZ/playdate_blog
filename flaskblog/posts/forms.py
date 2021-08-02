from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms import validators 
from wtforms.fields.core import FieldList, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    gender = StringField("Child's gender")
    age = IntegerField("Child's age", validators=[DataRequired()])
    language_speaking = SelectMultipleField('Languages we are speaking', choices=[('English', 'English'), ('German', 'German'), ('Spanish', 'Spanish'), ('Polish', 'Polish'), ('Arabic', 'Arabic'), ('Chinese', 'Chinese'), ('Dutsch', 'Dutsch'), ('French', 'French'), ('Greek', 'Greek'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('Other', 'Other')],validators=[DataRequired()])
    language_learning = SelectMultipleField('Languages we are learning', choices=[('English', 'English'), ('German', 'German'), ('Spanish', 'Spanish'), ('Polish', 'Polish'), ('Arabic', 'Arabic'), ('Chinese', 'Chinese'), ('Dutsch', 'Dutsch'), ('French', 'French'), ('Greek', 'Greek'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('Other', 'Other')],validators=[DataRequired(),])
    #language_learning = StringField('Languages we are learning', validators=[DataRequired()])
    #language_speaking = SelectMultipleField('Languages we are speaking', validators=[DataRequired()], choices = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submit = SubmitField('Post')
