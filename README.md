import random

secret = random.randint(1,10)
guess = int(input("ugadaite chislo ot 1 do 10: "))
if guess == secret:
print("Pozdravlayuu, you ugadali!)
else:
print("No ugadali! haha,bilo zagadano: ", secret)
