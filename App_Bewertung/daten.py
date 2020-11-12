import json


def speichern(bewertungseingabe, sterne):

    try:
        with open("datenbank.json", "r") as datenbank:
            eintraege = json.load(datenbank)

    except:
        eintraege = []

    eintrag = bewertungseingabe, sterne

    eintraege.append(eintrag)

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)
    return "Vielen Dank. Ihre Daten wurden gespeichert."