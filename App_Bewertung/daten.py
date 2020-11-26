import json


def speichern(bewertungseingabe):
    """
        Speichert eine Bewertungseingabe
        :param bewertungseingabe: Die Bewertung welche gespeichert werden muss
        :return: Das Ergebnis
    """
    bewertungen = alle_bewertungen_lesen()

    try:
        # w+ öffnet oder erstellt die Datei, falls sie noch nicht existiert.
        with open("datenbank.json", "w+") as datenbank:
            # hängt die neue Bewertung an den Schluss der Liste
            bewertungen.append(bewertungseingabe)
            # schreibt die Liste der Bewertungen in die Datei
            json.dump(bewertungen, datenbank, indent=4)

    except:
        return "Datenbank konnte nicht geöffnet/erweitert werden."

    return "Vielen Dank. Ihre Daten wurden gespeichert."

def alle_bewertungen_lesen():
    """
        Liest alle bewertungen aus dem file und gibt diese zurück.
    """
    try:
        # r+, liest eine datei, oder erstellt diese, falls sie nicht existiert.
        # ACHTUNG! WEGEN DEM AUSLESEN ALLER ZEILEN, WIRD DEM GERÄT DER ARBEITSPEICHER AUSGEHEN, SOBALD DIE DATEI ~16GIGABYTE GROSS IST.
        with open("datenbank.json", "r+") as datenbank:
            return json.load(datenbank)
    except:
        return list()


def laden():
    bewertungen = alle_bewertungen_lesen()

    try:
        with open("datenbank.json", "r") as datenbank:
            bewertungen.append(bewertungseingabe)
            json.dump(bewertungen, datenbank, indent=4)

    except:
        return "Datenbank konnte nicht geöffnet/erweitert werden."

    return bewertungen