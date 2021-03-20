from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms import SelectField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea


class UploadForm (FlaskForm):

    """title = StringField('Title', validators=[DataRequired()])
    bedroom = StringField('No. Of Bedrooms', validators=[DataRequired()])
    bathroom = StringField('No. Of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])

    my_choices = [('1', 'House'), ('2', 'Apartment')]
    types = SelectField(choices = my_choices, default = ['1'])

    description = StringField('Description', widget=TextArea())"""

    upload = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])