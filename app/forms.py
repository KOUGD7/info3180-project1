from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms import SelectField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from wtforms.widgets import TextArea


class UploadForm (FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    bedroom = StringField('No. Of Bedrooms', validators=[DataRequired()])
    bathroom = StringField('No. Of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])

    my_choices = [('House', 'House'), ('Apartment', 'Apartment')]
    types = SelectField(choices = my_choices, default = ['House'])

    description = StringField('Description', widget=TextArea(), validators=[Length(min=- 1, max=255, message=None)])

    upload = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])