gewicht = float(input("Geef je gewicht in kg: "))
lengte = float(input("Geef je lengte in m: "))

bmi = gewicht / (lengte * lengte)

print(f"Je BMI is {bmi:.1f}.")