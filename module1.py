#from flask_wtf import Form
from flask_wtf import FlaskForm as Form
from wtforms.fields import RadioField, SubmitField

class testForm(Form):
    answer =RadioField('First field',
                        choices=[('yes','Yes'),('no','No')])
    other = RadioField('Second field',
                        choices=[(1,'Pink'),(2,'Blue'),(3,'Black')])
    submit = SubmitField('Submit')

