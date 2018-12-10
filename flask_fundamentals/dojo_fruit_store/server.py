from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)

fruits = ['Strawberry', 'Rasberry', 'Apple']

@app.route('/')

def index():
    return render_template('index.html', fruits=fruits)

@app.route('/checkout', methods=['POST'])
def checkout():
    form_data = request.form
    total_quantity = 0

    for fruit in fruits:
        total_quantity += int(form_data[fruit])

    return render_template('checkout.html', fruits=fruits, form_data=form_data, total_quantity=total_quantity, current_time=str(datetime.now()))


if __name__=="__main__":
    app.run(debug=True)