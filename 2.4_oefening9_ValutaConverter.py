Wisselkoers_EUR_naar_USD = 1.12

Bedrag = float(input("Bedrag: "))

# strip().upper() zorgt ervoor dat wat je intypt volledig kleine letters worden en daarna iedere letter een grote letter wordt
Bronvaluta = input("Bronvaluta (EUR of USD): ").strip().upper()

if Bronvaluta == 'EUR':
    Doelvaluta = 'USD'
    Resultaat = Bedrag * Wisselkoers_EUR_naar_USD

if Bronvaluta == 'USD':
    Doelvaluta = 'EUR'
    Resultaat = Bedrag * Wisselkoers_EUR_naar_USD

print(f"{Bedrag:.2f} {Bronvaluta} is gelijk aan {Resultaat:.2f} {Doelvaluta}")