from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from datetime import datetime

from mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "It'sAOldCodeSicButItChecksOut"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('tripdb')

@app.route('/')
def index():
  return render_template('index.html')


#Register

@app.route('/register', methods=['POST'])
def register():
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  email = request.form['email']
  password = request.form['password']
  confirm_password = request.form['confirm_password']

  error = False 
  if len(first_name) < 2:
    flash('First name is too short', 'error')
    error = True

  if len(last_name) < 2:
    flash('Last name is too short', 'error')
    error = True
  
  if not first_name.isalpha():
    flash("No bots allowed")
    error = True
  if not last_name.isalpha():
    flash("No bots allowed - last_name")
    error = True

  mysql = connectToMySQL('tripdb')
  data = {'email': email}
  query = 'SELECT * from users WHERE email = %(email)s'
  email_existed = mysql.query_db(query, data)

  if len(email) < 0:
    flash('Email cannot be blank!', 'error')
    error = True
  if not EMAIL_REGEX.match(email):
    flash("Invalid Email Address!", "error")
    error = True
  if(email_existed):
    flash('Email is existed', 'error')
    error = True
  if len(password) < 8:
    flash("Password should be 8 characters!", "error")
    error = True
  if(password == "" or confirm_password == "" or password != confirm_password):
    flash('Password and password confirmation is invalid', 'error')
    error =  True

  if(error):
    return redirect('/')
  else:
    pw_hash = bcrypt.generate_password_hash(password)
    mysql = connectToMySQL('tripdb')
    query= "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) \
            VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, now(), now());"
    data= {'first_name': first_name,
          'last_name': last_name,
          'email': email,
          'password_hash': pw_hash}
    mysql.query_db(query, data)
    flash('Successfully created a account!!!!', 'success')
    return redirect('/')

#Login 

@app.route('/login', methods=['POST'])
def login(): 
  email = request.form['email']
  mysql = connectToMySQL('tripdb')
  data = {'email': email}
  query = 'SELECT * from users WHERE email = %(email)s'
  users = mysql.query_db(query, data)
  if(len(users) != 0):
    user = users[0]
    if bcrypt.check_password_hash(user['password'], request.form['password']):
      user.pop('password')
      session['user'] = user
      return redirect('/travels')
    else:
      flash("Invalid email or password", 'error')
      return redirect("/")
  else:
    flash("You could not be logged in- Invalid email or password", 'error')
    return redirect("/")

@app.route('/travels', methods=['GET', 'POST'])
def travels():
  if 'user' not in session:
    return redirect('/')

  if request.method == 'POST':
    #validations for form: no empty entries, travel start date should be future dated, travel end date should not be before start date. 
    error = False
    if len(request.form['destination_name']) <= 0:
      flash('You forgot to enter a destination!', 'error')
      error = True
    if len(request.form['plan']) <= 0:
      flash('You forgot to enter your trip description!', 'error')
      error = True
    if len(request.form['start_date']) <= 0:
      flash('No start date specified', 'error')
      error = True
    if len(request.form['end_date']) <= 0:
      flash('No end date specified', 'error')
      error = True

    now = datetime.now()
    print("my date", now)
    start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    if start_date < now:
      flash('Trip started from the past - not possible!', 'error')
      error = True

    if (request.form['start_date']) > request.form['end_date']:
      flash('Your trip ended before it even started!', 'error')
      error = True
    

    if(error):
      return redirect('/travels/new')

    else: 
    # create a new trip in db
      mysql = connectToMySQL('tripdb')
      query = 'INSERT INTO trips (start_date, end_date, plan, user_id, created_at, updated_at, destination_name)VALUES (%(start_date)s, %(end_date)s,%(plan)s,%(user_id)s,now(),now(),%(destination_name)s);'
      data= {
        'start_date': request.form['start_date'],
        'end_date': request.form['end_date'],
        'plan': request.form['plan'],
        'user_id': session['user']['id'],
        'destination_name': request.form['destination_name']
        }
      mysql.query_db(query, data)
      return redirect('/travels')

  else:
    mysql = connectToMySQL('tripdb')
    query ='SELECT * from trips LEFT JOIN users_trips ON trips.id = users_trips.trip_id WHERE trips.user_id = %(user_id)s OR users_trips.user_id = %(user_id)s'
    data = { "user_id": session['user']['id']}
    my_trips = mysql.query_db(query, data)

    #display all other people's trips that isn't the current user logged in ].
    mysql = connectToMySQL('tripdb')
    query = 'SELECT * from trips WHERE user_id != %(user_id)s;'
    data= {
      'user_id' : session['user']['id']
    }
    other_trips = mysql.query_db(query, data)
    return render_template('travels/index.html', other_trips=other_trips, my_trips=my_trips)

@app.route('/travels/new')
def new_trip():
  return render_template('travels/new.html')

@app.route('/travels/<int:trip_id>', methods=["GET","POST"])
def show_trip(trip_id):
    if(request.method == 'POST'):
      # edit the trip
      mysql = connectToMySQL('tripdb')
      query = 'UPDATE trips SET destination_name=%(destination_name)s, plan=%(plan)s, start_date=%(start_date)s, end_date=%(end_date)s, updated_at=NOW() WHERE trips.id = %(trip_id)s;'
      data= {
        "destination_name" : request.form['destination_name'],
        "plan": request.form['plan'],
        "start_date": request.form['start_date'],
        "end_date": request.form['end_date'],
        "trip_id": trip_id
      }
      mysql.query_db(query, data)
      return redirect('/travels')

    else:
      # show all logged in trips
      mysql = connectToMySQL('tripdb')
      query ='SELECT trips.id, trips.start_date, trips.end_date, trips.plan, trips.user_id,users.id AS user_id, users.first_name, users.last_name FROM trips JOIN users ON users.id = trips.user_id WHERE trips.id = %(trip_id)s;'
      data = {
        "trip_id": trip_id
      }
      trips = mysql.query_db(query, data)

      print(trips)
      
      mysql = connectToMySQL('tripdb')
      query ='SELECT users.first_name, users.last_name from users_trips JOIN users on users.id = users_trips.user_id;'
      trip_members= mysql.query_db(query)


    return render_template('travels/show.html', trips=trips, trip_members = trip_members)

@app.route('/delete/<int:trip_id>', methods=['POST'])
def delete_trip(trip_id):

  mysql = connectToMySQL('tripdb')
  query = 'DELETE FROM trips where trips.id = %(trip_id)s'
  data = { 'trip_id': trip_id }
  mysql.query_db(query, data)
  return redirect('/travels')

@app.route('/users_trips', methods=['POST'])
def join_a_trip():

  mysql = connectToMySQL('tripdb')
  query= 'INSERT INTO users_trips( user_id, trip_id, created_at, updated_at ) VALUES ( %(user_id)s, %(trip_id)s , NOW(), NOW() ) ;'
  data = {
    "user_id" : session['user']['id'],
    "trip_id" : request.form['trip_id']
  }
  mysql.query_db(query, data)

  return redirect('/travels')

@app.route('/users_trips/<int:users_trip_id>', methods=['POST'])
def user_trip (users_trip_id): 
  if request.form['_method'] == 'DELETE': 
    mysql = connectToMySQL('tripdb')
    query = 'DELETE FROM users_trips where users_trips.id = %(users_trip_id)s'
    data = { 'users_trip_id': users_trip_id }
    mysql.query_db(query, data)
    return redirect('/travels')

@app.route("/travels/<int:trip_id>/edit")
def edit_trips(trip_id):
   mysql = connectToMySQL('tripdb')
   query ='SELECT * FROM trips WHERE trips.id = %(trip_id)s'
   data = { "trip_id": trip_id }
   trip = mysql.query_db(query, data)[0]
   return render_template('travels/edit.html', trip=trip)

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')



if __name__=="__main__":
  app.run(debug=True)