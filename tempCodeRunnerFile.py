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