from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'get schwifty!'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def info():
    session['form_name'] = request.form['Your Name']
    session['form_location'] = request.form['Dojo Location']
    session['form_language'] = request.form['Favorite Language']
    session['form_comment'] = request.form['comment']

    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html", name = session['form_name'], location = session['form_location'], language = session['form_language'], comment = session['form_comment'])

@app.route('/refresh', methods=['POST'])
def refresh():
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
