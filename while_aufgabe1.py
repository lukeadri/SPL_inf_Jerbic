import random

sum = 0

while True:
    num = random.randint(10, 30)
    print(num)
    sum = sum + num
    if num == 15 or num == 25:
        break

print(sum)