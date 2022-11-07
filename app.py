from flask import Flask, render_template, request
import requests



request_url = "https://hawaiibeachsafety.com/rest/conditions.json"
response = requests.get(request_url)


app = Flask(__name__)

def find_index(select_beach: str):
    list_of_beaches: list[str] = []
    for beach in response.json():
        list_of_beaches.append(beach['beach'])
    index_of_beach: int = 0
    while index_of_beach < len(list_of_beaches):
        beach = list_of_beaches[index_of_beach]
        if beach != select_beach:
            index_of_beach += 1
        else:
            return index_of_beach

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ourmission')
def ourmission():
    return render_template("ourmission.html")

@app.route('/process')
def process():
    return render_template("process.html")

@app.route('/demo')
def demo():
    list_of_beaches: list[str] = []
    for beach in response.json():
        list_of_beaches.append(beach['beach'])
    return render_template("demo.html", list_of_beaches=list_of_beaches)

@app.route('/result', methods=['GET', 'POST'])
def result():
    select_beach = request.form.get('comp_select')
    index_of_beach: int = find_index(select_beach)
    full_dictionary_of_data = response.json()[index_of_beach]
    return render_template("result.html", data=full_dictionary_of_data)







