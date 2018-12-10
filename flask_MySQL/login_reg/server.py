from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re #import regular expression

app = Flask(__name__)
app.secret_key = "It'sAOldCodeSicButItChecksOut"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('emaildb')

# Get / - render index
# Post /register -insert into db
# Post /login -checkin against db and redirect 

@app.route('/')
def index():
  if('user' in session):
    return render_template("dashboard.html") 
  else:
   return render_template("index.html")

#   1. First Name - letters only, at least 2 characters and that it was submitted

# 2. Last Name - letters only, at least 2 characters and that it was submitted

# 3. Email - valid Email format, does not already exist in the database, and that it was submitted

# 4. Password - at least 8 characters, and that it was submitted

# 5. Password Confirmation - matches password
@app.route('/register', methods=['POST'])
def register():

  first_name = request.form['first_name']
  last_name = request.form['last_name']
  email = request.form['email']
  password = request.form['password']
  password_confirmation = request.form['confirm_password']

  error = False
  # Validation start here
  if(first_name is None or len(first_name) < 3 ):
    flash('First name is invalid', 'error')
    error = True

  if (last_name is None or len(last_name) < 3 ) :
    flash('Last name is invalid', 'error')
    error = True

  # use regular expression to check the validity of the email
  matched_email = re.match(r'.+@\w+\.[a-z]{2,3}', email)

  # query the DB to see if there is any record with the input email?
  # if there is we dont want to create a new account
  mysql = connectToMySQL('emaildb')
  query_string = 'SELECT * from users WHERE email = %(email)s'
  data = {'email': email}
  email_existed = mysql.query_db(query_string, data)

  if(email is None or matched_email is None):
     flash('Email is invalid', 'error')
     error = True
  
  if(email_existed):
     flash('Email is existed', 'error')
     error = True

  if(password == "" or password_confirmation == "" or password != password_confirmation):
    flash('Password and password confirmation is invalid, common it is 11 PM', 'error')
    error =  True

  if( len(password) < 8 ):
    flash('Password is too short damn it', 'error')
    error =  True

# Validation end

  if(error):
    return redirect('/')
  else:
    # Generate a hashed password
    pw_hash = bcrypt.generate_password_hash(password)

    # Create a new user in the DB with the information provided
    mysql = connectToMySQL('emaildb')
    query= "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) \
            VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, now(), now());"
    data= {'first_name': first_name,
          'last_name': last_name,
          'email': email,
          'password_hash': pw_hash}
    mysql.query_db(query, data)

    # Redirect with a success flash
    flash('Successfully created a account!!!!', 'success')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
  email = request.form['email']
  password = request.form['password']

# Go to the DB find records with the matching email
  mysql = connectToMySQL('emaildb')
  query_string = 'SELECT * from users WHERE email = %(email)s'
  data = {'email': email}
  result = mysql.query_db(query_string, data) # Return a list of matching user(dict)
  same_password = bcrypt.check_password_hash(result[0]['password'], password)

  if(result != [] and same_password):
    session['user'] = result[0]['email']
    return redirect('/')
  else:
    flash('Wrong email or password', 'error')
    return redirect('/')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
    
