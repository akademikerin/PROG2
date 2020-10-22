def hundert_franken_rabatt (preis):
    neuer_preis = 0

    if preis >= 100:
        neuer_preis = preis - (preis * 0.05)
    else:
        neuer_preis = preis
    return neuer_preis

berechneter_preis = hundert_franken_rabatt(100)
print(berechneter_preis)
