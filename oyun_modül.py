import time
import random


def sayiAl():
    sayi_tahmin = int(input("Sayıyı tahmin ediniz: "))
    return sayi_tahmin


def oyunBaslat():
    print("""
           *** Sayı tahmin oyununa hoşgeldiniz ! ***
           """)
    rastgele_sayi = random.randint(1, 100)
    while True:
        sayac = 0
        sayi_tahmin = sayiAl()
        if sayi_tahmin > rastgele_sayi:
            print("Kontrol Ediliyor")
            for i in range(3):
                time.sleep(1)
                print(".",end="",sep="")
            print("Girdiğiniz sayı gizli sayıdan büyük !")
        elif sayi_tahmin < rastgele_sayi:
            print("Kontrol Ediliyor")
            for i in range(3):
                time.sleep(1)
                print(".", end="",sep="")
            print("Girdiğiniz sayı gizli sayıdan küçük !")
        else:
            print("Kontrol Ediliyor")
            for i in range(3):
                time.sleep(1)
                print(".",end="",sep="")
            print("DOĞRU ! ")
            break
        sayac += 1
