şifre="205@a123A"
kullaniciadi="FbG"
username=input("Kullanıcı Adı Giriniz: ")
parola=input("Parola Giriniz: ")
if kullaniciadi==username and şifre==parola:
    print("Başarıyla giriş yaptınız.")
    print("Ne yapmak istersiniz?")
elif kullaniciadi==username and şifre!=parola:
    print("Parola yanlış, tekrar deneyiniz.")
elif kullaniciadi!=username and şifre==parola:
    print("Kullanıcı adı yanlış, tekrar deneyiniz.")
elif kullaniciadi!=username and şifre!=parola:
    print("Kullanıcı adı ve parola yanlış, tekrar deneyiniz.")