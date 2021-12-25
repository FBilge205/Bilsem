#Kullanıcıdan 10 tane sayı isteyerek bunları bir listeye atıp küçükten büyüğe doğru sıralayınız.
sayilar=[]
for i in range(10):
    sayi=int(input("Sayı giriniz:"))
    sayilar.append(sayi)
sayi=input("A'dan Z'ye mi, Z'den A'ya mı?(A-Z/Z-A):")
if sayi=="A-Z" or sayi=="a-z":
    sayilar.sort()
    print(sayilar)
elif sayi=="Z-A" or sayi=="z-a":
    sayilar.sort(reverse=True)
    print(sayilar)
else:
    print("Hatalı giriş")
