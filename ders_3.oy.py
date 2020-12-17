# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:16:37 2020

@author: Abdurrahim
"""

#while karsilastirma:
#    yapilacaklar
 
import random as rnd

i = 6

while i>10:
    print("dongu calisiyor")
    i=i-1

else:
    print("dongu bitti")
    
    #%%
    
i = 6

while i>1:
    print("dongu calisiyor")
    
    i=i-1
    if i == 4:
        continue
    print(i)
    

#%%


lower = "abcdefgh"
upper = "ABCDEFGH"
sayilar = "12345678"
sembol = "^+%&/(){}"


toplam = lower+upper+sayilar+sembol

    
uzunluk = 9

sifre = "".join(rnd.sample(toplam, uzunluk))
print(sifre)

sonuc = ""

while sonuc != sifre:
    sonuc = input("bir sifre girininz :")
    
    
else:
    print("giris basarili")    

#%%



def ilk_fonksiyon(x):
    
    return x*x + 2*x + 1 


#sonuc = ilk_fonksiyon(5)
  
sonuc = ilk_fonksiyon(5)
#print(ilk_fonksiyon(5)+4)

#%%

def parametresiz():
    print("fonksiyon calisiyor")
    a = 5
    b = 3
    c = 4
    d = [a,b,c]
    return d

sonuc = parametresiz()   
    

#%%

def topla(x,y):
    print("sonuc",x+y)
    return x+y

def cikar(x,y):
    print("sonuc",x-y)
    return x-y

def carp(x,y):
    print("sonuc",x*y)
    return x*y

def bol(x,y):
    print("sonuc",x/y)
    return x/y


print("İslemler...")
print("1- topla")        
print("2- cikar")
print("3- carp")
print("4- bol")  

while True:
    
    secenek = input("Bir islem seciniz(1/2/3/4) :")
    sayi1 = input("birinci sayi :")
    sayi1 = int(sayi1)
    
    sayi2 = input("ikinci sayi :")
    sayi2 = int(sayi2)
    
    if secenek == '1':
        topla(sayi1,sayi2)
    if secenek == '2':
        cikar(sayi1,sayi2)
    if secenek =='3':
        carp(sayi1,sayi2)
    if secenek == '4':
        bol(sayi1,sayi2)
        
#%%       
        
    
dizi = [1,2,3,4]

def carpma(x):
    
    for i in range(0,len(x)):
        x[i] = x[i] *5
        
    
    return x


sonuc = carpma(dizi)

#%%
#recursive
def faktoriyel(x):

    if x == 1:
        return 1
    
    else:
        return(x * faktoriyel(x-1))
    


sonuc = faktoriyel(20)    
        
  #%%


fonk = lambda x: x*x + 2*x + 1

sonuc = fonk(5)

#%%
#class (object oriented)

class calisan:
    
    zam = 0.8
    
    def __init__(self, isim, soyisim, maas):   #ilk calisan fonksiyon
        
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        #self.boy = 1.8
        self.email = isim+soyisim+"@123.com"
        
    def alisimsoyisim(self):
        return self.isim + " " + self.soyisim
    
    def zam_yap(self):
        self.maas = self.maas + self.maas*0.8
        
        
isci1 = calisan("ali","yilmaz",100)   
isci2 = calisan("mehmet", "özer",200)
isci3 = calisan("ece","uner",300)
isci4 = calisan("ayse", "hatice",400)
    
isci2.zam_yap()
#rint(isci1.alisimsoyisim())
#print(isci1.zam_yap())


max_maas = 0

calisan_dizi = [isci1,isci2,isci3,isci4]

for calisan_kisi in calisan_dizi:
    print(calisan_kisi.maas)
    if calisan_kisi.maas > max_maas:
        max_maas = calisan_kisi.maas
        print(calisan_kisi.email)
        
        
        
print(max_maas)        
        
        
    

#%%

class ogrenci:
    
    def __init__(self,isim,notu):
        self.isim = isim
        self.notu = notu

    def harfNotu(self):
        if self.notu >= 90:
            return 'AA'
        elif self.notu >=80 and self.notu <90:
            return 'BB'
        elif self.notu >=70 and self.notu <80:
            return 'CC'
        else:
            return 'DD'

ogr1 =ogrenci("ali",90)
ogr2 =ogrenci("ali",80)
ogr3 =ogrenci("ali",70)
ogr4 =ogrenci("ali",60)
ogr5 =ogrenci("ali",65)

print("adasd")


#%%  

x = 3232323







