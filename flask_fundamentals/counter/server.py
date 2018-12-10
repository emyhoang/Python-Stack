from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 


@app.route('/')

def index():
  if 'count' in session:
    session['count'] += 1
  else:
    session['count'] = 1

  print(session['count'])
  
  return render_template('index.html', count=session['count'])

@app.route('/destroy_session')
def destroy_session():
  session.clear()
  return redirect('/')

@app.route('/plus_two')
def plus_two():
  session['count'] += 2
  return render_template('index.html', count=session['count'])

@app.route('/print_hundred')
def print_hundred():
  session['count'] = 100
  return render_template('index.html', count=session['count'])

@app.route('/magic_number', methods=["POST"])
def magic_number():
  session['count'] = request.form['number']
  return render_template('index.html', count=session['count'])


  
# @app.route('/checkout', methods=['POST'])
# def checkout():
#   form_data = request.form
#   return render_template('checkout.html', form_data=form_data)

if __name__=="__main__":
  app.run(debug=True)