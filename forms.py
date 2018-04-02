from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    contact = StringField('contact', validators=[DataRequired()])
    message = StringField(
        'message',
        validators=[DataRequired()],
        widget=TextArea())


class QuoteForm(FlaskForm):
    company = StringField('company', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    floors = IntegerField('floors', validators=[DataRequired()])
    building = SelectField(
        'building type',
        choices=[
            ('None', 'Building Type'),
            ('residential', 'Residential'),
            ('commercial', 'Commerical')],
        validators=[DataRequired()])
    message = StringField(
        'message',
        widget=TextArea())
