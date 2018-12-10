from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "It'sAOldCodeSicButItChecksOut"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('amazondb')

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
  
  mysql = connectToMySQL('amazondb')
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
    mysql = connectToMySQL('amazondb')
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
  mysql = connectToMySQL('amazondb')
  data = {'email': email}
  query = 'SELECT * from users WHERE email = %(email)s'
  users = mysql.query_db(query, data)
  if(len(users) != 0):
    user = users[0]
    if bcrypt.check_password_hash(user['password'], request.form['password']):
      user.pop('password')
      session['user'] = user
      return redirect('/books')
    else:
      flash("Invalid email or password")
      return redirect("/")
  else:
    flash("You could not be logged in")
    return redirect("/")

@app.route('/books', methods=['GET','POST'])
def books():
  if request.method == 'POST': # if it comes from the new book form
    # create a book
    mysql = connectToMySQL('amazondb')
    query = 'INSERT into books (title, author, created_at, updated_at, user_id) VALUES(%(title)s,%(author)s,NOW(),NOW(), %(user_id)s);'
    data= {'title': request.form['title'],
          'author': request.form['author'],
          'user_id': session['user']['id']
    }
    book_id = mysql.query_db(query, data)

    mysql = connectToMySQL('amazondb')
    query = 'INSERT into reviews (content, rating, created_at, updated_at, user_id, book_id) VALUES(%(content)s,%(rating)s,NOW(),NOW(), %(user_id)s, %(book_id)s);'
    data= {'content': request.form['content'],
          'rating': request.form['rating'],
          'user_id': session['user']['id'],
          'book_id': book_id
    }
    mysql.query_db(query, data)
    return redirect('/books/' + str(book_id))

  else:
  # display last three reviews with the book title
    mysql = connectToMySQL('amazondb')
    query = 'SELECT books.id AS book_id, books.title AS book_title, reviews.rating, reviews.content, reviews.created_at FROM reviews JOIN books ON books.id = reviews.book_id ORDER BY reviews.created_at DESC LIMIT 3'
    reviews = mysql.query_db(query)

    displayed_book_ids = []
    for review in reviews:
      displayed_book_ids.append(review['book_id']) 

  #display all other books with reviews
    mysql = connectToMySQL('amazondb')
    query = 'SELECT books.id as book_id, books.title, reviews.content FROM books JOIN reviews ON reviews.user_id = books.user_id WHERE book_id NOT IN %(displayed_book_ids)s;'
    data = { 'displayed_book_ids': displayed_book_ids }
    books_with_reviews = mysql.query_db(query, data)

    print('books with reviews result')
    print(books_with_reviews)

  #display reviewer's name before the review content
    mysql = connectToMySQL('amazondb')
    query = 'SELECT users.id, users.first_name AS reviewer_name FROM reviews JOIN books ON reviews.book_id = books.id JOIN users ON users.id = books.user_id LIMIT 1;'
    reviewer_names = mysql.query_db(query)[0]
    print(reviewer_names)
    return render_template('books/index.html', reviews=reviews, books_with_reviews= books_with_reviews, reviewer_names=reviewer_names)
  
@app.route('/books/new')
def new_book():
  return render_template('books/new.html')

@app.route('/books/<int:book_id>')
def show_book(book_id):
  mysql = connectToMySQL('amazondb')
  query ='SELECT books.id,title,author FROM books WHERE id = %(book_id)s;'
  data = {
    "book_id": book_id
  }
  book = mysql.query_db(query, data)[0]

  mysql = connectToMySQL('amazondb')
  query ='SELECT reviews.id, reviews.rating, reviews.content, reviews.created_at, reviews.user_id, reviews.book_id, users.first_name as reviewer_name FROM reviews JOIN users ON reviews.user_id = users.id WHERE book_id = %(book_id)s;'
  data = {
    "book_id" : book_id
  }
  reviews = mysql.query_db(query, data)
  return render_template('books/show.html', book=book,reviews=reviews)

@app.route('/reviews', methods=['POST'])
def create_review():
  mysql = connectToMySQL('amazondb')
  query = 'INSERT into reviews (content, rating, created_at, updated_at, book_id,user_id) VALUES(%(content)s,%(rating)s,NOW(),NOW(), %(book_id)s, %(user_id)s);'
  data = {
    "content" : request.form['content'],
    "rating" : request.form['rating'],
    "book_id" : request.form['book_id'],
    "user_id" : session['user']['id']
  }
  mysql.query_db(query, data)
  return redirect ('/books/'+ str(request.form['book_id']))

@app.route('/reviews/<int:review_id>', methods=['POST'])
def delete_review(review_id):
  mysql = connectToMySQL('amazondb')
  query = 'DELETE FROM reviews where reviews.id = %(review_id)s'
  data = { 'review_id': review_id }
  mysql.query_db(query, data)
  return redirect('/books/' + request.form['book_id'])

@app.route('/users/<int:user_id>')
def show_user(user_id):
  mysql = connectToMySQL('amazondb')
  query ='SELECT users.id, users.first_name, users.last_name, users.email, COUNT(reviews.id) AS total_reviews FROM users JOIN reviews ON reviews.user_id = users.id WHERE user_id = %(user_id)s;'
  data = {
    "user_id" : user_id
  }
  users=mysql.query_db(query, data)[0]

  mysql = connectToMySQL('amazondb')
  query ='SELECT books.title, reviews.id AS reviews_id, books.id AS books_id, users.id AS users_id from books Join reviews ON books.id = reviews.book_id Join users ON users.id = reviews.user_id ;'
  user_books= mysql.query_db(query)[0]

  return render_template('users/show.html', users=users, user_books=user_books)


@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')

  




if __name__=="__main__":
  app.run(debug=True)