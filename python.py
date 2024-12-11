#opgave 1
'''

tall1 = float(input("skriv in tall 1: "))
tall2 = float(input("skriv in tall 2: "))
operasjon = input("skriv in operasjon (+, -, *, /): ")

if operasjon == "+":
    print(tall1 + tall2)
elif operasjon == "-":
    print(tall1 - tall2)
elif operasjon == "*":
    print(tall1 * tall2)
elif operasjon == "/":
    print(tall1 / tall2)
else:
    print("Ugyldig operasjon")
'''

#oppgave 2
""""
lengde = float(input("skriv inn lengde: "))
bredde = float(input("skriv inn bredde: "))

print("arealet er: ", lengde * bredde)
"""

#oppgave 3
""""
navn = input("skriv inn navnet ditt: ")
alder = int(input("skriv inn alderen din: "))
print("Hei", navn, "du er", alder, "år gammel")
årtilhundre = 100 - alder
print("du har", årtilhundre, "år til hundre")
"""

#oppgave 4
""""
tall1 = float(input("skriv in tall 1: "))
if tall1 > 0:
    print("tall 1 er større enn 0")
elif tall1 < 0:
    print("tall 1 er mindre enn 0")
else:
    print("tall 1 er lik 0")
"""
#oppgave 5
""""
grense = int(input("skriv inn et tall: "))
summen = sum(range(1, grense + 1))
print("summen av tallene fra 1 til", grense, "er", summen)
"""

#oppgave 6
"""
navn_liste = []
navn_liste.append(input("Skriv inn navn 1: "))
navn_liste.append(input("Skriv inn navn 2: "))
navn_liste.append(input("Skriv inn navn 3: "))
navn_liste.append(input("Skriv inn navn 4: "))
navn_liste.append(input("Skriv inn navn 5: "))
print(navn_liste)
"""
#oppgave 7
"""""
navn_liste = []
for i in range(5):
    navn = input(f"Skriv inn navn {i + 1}: ")
    navn_liste.append(navn)
print(navn_liste)
"""

#oppgave 8
"""
def sorter_og_gjennomsnitt(tall_liste):
    tall_liste.sort()
    gjennomsnitt = sum(tall_liste) / len(tall_liste)
    return tall_liste, gjennomsnitt

tall = [5, 2, 9, 1, 7]
sortert, gjennomsnitt = sorter_og_gjennomsnitt(tall)
print(f"Sortert: {sortert}, Gjennomsnitt: {gjennomsnitt}")
"""

#oppgave 9
tall_liste = [1, 2, 3, 4, 5]
snudd_liste = tall_liste[::-1]
print(snudd_liste)