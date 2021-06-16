from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class CseSem5(FlaskForm):
    roll_number = StringField(label='Roll Number', validators=[DataRequired()])
    submit = SubmitField(label='Get Result')
