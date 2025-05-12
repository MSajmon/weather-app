from flask import Flask, render_template, request
import requests
import os
from datetime import datetime

app = Flask(__name__)
PORT = 5000
AUTHOR = "Szymon Marczak"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        country = request.form["country"]
        city = request.form["city"]
        api_key = os.environ.get("WEATHER_API_KEY", "YOUR_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric&lang=pl"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
        else:
            weather = {"error": "Nie udało się pobrać danych pogodowych."}

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    print(f"[INFO] Start aplikacji: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[INFO] Autor: {AUTHOR}")
    print(f"[INFO] Aplikacja nasłuchuje na porcie {PORT}")
    app.run(host="0.0.0.0", port=PORT)