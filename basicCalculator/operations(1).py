def  topla (a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bolme(a, b):
    try:
        sonuc = a / b
        return sonuc
    except ZeroDivisionError:
        return "sifira bolme hatasi"
    
