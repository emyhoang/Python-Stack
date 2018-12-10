from flask import Flask, session, redirect, request, render_template, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsASecret'
print(__name__)         

@app.route('/')                       
def index():
  if 'gold' not in session: 
      session['gold'] = 0
      session['events'] = []
  return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
  building = request.form['building']
  if building == 'farm':
    gold_earned = random.randint(10,20)
  elif building == 'cave':
    gold_earned = random.randint(5,10)
  elif buiding == 'house':
    gold_earned = random.randint(2,5)
  elif building == 'casino':
    gold_earned = random.randint(-50,50)

  session['gold'] += gold_earned
  session['events'].append(
    { "building": building, "gold_earned": gold_earned, "time": datetime.now() }
  )
  return redirect('/')

@app.route('/start_over')
def start_over():
  session.clear()
  return redirect('/')
  
if __name__=="__main__":
  app.run(debug=True) 