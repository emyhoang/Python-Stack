from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  session['number'] = random.randrange(0,100)
  return render_template('index.html')

@app.route('/guess', methods=['POST'])
def result():
  if int(request.form['guess']) == session['number']:
    answer = "Spot on!"
    return render_template("index.html", answer=answer)
  elif int(request.form['guess']) < session['number']:
    answer = "Too Low, try again!"
    return render_template("index.html", answer=answer)
  else:
    answer = "Uh Oh, too High, try again"
    return render_template("index.html", answer=answer)


if __name__=="__main__":
    app.run(debug=True)