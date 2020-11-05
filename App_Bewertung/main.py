from flask import Flask
from flask import render_template
from flask import request

app = Flask("bewertung")


@app.route('/')
def start():
    ueberschrift_txt = "Willkommen auf der Bewertungs-Website"
    einleitung_txt = "Hier können Sie Ihre Bewertung für unsere Speisen abgeben"
    return render_template('start.html', app_name="Bewertung", ueberschrift=ueberschrift_txt, einleitung=einleitung_txt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
