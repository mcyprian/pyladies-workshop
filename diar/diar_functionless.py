# definicia slovnika bude pre zakladnu variantu
# vyzerat asi takto:
diar = {
    "pondelok": "",
    "utorok": "",
    "streda": "",
    "stvrtok": "",
    "piatok": "",
}

# Cely  program musi bezat v smycke aby opakovane vypisoval obsah diara a
# dotazoval sa na operace az kym uzivztel nezvoli konec (k):
operace = ""
while operace != "k":
    for key, value in diar.items():
        print(f"  {key}: {value}")
    operace = ""
    while operace not in ["p", "z", 'k']:
        operace = input("Zvol operaci p (pridaj) | z (zmaz) | k (konec): ")
    # Po overeni ze nacitana hodnota je validna mozme program vetvit
    # na zaklade zvolenej operace
    if operace == "p":
        den = ""
        while den not in ["pondelok", "utorok", "streda", "stvrtok", "piatok"]:
            den = input("Zvol den pondelok|utorok|streda|stvrtok|piatok: ")
        if diar[den] is not "":
            print(f"den {den} je uz obsadeny, pouzi najprv operaci zmaz (z).")
        else:
            diar[den] = input("Zadaj Udalost: ")
    elif operace == "z":
        den = ""
        while den not in ["pondelok", "utorok", "streda", "stvrtok", "piatok"]:
            den = input("Zvol den pondelok|utorok|streda|stvrtok|piatok: ")
        diar[den] = ""
