with open('slova.txt', 'r') as soubor:
    radky = list(soubor)

for radek in reversed(radky):
    print(radek.strip())
