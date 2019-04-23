with open('slova.txt', 'r') as soubor:
    for radek in soubor:
        if "y" in radek:
            print(radek.strip())
