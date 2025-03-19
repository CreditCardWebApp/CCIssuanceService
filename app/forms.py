from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from datetime import datetime
from wtforms.validators import DataRequired, Length, ValidationError

def validate_date(form, field):
    # Check if the date is in the correct format and valid
    try:
        # Attempt to parse the date
        date_value = datetime.strptime(field.data.strip(), '%d/%m/%Y')  # Strip any whitespace
        # Check if the year is before 2006
        if date_value.year >= 2006:
            raise ValidationError('Year must be before 2006.')
    except ValidationError as ve:
        raise ValidationError(ve)
    except ValueError:
        raise ValidationError('Invalid date format. Please use DD/MM/YYYY.')


class RequestCreditCardForm(FlaskForm):
    cardholder_name = StringField('Cardholder Name', validators=[DataRequired(), Length(max=100)])
    cardholder_address = StringField('Cardholder Address', validators=[DataRequired(), Length(max=255)])
    cardholder_dob =  StringField('Date of Birth (DD/MM/YYYY)', validators=[DataRequired(), validate_date])# DD/MM/YYYY
    submit = SubmitField('Request Card')