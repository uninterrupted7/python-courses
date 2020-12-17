# -*- coding: utf-8 -*-

import math as mth
import random as rnd

import cv2 as cv
#import matplotlib as mp
#part1
a = 5
b = 4  # tam sayi

kel1 = "ilk giriş cümlesi"  # kelime (string)

c = 1.89  # float degisken

#derse basliyorum

#  part 2
#%%

print(b)
print(a)
print(kel1 + kelime)

print(a*b)

#%%

#sin_deger = mth.sin(90*mth.pi/180)


val = input("bir deger giriniz :")  #donus hep string (kelime)

#%%

#karsilastirmalar
say1 = 1
say2 = 5
say3 = 7

if say1 < say2:
    print("1.sayi 2.sayidan büyüktür")

elif say3 > say2: 
    print("sayi 3 büyüktür")
    
else:
    print("2.sayi 1.sayidan büyüktür")
        
    #%%

say1 = 4
say2 = 4


if say1 != say2:
    print("iki sayi farklidir") 
else:
    print("iki sayi esittri")
   
    
   
if say1 == say2:

    print("asdasd")    


if say1 == say2: print("kisa if")

print("x") if say1 != say2 else print("y")
#%%
say1 = 4
say2 = 4

a = 4
b = 7
c = 5
if say1 == say2 and a < b:
    print("1.bölüm")


if say1 == say2 and a < b and  c > a:
    print("2.bölüm")

else:
    print("3.bölüm")


if say1 == say2 or a > b:
    print("4.bölüm")

#%%

# f(x) = ax^2 + bx + c

a = 1
b = 2
c = 1

dis = (b*b) - (4*a*c) 
print(dis)
if dis >0:
    print("iki farkli reel kök var")

elif dis == 0:
    print("cakisik iki kök")
    
else:
    print("iki tane imajiner kök var")    

#%%

a = rnd.randint(-5,5)
b = rnd.randint(-5,5)

carp = a*b

if a*b > 0:
    if a > 0:
        print("iki sayida pozitiftir.")
    else:
        print("iki sayi negatiftir.")

elif a*b == 0:
    print("iki sayidan biri 0'dır")

else:
    if a > 0:
        print("b negatif, a pozitif")
    else:
        print("a negatif, b pozitif")
         
#%%

# loop (donguler)

meyveler = ["elma", "armut", "muz","kiraz"]

for x in meyveler:
    print(x)

for x in "elmaasdasd":
    print(x)


for x in range(-5,5):
    print(x)
    #print(meyveler[x-1])
    
    #%%
    
for x in range(0,100,2):   #basamak degeri
    print(x)

#%%

for x in meyveler:
    print(x)
    
    if x == "elma":
        break
    
    print(x)
     #%% nested loop 
    
sifat = ["kirmizi", "yesil", "mavi", "mor"]   
meyveler = ["elma", "armut", "muz","kiraz"] 

for x in sifat:
    for y in meyveler:
        print(x + " " + y)
        
        
        

#%%

std_name = "ali"

isimler = ["veli", "mehmet", "berkay"] 

for student in isimler:
    if std_name == student:
        print("ali bir ogrencidir.")
        
else:
    print("ali ogrenci degil") 


#%%

#integral alma  f(x) = x^2 fonkisyonun integrali - 0-2 aralığında

a = 2
b = 0

n = 80

h = 2 / n

sum = 0
for x in range(0,n):
    y = mth.pow(x*h,2)*h
    sum = sum + y
   
    
print(sum)    
 
#%%   

     
    
