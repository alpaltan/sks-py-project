import random
import time
import os


def SayiTahmin():
    levelList = [30, 50, 100, 200, 400]
    can = 10
    print("Sayi Tahmin Oyununa Hos Geldin!!!")
    print("***********************************\n")
    print("Oyunumuzda 5 adet seviye bulunuyor")
    print("1 ile 30, 50, 100, 200 ve 400 ")
    print("Arasindaki sayilari canin bitmeden dogru tahmin etmen gerekiyor!")
    print("Her yanlis tahmininde 1 can kaybedersin!")
    print("Dogru tahmininde ise 2 can kazanirsin!\n")
    print("***********************************")
    print(*"SIMDIDEN BOL SANS\n")
    for i in range(0, 5, 1):
        tepeDeger = levelList[i]
        randomSayi = random.randint(1, tepeDeger)
        if (can == 0):
            print("Uzgunum canin Bitti... :(")
            a = input("Menuye donmek icin Enter tusuna basin: ")
            OyunMenu()
            break
        print("Seviye: " + str(i+1))
        while can != 0:
            girilenDeger = int(
                input("1 ile " + str(tepeDeger) + " arasinda bir deger tahmin etme sirasi:"))
            if (girilenDeger == randomSayi):
                print("Tebrik Ederimm!!!\n2 can eklendi...")
                can += 2
                break
            elif (girilenDeger < (randomSayi)):
                can -= 1
                print("Tuttugum sayi tahmininden daha BUYUK! | Kalan Can: " + str(can))
            elif (girilenDeger > (randomSayi)):
                can -= 1
                print("Tuttugum sayi tahmininden daha KUCUK! | Kalan Can: " + str(can))


def AdamAsmaca():
    print(*"Nasil oynanir?")
    print("***********************************\n")
    print("1.Kullanici maksimum 12 harfli tek kelime yazar.\n")
    print("2.Kullanici bu kelimeyi asilmadan bulmaya calisir.\n")
    print("Turkce karakter kullanmak yasak!\n")
    print("***********************************")
    input("Hazirsaniz Enter tusuna basin...")

    kelime = input("Bulunmasini istediginiz kelimeyi girin:")
    kelime = kelime.upper
    os.system("clear")
    print("A B C D E F G H I J K L M N O P R S T U V Y Z W Q X\n")
    print("***********************************")


def OyunMenu():
    os.system("clear")
    print("Oyun Menusune Hos Geldiniz...\n")
    print("Lutfen Oynamak Istediginiz Oyunu Listeden Tuslayin\n")
    print("***********************************\n")
    print("1-Sayi Tahmin Oyunu 1-5 Level")
    print("2-Adam Asmaca 2 kisilik\n")
    oyunSec = int(input("***********************************\n"))
    print("\n")
    if (oyunSec == 1):
        SayiTahmin()
    elif (oyunSec == 2):
        AdamAsmaca()


OyunMenu()
