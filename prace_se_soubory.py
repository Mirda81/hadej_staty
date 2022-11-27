from random import randint
import pickle

def nahodneslovo(soubor = 'data/countries.TXT' ):
    """
    Vrátí náhodné slovo ze zadaného souboru

    """
    muj_soubor = open(soubor).read()
    listslov = muj_soubor.splitlines()
    slovo = listslov[randint(0, len(listslov))]
    return slovo

def uloz_vysledky(nazev_souboru, objekt_k_ulozeni,slozka_ulozeni='data/'):
  """
  ukládá binární soubor do zvolené složky
  """
  f = open(slozka_ulozeni+nazev_souboru +".obj", 'wb')
  pickle.dump(objekt_k_ulozeni, f)
  f.close()



def nacti_vysledky(nazev_souboru, adresar_ulozeni='data/'):
    """
    načte soubor
    """
    f = open(adresar_ulozeni + nazev_souboru +".obj", 'rb')
    objekt = pickle.load(f)
    f.close()
    return objekt
#
def aktualizuj_nejlepsi_hry(list_novy):
    """
    Nový list připojí k načtenému, seřadí dle skore a pote vratí 10 nejlepších výsledků
    """
    # pokud existuje soubor se zápisem tak ho nacti jinak je záspis nový list
    try:
        list_historie = nacti_vysledky('vysledky_jednotlive')
        list_historie.extend(list_novy)
        list_historie.sort(key=lambda d: d["skore"], reverse=True)
        return list_historie[:9]
    except FileNotFoundError:
        return list_novy


def vypis_top_ten(soubor):
    """
    vypise nejlepších 10 her ze zadaného souboru
    """
    vysledky = nacti_vysledky(soubor)
    poradi = 0
    for zaznam in vysledky:
        poradi += 1
        print(f"{poradi}. místo: {zaznam['jméno']} se ziskem {zaznam['skore']} bodů")


def aktualizuj_nejlepsi_hrace(nove_vysledky):
    """
    Přičte výsledky z jedno lis/dict do historického list/dict
    """
    # pokud existuje soubor se zápisem tak ho nacti jinak je záspis nový list
    try:
        list_historie = nacti_vysledky('historie_hracu')
        # hledání záznamů z nových výsledků v načteném souboru, pokud je záznam v historii tak přičti skóre, jinak přidej výsledek do historie
        for vysledek_hrace in nove_vysledky:
            zmena = False
            for zaznam in list_historie:
                if vysledek_hrace['jméno'] == zaznam['jméno']:
                    zaznam['skore'] += vysledek_hrace['skore']
                    zmena = True
                    break
            if zmena == False:
                list_historie.append(vysledek_hrace)

        list_historie.sort(key=lambda d: d["skore"], reverse=True)
        return list_historie[:9]
    except FileNotFoundError:
        return nove_vysledky








