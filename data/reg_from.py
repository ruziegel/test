from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class RegForm(FlaskForm):
    surname = StringField('Фамилия')
    name = StringField('Имя')
    age = IntegerField('Ваш возраст')
    position = StringField('Должность')
    speciality = StringField('Специальность')
    address = StringField('Адрес')
    email = EmailField('Email', validators=[DataRequired()])
    hashed_password = PasswordField('Пароль', validators=[DataRequired()])
    about = StringField('О вас')
    submit = SubmitField('Зарегистрироваться')

