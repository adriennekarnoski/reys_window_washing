from flask import Flask, render_template, request, redirect, url_for
from forms import ContactForm, QuoteForm
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

app.config["MAIL_SERVER"] = os.environ.get('MAIL_SERVER')
app.config["MAIL_PORT"] = os.environ.get('MAIL_PORT')
app.config["MAIL_USE_SSL"] = os.environ.get('MAIL_USE_SSL')
app.config["MAIL_USERNAME"] = os.environ.get('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate():
            return redirect(url_for('done'))
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
    quote_form = QuoteForm()
    contact_form = ContactForm()
    if request.method == 'POST':
        if contact_form.validate():
            return redirect(url_for('success'))
        elif quote_form.validate():
            return redirect(url_for('success'))
    return render_template(
        'quote.html',
        quote_form=quote_form,
        contact_form=contact_form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate():
            return redirect(url_for('success'))
    return render_template('contact.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')
