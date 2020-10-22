import rechnungen

preisliste = []
preis = float(input("Preis:"))
preis = rechnungen.hundert_franken_rabatt(preis)

preisliste.append(preis)

with open("preisliste.txt", "w") as open_file:
    open_file.write(str(preisliste))

print(preis)