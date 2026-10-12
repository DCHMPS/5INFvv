Voornaam = input("Voornaam: ")
Achternaam = input("Achternaam: ")
Functietitel = input("Functietitel: ")

Naam = f"{Voornaam} {Achternaam}".upper()

# Breedte bepalen van langste regel op naamkaartje (+ marge van 2 spaties links en rechts)
Breedte = max(len(Naam), len(Functietitel)) + 4

Rand = "+" + "-" * Breedte + "+"
Regel_Naam = "|" + Naam.center(Breedte) + "|"
Regel_Functietitel = "|" + Functietitel.center(Breedte) + ""

print(Rand)
print(Regel_Naam)
print(Regel_Functietitel)
print(Rand)