from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms import validators 
from wtforms.fields.core import IntegerField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    gender = SelectField("Child's gender", choices=[('Boy', 'Boy'), ('Girl', 'Girl'), ('neutral gender', 'neutral gender')])
    age = IntegerField("Child's age", validators=[DataRequired()])
    language_speaking = SelectMultipleField('Languages you speak', choices=[('Arabic', 'Arabic'), ('Chinese', 'Chinese'), ('Dutch', 'Dutch'), ('English', 'English'), ('French', 'French'), ('German', 'German'), ('Greek', 'Greek'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Spanish', 'Spanish'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('Other', 'Other')],validators=[DataRequired()])
    language_learning = SelectMultipleField('Languages you learn', choices=[('Arabic', 'Arabic'), ('Chinese', 'Chinese'), ('Dutch', 'Dutch'), ('English', 'English'), ('French', 'French'), ('German', 'German'), ('Greek', 'Greek'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Spanish', 'Spanish'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('Other', 'Other')],validators=[DataRequired(),])
    submit = SubmitField('Post')
