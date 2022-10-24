import random
sum = 0
sum2 = 0

for i in range(0,6):
        randomNumber1 = random.randint(1, 6)
        sum = sum + randomNumber1
for i in  range(0,6):
        print("Würfeln mit w")
        wuerfel = (input())
        if wuerfel == "w":
            randomNumber2 = random.randint(1, 6)
            print("du hast", randomNumber2, "gewürfelt")
        sum2 = sum + randomNumber2

if sum > sum2:
        print("Der Computer  gewinnt mit ", sum, " du hast ", sum2)
else:
        print("Du gewinnst mit ", sum2, "der Computer hat", sum)