from flask import Flask
from flask import render_template
from flask import request

import plotly.graph_objects as go

from daten import speichern, laden

app = Flask("bewertung")


@app.route('/')
def start():
    """
    Homepage of application
    :return: Load start.html
    """
    ueberschrift_txt = "Herzlich Willkommen im Restaurant Hirschen"
    return render_template('start.html', app_name="Bewertung", ueberschrift=ueberschrift_txt)


@app.route('/eingabe', methods=['POST'])
def eingabe_post():
    """
    User can vote for each dish
    :return: Statistics with average ratings
    """
    vorspeise = request.form['eingabe_vorspeisen']
    bewertung_aussehen_vorspeise = request.form['sterne_aussehen_vorspeise']
    bewertung_geschmack_vorspeise = request.form['sterne_geschmack_vorspeise']
    bewertung_menge_vorspeise = request.form['sterne_menge_vorspeise']

    hauptspeise = request.form['eingabe_hauptspeisen']
    bewertung_aussehen_hauptspeise = request.form['sterne_aussehen_hauptspeise']
    bewertung_geschmack_hauptspeise = request.form['sterne_geschmack_hauptspeise']
    bewertung_menge_hauptspeise = request.form['sterne_menge_hauptspeise']

    dessert = request.form['eingabe_desserts']
    bewertung_aussehen_dessert = request.form['sterne_aussehen_dessert']
    bewertung_geschmack_dessert = request.form['sterne_geschmack_dessert']
    bewertung_menge_dessert = request.form['sterne_menge_dessert']

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
                         "anmerkungen": anmerkungen
                         }
    antwort = speichern(bewertungseingabe)
    if antwort is not None:
        return antwort
    return statistik()


@app.route('/eingabe', methods=['GET'])
def eingabe_request():
    """
    Allows adjustments of the dishes
    :return: Dishes
    """
    return render_template('eingabe.html',
                           app_name="Bewertung abgeben",
                           vorspeisen=['Lachsforellenfilet',
                                       'Steinpilzcrèmesuppe',
                                       'Nüsslisalat mit Ei'],
                           hauptspeisen=['Lammcarré mit Perlcouscous',
                                         ' Entenbrust mit Preiselbeerjus',
                                         'Risotto mit Kürbisragout'],
                           desserts=['Schoggi-Mille feuille',
                                     'Zuger Kirschtorte',
                                     'Käse mit Früchtebrot']
                           )


@app.route('/liste')
def liste():
    """
    Shows all submitted ratings incl. comments
    :return: Load liste.html
    """
    gespeicherte_bewertungen = laden()
    ueberschrift_txt = 'Ihre Bewertungsangaben'
    einleitung_txt = 'Hier wird Ihre Bewertung zu den bestellten Speisen aufgelistet.'
    return render_template(
        'liste.html',
        app_name="Liste",
        ueberschrift=ueberschrift_txt,
        einleitung=einleitung_txt,
        daten=gespeicherte_bewertungen
    )


@app.route('/statistik')
def statistik():
    """
    Creates a plotly diagram with all ratings
    :return: Load statistik.html with generated plotly diagram
    """
    aussehen_vorspeise = dict()
    geschmack_vorspeise = dict()
    menge_vorspeise = dict()

    aussehen_hauptspeise = dict()
    geschmack_hauptspeise = dict()
    menge_hauptspeise = dict()

    aussehen_dessert = dict()
    geschmack_dessert = dict()
    menge_dessert = dict()

    anmerkungen = list()

    bewertungen = laden()

    """
    Copies rating to table format
    Key = Type of dish
    Value = List of individual ratings
    """

    for eine_bewertung in bewertungen:
        vorspeisen_typ = eine_bewertung["vorspeise"]
        hauptspeisen_typ = eine_bewertung["hauptspeise"]
        dessert_typ = eine_bewertung["dessert"]
        if vorspeisen_typ not in aussehen_vorspeise:
            aussehen_vorspeise[vorspeisen_typ] = list()
            geschmack_vorspeise[vorspeisen_typ] = list()
            menge_vorspeise[vorspeisen_typ] = list()

        if hauptspeisen_typ not in aussehen_vorspeise:
            aussehen_hauptspeise[hauptspeisen_typ] = list()
            geschmack_hauptspeise[hauptspeisen_typ] = list()
            menge_hauptspeise[hauptspeisen_typ] = list()

        if dessert_typ not in aussehen_vorspeise:
            aussehen_dessert[dessert_typ] = list()
            geschmack_dessert[dessert_typ] = list()
            menge_dessert[dessert_typ] = list()

        aussehen_vorspeise[vorspeisen_typ].append(int(eine_bewertung["aussehen_vorspeise"]))
        geschmack_vorspeise[vorspeisen_typ].append(int(eine_bewertung["geschmack vorspeise"]))
        menge_vorspeise[vorspeisen_typ].append(int(eine_bewertung["menge vorspeise"]))

        aussehen_hauptspeise[hauptspeisen_typ].append(int(eine_bewertung["aussehen hauptspeise"]))
        geschmack_hauptspeise[hauptspeisen_typ].append(int(eine_bewertung["geschmack hauptspeise"]))
        menge_hauptspeise[hauptspeisen_typ].append(int(eine_bewertung["menge hauptspeise"]))

        aussehen_dessert[dessert_typ].append(int(eine_bewertung["aussehen dessert"]))
        geschmack_dessert[dessert_typ].append(int(eine_bewertung["geschmack dessert"]))
        menge_dessert[dessert_typ].append(int(eine_bewertung["menge dessert"]))

        anmerkungen.append(str(eine_bewertung["anmerkungen"]))

    vorspeisen_diagramm = generiere_diagram(aussehen_vorspeise, geschmack_vorspeise, menge_vorspeise)
    hauptspeise_diagramm = generiere_diagram(aussehen_hauptspeise, geschmack_hauptspeise, menge_hauptspeise)
    dessert_diagramm = generiere_diagram(aussehen_dessert, geschmack_dessert, menge_dessert)

    vorspeisen_diagramm = vorspeisen_diagramm.to_json()
    hauptspeise_diagramm = hauptspeise_diagramm.to_json()
    dessert_diagramm = dessert_diagramm.to_json()

    ueberschrift_txt = 'Statistik'
    einleitung_txt = 'Besten Dank für Ihre Bewertung. ' \
                     'Hier werden die durchschnittlichen Bewertungen pro Speise und pro Kategorie aufgeführt:'
    return render_template(
        'statistik.html',
        app_name="Statistik",
        ueberschrift=ueberschrift_txt,
        einleitung=einleitung_txt,
        vorspeisen_diagramm=vorspeisen_diagramm,
        hauptspeise_diagramm=hauptspeise_diagramm,
        dessert_diagramm=dessert_diagramm)


def calc_average(num):
    # Calculates average values of different categories
    sum_num = 0
    # For each variable in the list the sum should be increased by variable
    # For each variable in the list the sum should be increased by variable
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


def generiere_diagram(bewertungen_aussehen, bewertungen_geschmack, bewertungen_menge):
    vorspeisen_typen = list()
    diagramm = go.Figure()
    resultate_aussehen = list()
    resultate_geschmack = list()
    resultate_menge = list()

    for vorspeisen_typ in bewertungen_aussehen:
        vorspeisen_typen.append(vorspeisen_typ)
        resultate_aussehen.append(calc_average(bewertungen_aussehen[vorspeisen_typ]))
        resultate_geschmack.append(calc_average(bewertungen_geschmack[vorspeisen_typ]))
        resultate_menge.append(calc_average(bewertungen_menge[vorspeisen_typ]))

    diagramm.add_trace(go.Bar(x=vorspeisen_typen, y=resultate_aussehen, name="Aussehen"))
    diagramm.add_trace(go.Bar(x=vorspeisen_typen, y=resultate_geschmack, name="Geschmack"))
    diagramm.add_trace(go.Bar(x=vorspeisen_typen, y=resultate_menge, name="Menge"))
    diagramm.update_layout(barmode='group')
    return diagramm


@app.route('/about')
def about():
    """
    Shows general information about web-app
    :return: Load about.html
    """
    ueberschrift_txt = "Über diese Web-App"
    return render_template('about.html', app_name="About", ueberschrift=ueberschrift_txt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
