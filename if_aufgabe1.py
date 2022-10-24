import random
#Erstelle eine Zufallszahl zwischen 0 und 100

zufallszahl = random.randint(0, 100)
		
#Gib die Zufallszahl aus
		
print(zufallszahl)

#Wenn die Zahl kleiner ist als 20  gib aus "Mini"

if zufallszahl < 20:
    print("Mini")

#Wenn die Zahl zw. 20 und 50 ist gib aus "Medium"

if zufallszahl > 20 and zufallszahl < 50:
    print("Medium")

#Wenn die Zahl größer als 50 ist gib aus "Large"

if zufallszahl > 50:
    print("Large")
