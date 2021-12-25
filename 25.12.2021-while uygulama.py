#Kullanıcı adı admin, şifre 123456 yazınca sisteme giriş başarılı, bunların dışında bir şey yazınca kullanıcı adı veya
#şifre hatalı diyerek tekrar kullanıcı adı ve şifreyi isteyen bir uygulama geliştiriniz. Sonsuz kere soracak.
#Doğru bilince break yapacak.
#doğru yanlışı if ile sorgulayacak.
#break sonrası while bitiminden devam edecek.
#sisteme girildi yazacak.
while True:
    kullaniciadi=input("Kullanıcı adı giriniz:").lower
    şifre=input("Şifre giriniz")
if kullaniciadi==(admin) and şifre==(123456):
         print("Sisteme giriş başarılı.")
         break
else:
    print("Kullanıcı adı veya şifre hatalı.")