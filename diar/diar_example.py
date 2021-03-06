# definicia slovnika bude pre zakladnu variantu
# vyzerat asi takto:
diar = {
    "pondelok": "",
    "utorok": "",
    "streda": "",
    "stvrtok": "",
    "piatok": "",
}


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
    if diar[den] is not "":
        print(f"den {den} je uz obsadeny, pouzi najprv operaci zmaz (z).")
    else:
        diar[den] = input("Zadaj Udalost: ")


def operace_zmaz(diar, den):
    # Implementacia operacie zmaz, zmaze udalosti vybraneho dna (nastavi na
    # uvodnu hodnotu "")
    diar[den] = ""


def vypis_diar(diar):
    # Vypise aktualny obsah slovnika diar prehladnym sposobom
    for key, value in diar.items():
        print(f"  {key}: {value}")


# Cely  program musi bezat v smycke aby opakovane vypisoval obsah diara a
# dotazoval sa na operace az kym uzivztel nezvoli konec (k):
operace = ""
while operace != "k":
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
