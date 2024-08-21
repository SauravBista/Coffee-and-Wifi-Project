from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
import csv


def validate_https(form, field):
    if not field.data.startswith('https://'):
        raise ValidationError('The url must be valid')



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), validate_https])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    
    coffee = SelectField(
        'Coffee Quality',
        choices=[
            ('☕', '☕'),
            ('☕☕', '☕☕'),
            ('☕☕☕', '☕☕☕'),
            ('☕☕☕☕', '☕☕☕☕')
        ],
        validators=[DataRequired()]
    )
    
    wifi = SelectField(
        'WiFi Speed',
        choices=[
            ('🚀', '🚀'),
            ('🚀🚀', '🚀🚀'),
            ('🚀🚀🚀', '🚀🚀🚀'),
            ('🚀🚀🚀🚀', '🚀🚀🚀🚀')
        ],
        validators=[DataRequired()]
    )
    
    power = SelectField(
        'Power Availability',
        choices=[
            ('🔌', '🔌'),
            ('🔌🔌', '🔌🔌'),
            ('🔌🔌🔌', '🔌🔌🔌'),
            ('🔌🔌🔌🔌', '🔌🔌🔌🔌')
        ],
        validators=[DataRequired()]
    )
    
    submit = SubmitField('Add Cafe')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Process the form data here
        cafe_data = {
            'Cafe Name': form.cafe.data,
            'Location': form.location.data,
            'Open': form.open.data,
            'Close': form.close.data,
            'Coffee': form.coffee.data,
            'Wi Fi': form.wifi.data,
            'Power': form.power.data
        }
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cafe_data.keys())
            writer.writerow(cafe_data)
        return redirect(url_for('cafes'))  # Redirect to the cafes list page
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv',  newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # Use DictReader to read rows as dictionaries
        list_of_dicts = [row for row in csv_reader]  # Convert to list of dictionaries
    
    return render_template('cafes.html', cafes=list_of_dicts)

if __name__ == '__main__':
    app.run(debug=True)
