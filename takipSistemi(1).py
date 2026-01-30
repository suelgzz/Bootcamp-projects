def gorev_ekle(gorev_listesi):
    gorev = input("gorev adi:")
    gorev_listesi.append(gorev)

def gorevleri_listele(gorev_listesi):
    for i in range(len(gorev_listesi)):
        print(f"{i + 1}.{gorev_listesi[i]}")

def gorev_analizi(gorev_listesi):
    adet = len(gorev_listesi)

    if adet == 0:
        print("gorev durumu: henuz gorev eklenmemis")
    elif 1 <= adet <= 3:
        print("gorev durumu: baslangic seviyesi")
    else:
        print("gorev durumu: yogun bir gun")

gorev_listesi = []

while True:
    print("\n1-gorev ekle")
    print("2-gorevleri listele")
    print("3-gorev analizi")
    print("4- cikis")

    secim = input("\nseciminiz:")

    if secim == "1":
        gorev_ekle(gorev_listesi)
    elif secim == "2":
        gorevleri_listele(gorev_listesi)
    elif secim == "3":
        gorev_analizi(gorev_listesi)
    elif secim == "4":
        break
print("Programdan cikiliyor.")
