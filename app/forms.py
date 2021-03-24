from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from wtforms.widgets import TextArea


class UploadForm (FlaskForm):

    title = StringField('Property Title', validators=[DataRequired()])
    bedroom = IntegerField('No. Of Bedrooms', validators=[DataRequired()])
    bathroom = IntegerField('No. Of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()], places=2)

    my_choices = [('House', 'House'), ('Apartment', 'Apartment')]
    types = SelectField(choices = my_choices, default = ['House'])

    description = StringField('Description', widget=TextArea(), validators=[Length(max=255, message = "Max lenght is 255")])

    upload = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])