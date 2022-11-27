import sibenice_funkce as hadani
import HracTrida
import prace_se_soubory as soubory
import pandas as pd

pocet_hracu = input('Zadej počet hráčů: ')
hraci = []
mrtvi_hraci = []
for i in range(0, int(pocet_hracu)):
    hraci.append(HracTrida.Hrac(input(f"Zadej jméno {i + 1}. hráče")))
hrajehrac = 0
aktivni_hrac = hraci[hrajehrac]

# dokud je nějaký hráč se životem tak vygeneruj slovo
while sum(player.zivoty for player in hraci) != 0:
    hledaneslovo = soubory.nahodneslovo()
    # v hadanych pismenech implicitně mezera aby při víceslovných názvech byla vidět a nebylo tam podtržítko
    hadanapismena = ' '
    moje_tajenka = hadani.tajenka(hadanapismena, hledaneslovo)
    # vytisklé s mezerou aby bylo lépe čitelné
    print(' '.join(moje_tajenka))

    # pokud neni uhodnuta tajenka a je ještě nějaký jráč se životem tak pokračuj
    while moje_tajenka != hledaneslovo and sum(player.zivoty for player in hraci) != 0:
        print(f'na řadě je hráč {aktivni_hrac.jmeno}')
        pismeno = input('zadej pismeno: ').lower()

        # kontrola jestli se písmeno už nehádalo, pokud ano tak odečti body a vyzvy znova
        while pismeno in hadanapismena:
            print(f'pismeno {pismeno} už si zkoušel vole!')
            aktivni_hrac.skoreminus()
            pismeno = input('zdaej pismeno: ').lower()
        hadanapismena += pismeno
        moje_tajenka = hadani.tajenka(hadanapismena, hledaneslovo)
        print(' '.join(moje_tajenka))

        #  pokud bylo písmeno trefeno tak pricti skore pokud je uhodnuta tajenka tak i život
        if hadani.bylatrefa(pismeno, hledaneslovo):
            aktivni_hrac.skoreplus(hledaneslovo.lower().count(pismeno))
            if moje_tajenka == hledaneslovo:
                aktivni_hrac.plus_zivot()

        # pokud nebylo trefeno odecti život a přepni na dalšího hráče
        else:
            hraci[hrajehrac].minus_zivot()
            # pokud hráči došli životy tak ho přeřaď do lisu mrtvých a uprav index hrajícího hráče
            if aktivni_hrac.zivoty == 0:
                mrtvi_hraci.append(hraci.pop(hrajehrac))
                hrajehrac -= 1
            # pokud hrál poslední hráč restartuj index
            if hrajehrac == len(hraci) - 1:
                hrajehrac = -1
            # přpenutí aktivního hráče pokud nějaký ještě zbyl
            hrajehrac += 1
            if len(hraci) > 0:
                aktivni_hrac = hraci[hrajehrac]

        # Vypiš statistiku pro hráče
        for hrac in hraci:
            hrac.statistika_hrace()

print(hledaneslovo)
# generuj a seřaď list výsledků
list_vysledku = [{"jméno": mrtvola.jmeno, "skore": mrtvola.skore} for mrtvola in mrtvi_hraci]
list_vysledku.sort(key=lambda d: d["skore"], reverse=True)
print('Výsledky hry:')
print('_____________')
hadani.vypis_vysledky(list_vysledku)

# aktualizuj hostorické výsledky a uloz
soubory.uloz_vysledky('vysledky_jednotlive', soubory.aktualizuj_nejlepsi_hry(list_vysledku))
soubory.uloz_vysledky('historie_hracu', soubory.aktualizuj_nejlepsi_hrace(list_vysledku))
# tiskni statistiky
print('Top 10 her of all time:')
print('__________________________')
soubory.vypis_top_ten('vysledky_jednotlive')
print('Top 10 hráčů of all time:')
print('__________________________')
soubory.vypis_top_ten('historie_hracu')
