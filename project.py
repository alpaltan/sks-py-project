import random
import time

levelList = [30, 50, 100, 200, 400]
seviye = 1
can = 10
for i in range(0, 5, 1):
    tepeDeger = levelList[i]
    randomSayi = random.randint(1, tepeDeger)
    while can != 0:
        girilenDeger = int(
            input("1 ile " + str(tepeDeger) + " arasinda bir sayi tut"))
        if (girilenDeger == randomSayi):
            print("buldun")
            break
        elif (girilenDeger < (randomSayi)):
            print("Tuttugum sayi tahmininden daha buyuk")
            can -= 1
        elif (girilenDeger > (randomSayi)):
            can -= 1
            print("Tuttugum sayi tahmininden daha kucuk")
