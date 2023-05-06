from flask import Flask, redirect, render_template
from data import db_session
from data.user import User
from flask_login import LoginManager, login_user
from data.login_form import LoginForm
from data.reg_from import RegForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/blogs.db')

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            print(user.id, user.email)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('reg.html',
                                   form=form,
                                   message='Пользователь с такой почтой уже существует!')
        user = User()
        user.name = form.name.data
        user.surname = form.surname.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.email = form.email.data
        user.hashed_password = form.hashed_password.data
        user.about = form.about.data
        db_sess.add(user)
        db_sess.commit()
        db_sess.close()
        return redirect('/login')
    return render_template('reg.html', title='Регистрация', form=form)


@app.route('/')
def index():
    return render_template('index.html')


def main():
    con = db_session.create_session()
    app.run(port=8888)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == '__main__':
    main()
