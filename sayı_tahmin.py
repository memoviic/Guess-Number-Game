import random
liste = random.randrange(1,100)
def sayı_tahmini():
    tahmin = int(input("Lütfen tahmininizi giriniz:"))
    while liste != tahmin :
        if tahmin < liste:
            print("Biraz daha yükselt")
            tahmin = int(input("Sayı giriniz:"))
        elif liste < tahmin:
            print("Biraz daha küçült")
            tahmin = int(input("Sayı giriniz:"))
        else:
            break
    print("Tebrikler")

sayı_tahmini()
    
