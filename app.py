from flask import Flask, request, render_template
from ai import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    subjects = request.form["subjects"]
    a = returnWorkflow(subjects)
    return render_template('results.html', result=a)
app.run(debug=True)