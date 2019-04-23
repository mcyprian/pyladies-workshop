import json

def nacti_operaci():
    # Vyber operace je mozne riesit jednoducho s vyuzitim funkcie
    # input, v pripade nevalidnej volby vyzvu opakujeme:
    operace = ""
    while operace not in ["p", "z", 'k']:
        operace = input("Zvol operaci p (pridaj) | z (zmaz) | k (konec): ")
    return operace


def naciti_den():
    # Nacita od uzivatela pomocou funkcie input den v tyzdni a overi
    # ze ide o validnu moznost, da sa riesit podobne ako nacti_operaci
    den = ""
    while den not in ["pondelok", "utorok", "streda", "stvrtok", "piatok"]:
        den = input("Zvol den pondelok|utorok|streda|stvrtok|piatok: ")
    return den


def operace_pridej(diar, den):
    # Implementacia operacie pridej, nacita od uzivatela aktivity a prida
    # do slovnika na zvoleny den, pokial je na dany den uz nejaka aktivita
    # naplanovana vypise upozornenie a obsah slovnika nemeni.
    diar[den].append(input("Zadaj Udalost: "))


def operace_zmaz(diar, den):
    # Implementacia operacie zmaz, zmaze udalosti vybraneho dna (nastavi na
    # uvodnu hodnotu "")
    diar[den] = []


def vypis_diar(diar):
    # Vypise aktualny obsah slovnika diar prehladnym sposobom
    for key, value in diar.items():
        print(f"  {key}: {value}")


def uloz_diar(diar):
    with open("diar.json", "w") as soubor:
        json.dump(diar, soubor)


def nacti_diar():
    with open("diar.json", "r") as soubor:
        return json.load(soubor)


# Cely  program musi bezat v smycke aby opakovane vypisoval obsah diara a
# dotazoval sa na operace az kym uzivztel nezvoli konec (k):
diar = nacti_diar()

operace = ""
while True:
    vypis_diar(diar)
    operace = nacti_operaci()
    # Po overeni ze nacitana hodnota je validna mozme program vetvit
    # na zaklade zvolenej operace
    if operace == "p":
        den = naciti_den()
        operace_pridej(diar, den)
    elif operace == "z":
        den = naciti_den()
        operace_zmaz(diar, den)
    elif operace == "k":
        uloz_diar(diar)
        break
