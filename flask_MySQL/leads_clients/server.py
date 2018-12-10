from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('lead_gen_business')

# number_of_leads=[4,3,7,7]
@app.route('/')
def index():
  mysql = connectToMySQL('lead_gen_business')
  customer_names= mysql.query_db("SELECT first_name,last_name from clients")
  mysql = connectToMySQL('lead_gen_business')
  number_of_leads= mysql.query_db("SELECT COUNT(id) from leads")
  return render_template('index.html', customers=customer_names, leads=number_of_leads)

# customer_names=customers, number_of_leads=number_of_leads

if __name__=="__main__":
    app.run(debug=True)