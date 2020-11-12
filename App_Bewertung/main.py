from flask import Flask
from flask import render_template
from flask import request

from daten import speichern

app = Flask("bewertung")


@app.route('/')
def start():
    ueberschrift_txt = "Willkommen auf der Bewertungs-Website"
    einleitung_txt = "Hier können Sie Ihre Bewertung für unsere Speisen abgeben"
    return render_template('start.html', app_name="Bewertung", ueberschrift=ueberschrift_txt, einleitung=einleitung_txt)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():
    if request.method == 'POST':
        bewertungseingabe = request.form['bewertungseingabe']
        sterne = request.form['sterne']
        antwort = speichern(bewertungseingabe, sterne)
        return 'Gespeicherte Daten: <br>' + str(antwort)
    return render_template('eingabe.html', app_name="Bewertung abgeben")


@app.route('/about')
def about():
    ueberschrift_txt = "Über diese Web-App"
    einleitung_txt = "Diese App wurde als Demo App programmiert"
    return render_template('start.html', app_name="About", ueberschrift=ueberschrift_txt, einleitung=einleitung_txt)







if __name__ == "__main__":
    app.run(debug=True, port=5000)
