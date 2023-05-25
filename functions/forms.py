from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional
from models.users import User
from email_validator import validate_email, EmailNotValidError

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password'), Optional()])
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        try:
            validate_email(field.data)
            user = User.query.filter_by(email=field.data).first()
            if user:
                raise ValidationError('That email is already taken. Please choose a different one.')
        except EmailNotValidError:
            raise ValidationError('Invalid email address')

class EditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    name_kana = StringField('NameKana', validators=[DataRequired()])
    phone = TelField('Phone', validators=[DataRequired()], message='無効な電話番号です')
    job_id = IntegerField('JobId', validators=[DataRequired()])
    prefecture_id = IntegerField('PrefectureId', validators=[DataRequired()])
    submit = SubmitField('Sign Up')