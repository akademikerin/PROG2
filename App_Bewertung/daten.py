import json

def speichern(bewertungseingabe):
    """
        Saves a rating input
        :param bewertungseingabe: The rating which must be saved
        :return: The result
    """
    bewertungen = alle_bewertungen_lesen()

    try:
        # w+ opens or creates file, if it does not already exist
        with open("datenbank.json", "w+") as datenbank:
            # Adds the new rating to the end of the list
            bewertungen.append(bewertungseingabe)
            # Puts the list of ratings to the file
            json.dump(bewertungen, datenbank, indent=4)

    except:
        return "Datenbank konnte nicht geöffnet/erweitert werden."


def alle_bewertungen_lesen():
    """
    Reads all ratings from the file
    :return: Database with saved ratings
    """

    try:
        # r+ reads or creates file, if it does not already exist
        with open("datenbank.json", "r+") as datenbank:
            return json.load(datenbank)
    except:
        return list()


def laden():
    """
    Reads all ratings
    :return: All ratings
    """
    bewertungen = alle_bewertungen_lesen()

    return bewertungen
