def tajenka(hadana_pismena, hledane_slovo):
    """
    Vypíše tajenku, z uhodnutých písmen neuhodnutých = _
    """
    # vypis pismeno z hledaneho slova pokud je v hadanych pismenech jinak _
    return ''.join([pismeno if pismeno.lower() in hadana_pismena else '_' for pismeno in hledane_slovo])

def bylatrefa(pismeno, hadane_slovo):
    """
    Zkontroluje jestli zadané písmeno je v tajence.
    Vrací True/False
    """
    if pismeno.lower() in hadane_slovo.lower():
        return True
    else:
        return False

def vypis_vysledky(vysledky):
    """
    vypise vysledky aktualni hry
    """
    poradi = 0
    for zaznam in vysledky:
        poradi += 1
        print(f"{poradi}. místo: {zaznam['jméno']} se ziskem {zaznam['skore']} bodů")

