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
        bewertung_aussehen_vorspeise = request.form['sterne_aussehen_vorspeise']
        bewertung_geschmack_vorspeise = request.form['sterne_geschmack_vorspeise']
        bewertung_menge_vorspeise = request.form['sterne_menge_vorspeise']
        bewertung_aussehen_hauptspeise = request.form['sterne_aussehen_hauptspeise']
        bewertung_geschmack_hauptspeise = request.form['sterne_geschmack_hauptspeise']
        bewertung_menge_hauptspeise = request.form['sterne_menge_hauptspeise']
        bewertung_aussehen_dessert = request.form['sterne_aussehen_dessert']
        bewertung_geschmack_dessert = request.form['sterne_geschmack_dessert']
        bewertung_menge_dessert = request.form['sterne_menge_dessert']
        bewertung_service = request.form['sterne_service']
        anmerkungen = request.form['anmerkungen']
        bewertungseingabe = {"Aussehen_Vorspeise": bewertung_aussehen_vorspeise, "Geschmack Vorspeise": bewertung_geschmack_vorspeise, "Menge Vorspeise": bewertung_menge_vorspeise, "Aussehen Hauptspeise": bewertung_aussehen_hauptspeise, "Geschmack Hauptspeise": bewertung_geschmack_hauptspeise, "Menge Hauptspeise": bewertung_menge_hauptspeise, "Aussehen Dessert": bewertung_aussehen_dessert, "Geschmack Dessert": bewertung_geschmack_dessert, "Menge Dessert": bewertung_menge_dessert, "Service": bewertung_service, "Anmerkungen": anmerkungen}
        antwort = speichern(bewertungseingabe)
        return 'Gespeicherte Daten:' + str(bewertungseingabe) + ' <br>' + str(antwort)
    return render_template('eingabe.html', app_name="Bewertung abgeben", vorspeisen=['Salat', 'Suppe', 'Tatar'])


@app.route('/restaurant')
def restaurant():
    ueberschrift_txt = "Willkommen im Restaurant Hirschen"
    einleitung_txt = "Hier finden Sie unsere aktuelle Speisekarte"
    return render_template('start.html', app_name="Restaurant", ueberschrift=ueberschrift_txt, einleitung=einleitung_txt)


@app.route('/about')
def about():
    ueberschrift_txt = "Über diese Web-App"
    einleitung_txt = "Diese App wurde als Demo App programmiert"
    return render_template('start.html', app_name="About", ueberschrift=ueberschrift_txt, einleitung=einleitung_txt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
