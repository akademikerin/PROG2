import json


def speichern(bewertungseingabe):

    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)

    except:
        eintraege = {}

    eintraege["Aussehen_Vorspeise"] = bewertungseingabe

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)
    return "Vielen Dank. Ihre Daten wurden gespeichert."