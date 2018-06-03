from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    first_name = StringField("First name", validators=[
        DataRequired("Please enter your First name")
    ])
    last_name = StringField("Last name", validators=[
        DataRequired("Please enter your Last name")
    ])
    email = StringField("Email", validators=[
        DataRequired("Please enter email"),
        Email("Please enter correct email address")
    ])
    password = PasswordField("Password", validators=[
        DataRequired("Please enter password"),
        Length(min=6, message="Your password must be minimum 6 characters")
    ])
    submit = SubmitField("Submit")


class LoginForm(Form):
    email = StringField("Email", validators=[
        DataRequired("Please enter your email address"),
        Email("Please enter valid email")
    ])
    password = StringField("Password", validators=[
        DataRequired("Please enter your password")
    ])


class AddressForm(Form):
    address = StringField("Address", validators=[
        DataRequired("Please enter address")
    ])
    submit = SubmitField("Search")
