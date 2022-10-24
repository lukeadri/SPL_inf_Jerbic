import random
#Erstelle zwei Zufallszahl zwischen 0 und 100

zufallszahl1 = random.randint(0, 100)
print(zufallszahl1)

zufallszahl2 = random.randint(0, 100)
print(zufallszahl2)

#Wenn die erste Zahl kleiner ist als die zweite UND die erste Zahl kleiner ist als 50
#dann gib aus "Zahl 1 ist kleiner als Zahl 2 und Mini"

if zufallszahl1 < zufallszahl2 and zufallszahl1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

#Wenn die erste Zahl kleiner ist als 30 oder die zweite Zahl kleiner ist als 30
#dann gib aus "Eine der beiden ist kleiner als 30"

if zufallszahl1 < 30 or zufallszahl2 < 30:
    print("Eine der beiden ist kleiner als 30")

#Wenn die erste Zahl kleiner ist als 50 UND die zweite Zahl ungleich 50 ist
#dann gib aus "Erste Zahl klein, zweite kein 50iger"
	
if zufallszahl1 < 50 and zufallszahl2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")