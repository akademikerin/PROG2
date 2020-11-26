from flask import Flask
from flask import render_template
from flask import request
from flask import url_for

from daten import speichern, laden

app = Flask("bewertung")


@app.route('/')
def start():
    ueberschrift_txt = "Willkommen auf der Bewertungs-Website"
    einleitung_txt = "Hier können Sie Ihre Bewertung für unsere Speisen abgeben"
    return render_template('start.html', app_name="Bewertung", ueberschrift=ueberschrift_txt, einleitung=einleitung_txt)


@app.route('/eingabe', methods=['POST', 'GET'])
def eingabe():
    if request.method == 'POST':
        vorspeise = request.form['eingabe_vorspeisen']
        bewertung_aussehen_vorspeise = request.form['sterne_aussehen_vorspeise']
        bewertung_geschmack_vorspeise = request.form['sterne_geschmack_vorspeise']
        bewertung_menge_vorspeise = request.form['sterne_menge_vorspeise']
        hauptspeise = request.form['eingabe_hauptspeisen']
        bewertung_aussehen_hauptspeise = request.form['sterne_aussehen_hauptspeise']
        bewertung_geschmack_hauptspeise = request.form['sterne_geschmack_hauptspeise']
        bewertung_menge_hauptspeise = request.form['sterne_menge_hauptspeise']
        bewertung_aussehen_dessert = request.form['sterne_aussehen_dessert']
        bewertung_geschmack_dessert = request.form['sterne_geschmack_dessert']
        bewertung_menge_dessert = request.form['sterne_menge_dessert']
        dessert = request.form['eingabe_desserts']
        bewertung_service = request.form['sterne_service']
        anmerkungen = request.form['anmerkungen']
        bewertungseingabe = {"vorspeise": vorspeise,
                             "aussehen_vorspeise": bewertung_aussehen_vorspeise,
                             "geschmack vorspeise": bewertung_geschmack_vorspeise,
                             "menge vorspeise": bewertung_menge_vorspeise,
                             "hauptspeise": hauptspeise,
                             "aussehen hauptspeise": bewertung_aussehen_hauptspeise,
                             "geschmack hauptspeise": bewertung_geschmack_hauptspeise,
                             "menge hauptspeise": bewertung_menge_hauptspeise,
                             "dessert": dessert,
                             "aussehen dessert": bewertung_aussehen_dessert,
                             "geschmack dessert": bewertung_geschmack_dessert,
                             "menge dessert": bewertung_menge_dessert,
                             "service": bewertung_service,
                             "anmerkungen": anmerkungen
                             }
        antwort = speichern(bewertungseingabe)
        return 'Gespeicherte Daten:' + str(bewertungseingabe) + ' <br>' + str(antwort)
    return render_template(
        'eingabe.html',
        app_name="Bewertung abgeben",
        vorspeisen=['Salat', 'Suppe', 'Tatar'],
        hauptspeisen=['Pizza', 'Pasta', 'Risotto'],
        desserts=['Sorbet', 'Tiramisu', 'Käse']
    )

@app.route('/liste')
def liste():
    gespeicherte_bewertungen = laden()
    ueberschrift_txt = 'Ihre Bewertungsangaben'
    einleitung_txt = 'Hier wird Ihre Bewertung zu den bestellten Speisen aufgelistet.'
    return render_template(
        'liste.html',
        app_name="Restaurant",
        ueberschrift=ueberschrift_txt,
        einleitung=einleitung_txt,
        daten=gespeicherte_bewertungen
    )

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
