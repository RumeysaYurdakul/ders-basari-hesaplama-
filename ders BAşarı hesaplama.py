#ders başarı hesaplama programı
#10.11.2020

v1=eval(input("Vize 1 notunu giriniz(0-100):"))
v2=eval(input("Vize 2 notunu giriniz(0-100):"))
f=eval(input("Final notunu giriniz(0-100):"))

#evaluate çalıştırmak gibi bir anlamı var 

#ortalama hesabı
#örnek olarak,
#vize1 %20
#vize2 %30
#final %50
#etki oranına sahip olsun
ortalama =(v1*0.2)+(v2*0.3)+(f*0.5)

print("bu dersteki ortalamanız:",ortalama)

#iften sonra yapmamız gereken şey bir koşul
#if bütün dillerde kullanılır faklat başka dillerde farklılıkları var

if ortalama>=50:
    print("TEBRİKLER!")
    print("dersi başardınız")

#else koysaydık buraya yine çalışırdı . (eğer üsteki sağlanırsa üstteki aksi taktirde alttaki çalışır )
#farklı bir yol:
#if ortalama>=50:
  #  print("TEBRİKLER!")
  #  print("dersi başardınız")
#else eğer 50 den çüküse alttaki çalşışır.
   # print("üzgünüm....")
   # print("başarlı olamadınız.")
if ortalama<50:
    print("üzgünüm....")
    print("başarlı olamadınız.")



print("***program sonlandı***")

    #büyük eşittir matematikteki haliyle bilgisayarda olmadığından
    #büyüktür ve eşittir işaretini art arda yazarız 
   #NOT : SHELL EKRANINDA  BİRŞEYİN BİRŞEYE EŞİT OLUP OLMADIĞINI
    #KARŞILAŞTIRMAK İÇİN == (EŞİTEŞİT) KULLANILIR.
   #NOT:SHELL EKRANINDA BİRŞEYİN BİRŞEYE EŞİT OLMADIĞINI
    #KARIŞLAŞTIRIKEN !=(ÜNLEMEŞİT) KULLANILIR .
