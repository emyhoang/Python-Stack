from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

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

    error = False 
    if len(request.form['name']) <= 0:
        flash('Uh oh did you forget your name?','error')
        error = True
    if len(request.form['comment']) <= 0: 
        flash('Uh oh, we want to hear from you! Tell us something.', 'error')
        error = True
    if len(request.form['comment']) >= 120: 
        flash('Make sure your comment is less than 120 characters!', 'error')
        error = True
    if (error):
        return redirect('/')
    else:
        return render_template('results.html', form_data=request.form)

if __name__=="__main__":
    app.run(debug=True)