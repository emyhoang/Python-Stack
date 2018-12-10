from flask import Flask, render_template
app = Flask(__name__)    
                        
print(__name__)         
@app.route('/')          
                         
                         
def index():
  return render_template("index.html")

@app.route('/play')
def play():
  return render_template("play.html")

@app.route("/play/<x>")
def playx(x):
  print(x)
  return render_template("play_x_times.html", times=int(x))

@app.route("/play/<x>/<col>")
def playxtimes(x,col):
  print(x)
  print(col)
  return render_template("play_color.html", times=int(x), color = col)

if __name__=="__main__":
  app.run(debug=True) 