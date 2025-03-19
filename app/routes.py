from flask import render_template, flash
from . import db
from .models import CreditCardData
from .forms import RequestCreditCardForm
from . import app

import random

generated_numbers = set()

def generate_unique_number(n):
    while True:
        # Generate a random 16-digit number
        number = str(random.randint(10**(n-1), 10**n - 1))
        if number not in generated_numbers:
            generated_numbers.add(number)
            return number


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/customer', methods=['GET', 'POST'])
def customer():
    return render_template('customer.html')


@app.route('/customer/request_card', methods=['GET', 'POST'])
def request_card():
    form = RequestCreditCardForm()
    if form.validate_on_submit():
        new_card = CreditCardData(
        card_number = generate_unique_number(16),
        cardholder_name = form.cardholder_name.data,
        cardholder_address = form.cardholder_address.data,
        cardholder_dob = form.cardholder_dob.data,
        expiration_date = "03/30",
        cvv = generate_unique_number(3)
        )
        db.session.add(new_card)
        db.session.commit()
        flash('Credit card added successfully!', 'success')
        card = CreditCardData.query.filter_by(id=new_card.id)
        return render_template('view_card.html', cards=card)
    return render_template('request_card.html', form=form)