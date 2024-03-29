from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterFormdk(FlaskForm):

   def validate_username(self, username_to_check):
      user = User.query.filter_by(username=username_to_check.data).first()

      if user:
         raise ValidationError('Username already exists! Please try a different name')
   
   def validate_email_address(self, email_to_check):
      email_address = User.query.filter_by(email_address=email_to_check.data).first()

      if email_address:
         raise ValidationError('Email already exists! Please try a different name')


   username = StringField(label='Username', validators=[Length(min=2, max=20), DataRequired()])
   email_address = StringField(label='Email', validators=[Email(), DataRequired()])
   password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
   password2 = PasswordField(label='Re-enter Password', validators=[EqualTo('password1')])
   submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):
   username = StringField(label='Username :', validators=[DataRequired()])
   password = PasswordField(label='Password :', validators=[DataRequired()])
   submit = SubmitField(label='Log In')


class PurchaseItemForm(FlaskForm):
   submit = SubmitField(label='Purchase Item')

class SellItemForm(FlaskForm):
   submit = SubmitField(label='Sell Item')
