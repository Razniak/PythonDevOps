from flask import Flask, render_template, request
import json
import requests
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route('/pogoda', methods=["POST"])
def pogoda():
    if request.method == 'POST':
        api_key = "5d500da3ae079f0573a5c9d54860e79f"
        own_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = request.form['city']
        own_url2 = "http://api.openweathermap.org/data/2.5/forecast?q=" + city_name + "&appid=" + api_key + \
                   "&units=metric"
        complete_url = own_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
        question = requests.get(complete_url)
        question2 = requests.get(own_url2)
        response = question.json()
        response2 = question2.json()
        if response["cod"] == 200:
            data = response2["list"]
            print(data)
            tablica_z_prognozą = []
            tablica_z_prognozą2 = []
            for i in data:
                tablica_z_prognozą.append(i["main"]["temp_max"])
            i = 0
            while i <= 39:
                tablica_z_prognozą2.append(tablica_z_prognozą[i])
                print(tablica_z_prognozą2)
                i = i + 8
            dane = response["main"]
            temp = dane["temp"]
            return render_template("pogoda.html", temp=temp, tablica_z_prognozą2=tablica_z_prognozą2, city_name=city_name)
        else:
            return print("Coś poszlo nie tak ! ")


if __name__ == "__main__":
    app.run()
