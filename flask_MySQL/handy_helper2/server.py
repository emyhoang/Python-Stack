from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt

from mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "It'sAOldCodeSicButItChecksOut"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('handy_helperdb')

@app.route('/')
def index():
  return render_template('index.html')

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
    flash("No bots allowed", 'error')
    error = True
  if not last_name.isalpha():
    flash("No bots allowed - last_name", 'error')
    error = True

  mysql = connectToMySQL('handy_helperdb')
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
    mysql = connectToMySQL('handy_helperdb')
    query= "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) \
            VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, now(), now());"
    data= {'first_name': first_name,
          'last_name': last_name,
          'email': email,
          'password_hash': pw_hash}
    mysql.query_db(query, data)
    flash('Successfully created a account!!!!', 'success')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login(): 
  email = request.form['email']
  mysql = connectToMySQL('handy_helperdb')
  data = {'email': email}
  query = 'SELECT * from users WHERE email = %(email)s'
  users = mysql.query_db(query, data)
  if(len(users) != 0):
    user = users[0]
    if bcrypt.check_password_hash(user['password'], request.form['password']):
      user.pop('password')
      session['user'] = user
      return redirect('/dashboard')
    else:
      flash("Invalid email or password", 'error')
      return redirect("/")
  else:
    flash("You could not be logged in- Invalid email or password", 'error')
    return redirect("/")

@app.route('/dashboard', methods=['GET', 'POST'])
def quotes():
  if 'user' not in session:
    return redirect('/')
    
  if request.method == 'POST':
    #validations for form: no empty entries, entries must be at least 3 characters
    error = False
    if len(request.form['job']) <= 0:
      flash('You forgot to enter a job!', 'error')
      error = True
    if len(request.form['job']) < 3:
      flash('Your title is too short! Must be at least 3 characters long!', 'error')
      error = True
    if len(request.form['description']) <= 0:
      flash('You forgot to enter a description!', 'error')
      error = True
    if len(request.form['description']) < 3:
      flash('Your description is too short! Must be at least 3 characters long!', 'error')
      error = True
    if len(request.form['location']) <= 0:
      flash('No location specified', 'error')
      error = True
    if len(request.form['location']) < 3:
      flash('Your location is too short! Must be at least 3 characters long!', 'error')
      error = True

    if(error):
      return redirect('/jobs/new')

    else: 
    # create a new job in db
      mysql = connectToMySQL('handy_helperdb')
      query = 'INSERT INTO jobs (job, location, user_id, created_at, updated_at, description)VALUES (%(job)s, %(location)s,%(user_id)s,now(),now(),%(description)s);'
      data= {
        'job': request.form['job'],
        'location': request.form['location'],
        'user_id': session['user']['id'],
        'description': request.form['description']
        }
      mysql.query_db(query, data)
      return redirect('/dashboard')
  # display all jobs on dashboard 
  else:
    mysql = connectToMySQL('handy_helperdb')
    query ='SELECT * from jobs'
    jobs = mysql.query_db(query)

  return render_template('dashboard/index.html', jobs=jobs)

@app.route('/jobs/new')
def new_job():
  return render_template('dashboard/new.html')

@app.route("/jobs/<int:job_id>/edit")
def edit_trips(job_id):
   mysql = connectToMySQL('handy_helperdb')
   query ='SELECT * FROM jobs WHERE jobs.id = %(job_id)s'
   data = { "job_id": job_id }
   job = mysql.query_db(query, data)[0]
   return render_template('dashboard/edit.html', job= job)

@app.route('/dashboard/<int:job_id>', methods=["POST"])
def update_job(job_id):
  #validations for form: no empty entries, entries must be at least 3 characters
    error = False
    if len(request.form['job']) <= 0:
      flash('You forgot to enter a job!', 'error')
      error = True
    if len(request.form['job']) < 3:
      flash('Your title is too short! Must be at least 3 characters long!', 'error')
      error = True
    if len(request.form['description']) <= 0:
      flash('You forgot to enter a description!', 'error')
      error = True
    if len(request.form['description']) < 3:
      flash('Your description is too short! Must be at least 3 characters long!', 'error')
      error = True
    if len(request.form['location']) <= 0:
      flash('No location specified', 'error')
      error = True
    if len(request.form['location']) < 3:
      flash('Your location is too short! Must be at least 3 characters long!', 'error')
      error = True

    if(error):
      return redirect('/jobs/'+str(job_id) + '/edit')
    else:
      # edit job
      mysql = connectToMySQL('handy_helperdb')
      query = 'UPDATE jobs SET job=%(job)s, description=%(description)s, location=%(location)s, updated_at=NOW() WHERE jobs.id = %(job_id)s;'
      data= {
        "job" : request.form['job'],
        "description": request.form['description'],
        "location": request.form['location'],
        "job_id": job_id
      }
      mysql.query_db(query, data)
      return redirect('/dashboard')

@app.route('/delete/<int:job_id>', methods=['POST'])
def delete_job(job_id):

  mysql = connectToMySQL('handy_helperdb')
  query = 'DELETE FROM jobs where jobs.id = %(job_id)s'
  data = { 'job_id': job_id }
  mysql.query_db(query, data)
  return redirect('/dashboard')


@app.route('/jobs/<int:job_id>')
def show_job(job_id):
  mysql = connectToMySQL('handy_helperdb')
  query ='SELECT jobs.id, jobs.job, jobs.description, jobs.location, jobs.user_id, users.id AS user_id, users.first_name, jobs.updated_at FROM jobs JOIN users ON users.id = jobs.user_id WHERE jobs.id = %(job_id)s;'
  data = {
    "job_id": job_id
  }
  job_details = mysql.query_db(query, data)[0]
  return render_template('dashboard/show.html', job_details = job_details )




@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


if __name__=="__main__":
  app.run(debug=True)