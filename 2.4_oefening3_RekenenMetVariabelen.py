startbedrag = 50.00
prijs_boek = 12.50
prijs_tijdschrift = 3.75

aantal_boeken = 2
aantal_tijdschriften = 3

totale_kosten = (aantal_boeken * prijs_boek) + (aantal_tijdschriften * prijs_tijdschrift)
overgebleven_geld = startbedrag - totale_kosten

print(f"Na het kopen van {aantal_boeken} boeken en {aantal_tijdschriften} tijdschriften heb ik nog €{overgebleven_geld} over.")