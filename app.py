from flask import Flask, render_template, request, redirect, url_for
from forms import ContactForm, QuoteForm
from flask_mail import Mail, Message
import os

mail = Mail()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')


mail.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            sender = request.form['name']
            msg = Message(
                '{} has sent you a message'.format(sender),
                sender=os.environ.get('MAIL_SENDER'),
                recipients=[os.environ.get('MAIL_USERNAME')])
            msg.body = """
            Name: {}
            Contact Information: {}


            Message: {}

            """.format(
                request.form['name'],
                request.form['contact'],
                request.form['message'])
            mail.send(msg)
            return render_template('success.html', sender=sender)
    return render_template('home.html', form=form)


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/discounts')
def discounts():
    return render_template('discounts.html')


@app.route('/quote', methods=['GET', 'POST'])
def quote():
    form = QuoteForm()
    if form.validate_on_submit():
        sender = request.form['name']
        msg = Message(
            '{} has requested a quote'.format(sender),
            sender=os.environ.get('MAIL_SENDER'),
            recipients=[os.environ.get('MAIL_USERNAME')])
        if request.form['message']:
            message = request.form['message']
        else:
            message = 'None'
        msg.body = """
        Name: {}
        Contact Information: {}

        Company Name: {}
        City: {}
        Number of Floors: {}
        Building Type: {}

        Message: {}

        """.format(
            request.form['name'],
            request.form['contact'],
            request.form['company'],
            request.form['location'],
            request.form['floors'],
            request.form['building'],
            message)
        mail.send(msg)
        return render_template('success.html', sender=sender)
    return render_template(
        'quote.html', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            sender = request.form['name']
            msg = Message(
                '{} has sent you a message'.format(sender),
                sender=os.environ.get('MAIL_SENDER'),
                recipients=[os.environ.get('MAIL_USERNAME')])
            msg.body = """
            Name: {}
            Contact Information: {}


            Message: {}

            """.format(
                request.form['name'],
                request.form['contact'],
                request.form['message'])
            mail.send(msg)
            return render_template('success.html', sender=sender)
    return render_template('contact.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')
