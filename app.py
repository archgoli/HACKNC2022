from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/ourmission')
def ourmission():
    return render_template("ourmission.html")

@app.route('/process')
def process():
    return render_template("process.html")

@app.route('/demo')
def demo():
    return render_template("demo.html")