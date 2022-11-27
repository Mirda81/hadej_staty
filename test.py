import prace_se_soubory as soubory

novy_list = [{'jméno': 'Mirda', 'skore': 1050}, {'jméno': 'kokot', 'skore': 5000}]
# aktualizace = soubory.aktualizuj_nejlepsi_hry(novy_list)
# soubory.uloz_vysledky('vysledky_jednotlive',aktualizace)
# print(soubory.nacti_vysledky('vysledky_jednotlive'))
# print(soubory.aktualizuj_nejlepsi_hrace(novy_list))
print(soubory.vypis_top_ten('historie_hracu'))