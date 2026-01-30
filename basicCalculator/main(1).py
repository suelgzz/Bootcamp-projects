from operations import topla, cikar, carp, bolme
from utils import guvenli_sayi_al

while True:
    print("--Hesap Makinesi--")
    print("1. toplama")
    print("2. cikarma")
    print("3. carpma")
    print("4. bolme")
    print("5. cikis")

    secim = input("bir islem secin ")

    if secim == '5':
        print("cikis yapiliyor")
        break

    try:
        sayi1 = guvenli_sayi_al()
        sayi2 = guvenli_sayi_al()

        if secim == '1':
            print(f"Sonuç: {topla(sayi1, sayi2)}")
        elif secim == '2':
            print(f"Sonuç: {cikar(sayi1, sayi2)}")
        elif secim == '3':
            print(f"Sonuç: {carp(sayi1, sayi2)}")
        elif secim == '4':
            print(f"Sonuç: {bolme(sayi1, sayi2)}")
        else:
            print("lutfen tekrar deneyin.")

    except ValueError:
        print("gecersiz girdi, lutfen sayi girin.")
