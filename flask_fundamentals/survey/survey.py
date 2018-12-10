from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    location_list = ['San Jose', 'Burbank', 'Seattle']
    language_list = ['Javascript', 'Python', 'Java']
    return render_template('index.html', locations=location_list, languages=language_list)

@app.route('/result', methods=['POST'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('results.html', form_data=request.form)

if __name__=="__main__":
    app.run(debug=True)