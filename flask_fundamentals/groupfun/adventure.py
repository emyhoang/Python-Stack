from flask import Flask, render_template
app = Flask(__name__)    
                        
print(__name__)         
@app.route('/')          
                         
                         
def index():
    return render_template("index.html")

@app.route('/choose_your_path')
def success():
  return render_template("choose_your_path.html")

@app.route('/left_scary')
def left():
  return render_template("left_scary.html")

@app.route('/right_scary')
def right():
  return render_template("right_scarier.html")

if __name__=="__main__":  
                           
    app.run(debug=True) 