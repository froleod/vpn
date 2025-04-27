from flask import Flask, render_template, redirect, url_for, flash
from flask_mail import Mail, Message
from models import db, Subscriber
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
mail = Mail(app)

# Главная страница
from forms import SubscribeForm

@app.route('/')
def index():
    form = SubscribeForm()
    return render_template('index.html', form=form)


# Страница подписки
@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    form = SubscribeForm()
    if form.validate_on_submit():
        new_subscriber = Subscriber(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data
        )
        db.session.add(new_subscriber)
        db.session.commit()

        # Отправка письма
        msg = Message('Подписка на сервис!',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[form.email.data])
        msg.body = f"Спасибо за подписку, {form.first_name.data}!"
        mail.send(msg)

        flash('Subscription successful! Check your email!', 'success')
        return redirect(url_for('index'))

    return render_template('subscribe.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
