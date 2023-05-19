import random
import time

randomSayi = random.randint(1, 20)
seviye = 1
can = 7
print(randomSayi)
while True:
    girilenDeger = int(input("1 ile 20 arasinda bir sayi tut"))
    if (girilenDeger == randomSayi):
        print("buldun")
        break
    elif (girilenDeger < (randomSayi)):
        print("Tuttugum sayi tahmininden daha buyuk")
    elif (girilenDeger > (randomSayi)):
        print("Tuttugum sayi tahmininden daha kucuk")
