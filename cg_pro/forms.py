from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class LineDrawing(FlaskForm):
    point1_x = IntegerField(label='Point1 X', validators=[DataRequired()])
    point1_y = IntegerField(label='Point1 Y', validators=[DataRequired()])
    point2_x = IntegerField(label='Point2 X', validators=[DataRequired()])
    point2_y = IntegerField(label='Point2 Y', validators=[DataRequired()])
    submit = SubmitField(label='Get Result')


class CircleDrawing(FlaskForm):
    radius_c = IntegerField(label='Radius Of Circle', validators=[DataRequired()])
    submit = SubmitField(label='Get Result')


class EllipseDrawing(FlaskForm):
    point_a = IntegerField(label='Length of Semi Major Axis - a/Rx', validators=[DataRequired()])
    point_b = IntegerField(label='Length of Semi Minor Axis - b/Ry', validators=[DataRequired()])
    submit = SubmitField(label='Get Result')
