from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField("Pet Name",
                           validators=[InputRequired(message="Pet name is required.")])
    
    species = SelectField("Species",
                          choices=[("cat", "Cat"), 
                                   ("dog", "Dog"), 
                                   ("porcupine", "Porcupine")])
    
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    
    age = IntegerField("Age",
                       validators=[Optional(), NumberRange(min=0, max=30)])
    
    notes = TextAreaField("Comments",
                          validators=[Optional(), Length(min=10)])
    

class EditPetForm(FlaskForm):
    """Form for editing an existing pet"""

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    
    notes = TextAreaField("Comments",
                          validators=[Optional(), Length(min=10)])
    
    available = BooleanField("Available?")
