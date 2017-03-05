from flask_wtf import FlaskForm
from wtforms.fields import RadioField, SubmitField

class testForm(FlaskForm):
    answer =RadioField('First field',
                        choices=[('yes','Yes'),('no','No')])
    other = RadioField('Second field',
                        choices=[('1','Pink'),('2','Blue'),('3','Black')])
    submit = SubmitField('Submit')

