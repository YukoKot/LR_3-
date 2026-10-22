import random
print("vuberi lvl:")
print("1 - Easy (5 popitok)")
print("2 - Middle (3 popitok)")
print("3 - Unposible (1 popitok)")

level = int(input("Vach lvl = "))
if level == 1:
    a = 5
elif level == 2:
    a = 3
else:
    a = 1
secret = random.randint(1, 10)
print(f"ugadaite chislo ot 1 do 10: ")
while a > 0:
    guess = int(input(f"Otwet: "))
    if guess == secret:
        print("Pozdravlayuu, you ugadali!")
        break
    else:
        a -= 1
        if a > 0:
            print("No ugadali! haha, ehe raz poprobyi.")
        else:
            print("No ugadali! haha,bilo zagadano: ", secret)