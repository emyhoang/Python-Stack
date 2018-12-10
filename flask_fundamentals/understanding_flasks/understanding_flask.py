from flask import Flask  
app = Flask(__name__)    
                        
print(__name__)         
@app.route('/')          
                         
                         
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def success():
  return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "hi "+name

@app.route('/repeat/<integer>/<str>')
def repeat(integer,str):
    print(integer)
    print(str)
    return f"{str}"*int(integer)


 # for a route '/users/____/____', two parameters in the url get passed as username and id

if __name__=="__main__":  
                           
    app.run(debug=True) 