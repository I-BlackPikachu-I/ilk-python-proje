import sqlite3
vt = sqlite3.connect("vt.sqlite")
istek=[]
im = vt.cursor() 

im.execute("""CREATE TABLE IF NOT EXISTS personel
    (ad, sifre, bakiye, odenmispara)""")


    



print("Kütüphanemize Hoşgeldiniz. ")
devamkontrol=0
toplam=0
sepetkitap=[]

kitap=[]
gunsonupara={}
gunsonukitap={}
devamlilik=0

roman=[["AD",            "KOD",             "KİRALAMA FİYATI"],
["Armağan",              "000",           "11"],
["Acımak",               "001",           "20"],
["Adı Aylin",            "002",           "21"],
["Akşam Güneşi",         "003",           "42"],
["Anadolu Notları",      "004",           "33"],
["Ankara",               "005",           "28"],
["Ateşten Gömlek",       "006",           "19"],
["Aşk-ı Memnu",          "007",           "20"],
["Aaraba Sevdası",       "008",           "51"],
["Ayaşlı ve Kiracıları", "009",           "108"] ]
macera=[["AD",            "KOD",             "KİRALAMA FİYATI"],
["AlacaKaranlık",           "000",               "71"],
["Hobbit",                  "001",               "10"],
["Watchmen",                "002",               "41"],
["Azra Kohen",              "003",               "42"],
["Yüzüklerin Efendisi",     "004",               "38"],
["Yolda",                   "005",               "25"],
["Don Kişot",               "006",               "19"],
["Kimyager",                "007",               "20"],
["Robinson Crusoe",         "008",               "56"],
["Dünyanın Uyanışı",        "009",               "111"] ]
aksiyon=[["AD",            "KOD",             "KİRALAMA FİYATI\n"],
["Da Vinci Şifresi",        "000",               "31"],
["Cehennem",                "001",               "43"],
["Alaycı Kuş",              "002",               "12"],
["Açlık Oyunları",          "003",               "42"],
["Üç Silahşor",             "004",               "28"],
["Ruhi Mücerret",           "005",               "25"],
["Tutulma",                 "006",               "19"],
["Siyah Kan",               "007",               "20"],
["Koloni",                  "008",               "86"],
["Labirent: Alev Deneyleri","009",               "81"]]
masal=[["AD",            "KOD",             "KİRALAMA FİYATI\n"],
["Peter Pan",               "000",               "61"],
["Değnek Adam",             "001",               "37"],
["Rapunzel",                "002",               "31"],
["Pamuk Prenses",           "003",               "42"],
["Keloğlan Masalları",      "004",               "78"],
["Yüzyüz",                  "005",               "85"],
["Ezop Masalları",          "006",               "39"],
["Ay'a Yolculuk",           "007",               "10"],
["Binbir Gece Masalları",   "008",               "66"],
["Üç Kedi Bir Dilek",       "009",               "69"]]
while(True):
    kayitsonrasi=0
    if kayitsonrasi==0:
        uyekontrol=input("Kütüphanemize Üye misiniz:(Üyeyseniz E değilseniz H)(gün sonu raporu için yönetici kodunu giriniz)\n")
    if uyekontrol==("E") or uyekontrol==("e") or kayitsonrasi==1:
        odenmiskitap=[]
        odenmispara=0
        devamkontrol=0
        toplamtutar=0
        bakiye=0
        sozlukkitap=[]
        ad=input("kullanici adınızı giriniz=\n")
        sifre=input("şifrenizi giriniz=\n")
        im.execute("""SELECT * FROM personel WHERE
        ad = ? AND sifre = ?""", (ad, sifre))

        data = im.fetchone()

        if data:
            print("Programa hoşgeldin {}!".format(data[0]))
        else:
            print("Parola veya kullanıcı adı yanlış!")
            
            devamkontrol=1
        
        
    elif uyekontrol==("H") or uyekontrol==("h"):
        ad=input("kullanıcı adınızı belirleyiniz? \n")
        sifre=input("şifrenizi belirleyiniz? \n")
        add_comand="""INSERT INTO personel VALUES {}"""
        data1=(ad,sifre,0,0)
        im.execute(add_comand.format(data1))
        vt.commit()
        kayitsonrasi=1
        devamkontrol=1
        
        
         
         
    elif uyekontrol=="01287":
        print("Bugün kütüphaneden hangi üyenin hangi kitapları aldığını gösteren liste:\n")
        print("AD     KİTAPLAR")
        for i in gunsonukitap.items():
            print(i[0]," ",i[1])
        print("\n\n")
        print("bugün kütüphanede hangi üyenin kaç para harcadığını gösteren liste : \n")
        print("AD     PARA")
        for i in gunsonupara.items():
            print(i[0]," ",i[1] )
        print("bugün kütüphanede hangi üyenin ne önerisi verdiğini gösteren liste : \n")
        print(istek)
        break
        
    else:
        print("Hatalı Bir kod yazdınız ya da yanlış bir harfe lütfen tekrar deniyiniz.\n")
        devamkontrol=7

    while(devamkontrol==0):
        
        class oneri:
            def sorgu(self):
                sorgu=(input("öneriniz var mı?\n"))
                if sorgu=="E" or sorgu=="e":
                    istek1=input("Önerinizi yazınız: \n")
                    istek.append(ad)
                    istek.append(istek1) 
                elif sorgu=="H" or sorgu=="h":
                    print("tabi efendim sistemden çıkış yapılıyor... :(")
        
        def denetleme():
            anamenü=input("ana menüye dönmek ister misiniz? \n")
            try:
                if anamenü=="e" or anamenü=="E":
                    devamlilik=0
                    return devamlilik
                elif anamenü=="h"or anamenü=="H":
                    print("kitap kiralamaya geri gönderiliyorsunuz...")
                    devamlilik=1
                    return devamlilik
                else:
                    print("hatalı sayı veya harf girişi lütfen tekrar deniyiniz.")
                    denetleme()
            except:
                print("Bir hata Meydana geldi lütfen iletişime geçiniz")
       
        
        def kod1(c,a):
            for i in range(0,len(c)):
                if kod==000+i:
                    print(c[i+1][0],"hesabınıza",int(c[i+1][2]),"TL'ye"," eklenmiştir")
                    kitap.append(c[i+1])
                    a = a + int(c[i+1][2])
            return a
        
        sorgu2=oneri()
        
        
        if devamlilik==0:
            yapilacaklarlistei=int(input("""Ne yapmak istiyorsunuz=
            Kitap kiralamak için 1
            ödeme yapmak için 2
            kiralanmış kitapları görmek için 3
            sepeti görmek için 4
            bakiyenizi görmek için 5
            bakiye yükleme için 6
            sepetten ürün çıkarmak için 7
            çıkış yapmak için 0ı tuşlayınız: \n"""))

        
        if yapilacaklarlistei==0:
            sorgu2.sorgu()
            sozlukkitap.append(odenmiskitap)
            gunsonukitap.setdefault(ad,odenmiskitap)
            gunsonupara.setdefault(ad,odenmispara)
            im.execute("UPDATE personel SET bakiye =? WHERE ad=? AND sifre=? ",(bakiye,ad,sifre))
            vt.commit()
            for b in range(0,int(len(kitap))):
                del kitap[0]
            devamkontrol=1
            break
            
         
        if yapilacaklarlistei==2:
            odemekontrol=str(input("Ödeme yapmak istediğinize emin misiniz?=(Y/N)\n"))
            if odemekontrol == ("Y") or odemekontrol==("y"):
                if int(bakiye)>=int(toplam):
                    print("Ödeme Başarılı")
                    for z in range(0,len(kitap)):
                        odenmispara = odenmispara + int(kitap[z][2])
                    for z in range(0,len(kitap)):
                        bakiye = bakiye - int(kitap[z][2])
                    for z in range(0,len(kitap)):
                        odenmiskitap.append(kitap[z][0])   
                    for z in range(0,len(kitap)):
                        del kitap[0]
                    print("kalan bakiyeniz=",bakiye)
                elif int(bakiye)<int(toplam):
                    print("yetersiz bakiye")
            elif odemekontrol == ("N") or odemekontrol==("n"):
                print("Ödeme Başarıyla İptal Edilmiştir.Ana menüye aktarılıyorsunuz. \n")
                
        if yapilacaklarlistei==3:
            print("Ödemiş olduğunuz kiralanmış kitaplarınız= \n",odenmiskitap)
                
        if yapilacaklarlistei==6:
            tutar=int(input("Ödemek İstediğiniz Miktarı giriniz=\n"))
            bakiye = bakiye + tutar
            print("Yükleme Başarılı")
            print("Mevcut Bakiyeniz=",bakiye,"Tl'dir")
        
        if yapilacaklarlistei==5:
            print("Şuanki mevcut Bakiyeniz=",bakiye,"TL'dir")
         
            
         
            
        if yapilacaklarlistei==4:
          toplam=0
          for a in range(0,len(kitap)):
              toplam = toplam + int(kitap[a][2])
          print("sepetinizdeki kitaplar şunlardır:\n")
          for c in range(0,len(kitap)):  
                print(kitap[c][0])
          print("toplam tutar=",toplam,"TL'dir.")
          
            
            
            
        if yapilacaklarlistei==1 or devamlilik==1 :
            turkontrol=int(input("""Hangi tür kitap kiralamak istersiniz=
            roman ise 1
            macera ise 2
            aksiyon ise 3
            masal ise 4
            ana menüye dönmek için 5'i tuşlayınız. \n"""))
            
            
            if turkontrol==1:
                for y in range(0,len(roman)):
                    print(roman[y])
                kod=int(input("kitabın kodunu giriniz=\n"))
                fiyat=kod1(roman,0)
                toplam=toplam+fiyat
                devamlilik=denetleme()
    
                
            if turkontrol==2:
                for y in range(0,len(macera)):
                    print(macera[y])
                kod=int(input("kitabın kodunu giriniz=\n"))
                fiyat=kod1(macera,0)
                toplam=toplam+fiyat
                devamlilik=denetleme()
                        
                        
            if turkontrol==3:
                for y in range(0,len(aksiyon)):
                    print(aksiyon[y])
                kod=int(input("kitabın kodunu giriniz=\n"))
                fiyat=kod1(aksiyon,0)
                toplam=toplam+fiyat
                devamlilik=denetleme()
                        
                        
            if turkontrol==4:
                for y in range(0,len(masal)):
                    print(masal[y])
                kod=int(input("kitabın kodunu giriniz=\n"))
                fiyat=kod1(masal,0)
                toplam=toplam+fiyat
                devamlilik=denetleme()
            if turkontrol==5:
                print("anamenüye dönülüyor.")
                devamlilik=0
        if yapilacaklarlistei==7:  
            try:
                if len(kitap)>0:
                    for f in range(0,len(kitap)):
                        print(f+1,"-",kitap[f][0],"-",kitap[f][2],"TL")
                    kaldırma=int(input("""sepetinizdeki kitaplar bunlardır kaldırmak istediğiniz kitabın yanındaki sayıyı tuşlayınız
ana menüye dönmek istiyorsanız 0'ı tuşlayınız.\n"""))
                    if kaldırma==0:
                        print("ana menüye dönülüyor")
                    if kaldırma!=0:
                        print(kitap[kaldırma-1][0],"sepetinizden kaldırılmıştır.")
                        kitap.pop(kaldırma-1)
                else:
                    print("sepetinizde kitap bulunmamaktadır ana menüye aktarılıyorsunuz...")
            except len(kitap)==0:
                print("Yazdığınız numarada bir kitap bulunmamaktadır ana menüye aktarılıyorsunuz...")
vt.close()