def guvenli_sayi_al():
    while True:
        try:
            sayi = int(input(" bir sayi girin: "))
            return sayi
        except ValueError:
            print("bir tam sayi girin." )