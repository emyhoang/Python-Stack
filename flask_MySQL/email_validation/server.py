from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
mysql = connectToMySQL('emaildb')

app.secret_key = 'fdshkjfgdsjkfhdk3'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/check_and_save', methods=['POST'])
def check_and_save():
  email = request.form['email']
  matched_email = re.match(r'.+@\w+\.[a-z]{2,3}', email)

  if(matched_email is None):
    # redirect to index and flash error msg
    flash('Email is not valid!')
    return redirect('/')
  else:
    mysql = connectToMySQL('emaildb')
    query= "INSERT INTO emails(email,created_at, updated_at) VALUES(%(email)s, now(), now());"
    data= {'email': email}
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def success():
  mysql = connectToMySQL('emaildb')
  emails = mysql.query_db("SELECT * from emails")
  last_email = emails[len(emails) -1]
  return render_template('success.html', emails=emails, last_email=last_email)

if __name__=="__main__":
    app.run(debug=True)