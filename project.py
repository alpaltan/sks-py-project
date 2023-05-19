import random
import time

levelList = [30, 50, 100, 200, 400]
seviye = 1
can = 10
print("***********************************")
print("Sayi Tahmin Oyununa Hos Geldin!!!\n")
print("Oyunumuzda 5 adet seviye bulunuyor")
print("1 ile 30, 50, 100, 200 ve 400 ")
print("Arasindaki sayilari canin bitmeden dogru tahmin etmen gerekiyor!")
print("Her yanlis tahmininde 1 can kaybedersin!")
print("Dogru tahmininde ise 2 can kazanirsin!")
print(*"SIMDIDEN BOL SANS")
print("***********************************\n")
for i in range(0, 5, 1):
    tepeDeger = levelList[i]
    randomSayi = random.randint(1, tepeDeger)
    while can != 0:
        girilenDeger = int(
            input("1 ile " + str(tepeDeger) + " arasinda bir sayi tut"))
        if (girilenDeger == randomSayi):
            print("buldun")
            can += 2
            break
        elif (girilenDeger < (randomSayi)):
            can -= 1
            print("Tuttugum sayi tahmininden daha buyuk")
        elif (girilenDeger > (randomSayi)):
            can -= 1
            print("Tuttugum sayi tahmininden daha kucuk")
