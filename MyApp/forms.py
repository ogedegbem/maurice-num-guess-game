from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length


class HomeForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Generate a random number')

class PlayForm(FlaskForm):
    number = StringField('Number',validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Send your guess')

class ReplayForm(FlaskForm):
    number = StringField('Number',validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Guess')

class ReplayOptionForm(FlaskForm):
     submit = SubmitField('Replay')

class TryAgainForm(FlaskForm):
     submit = SubmitField('Replay')

