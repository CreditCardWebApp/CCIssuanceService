from . import db

class CreditCardData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16), unique=True, nullable=False)
    cardholder_name = db.Column(db.String(100), nullable=False)
    cardholder_address = db.Column(db.String(255), nullable=False)
    cardholder_dob = db.Column(db.String(10), nullable=False)  # DD/MM/YYYY
    expiration_date = db.Column(db.String(5), nullable=False)  # MM/YY
    cvv = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return f'<CreditCardData {self.cardholder_name}>'