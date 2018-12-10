from flask import Flask, render_template
app = Flask(__name__)    
                        
print(__name__)         
@app.route('/')          
             
def index():
  return render_template("index.html")

@app.route("/<x>/<y>")

def checkerboard(x,y):
  print(x)
  print(y)
  return render_template("checker_x_times.html", rows=int(x), cols=int(y))


if __name__=="__main__":
  app.run(debug=True) 