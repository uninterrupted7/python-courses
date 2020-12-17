# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:15:39 2020

@author: Abdurrahim
"""
#section1
import math as mat
#import matplotlib as matp

var1 = 10  
var2 = 5

# %%
# section2

# consola bir seyler  yazdiriyorum...
#print(var1)
#print(var2)
print(var1+var2)


str1 = "hello world2 adasdasd adsadasd"

var3 = 10.0
print(str1)
pi =3.14
#%%

pi = mat.pi

print(pi)



d2r = pi/180

x = mat.sin(90*d2r)

y = mat.cos(0)

a_x = mat.asin(1)

print(a_x)

# %%


#enBuyuk = 4
#enBuyuk = 4

giris = input("Lutfen bir sayi giriniz :")  # cikisi her zaman  string ifadedir

giris = float(giris)
print(giris)

# %%

str_giris = input("bir kelime yaziniz :")


print(str_giris)
str_giris2 = input("bir kelime yaziniz :")

len(str_giris)  

# %%
fruits = ["apple", "banana", "cherry"]   #string array
for x in fruits:
  print(x)

for x in "banana":
    print(x)

for x in fruits:
    print(x)
    
    if x == "banana":        #conditions
        break               #döngüden çıkma


for x in fruits:
  if x == "banana":        
    continue                   #bunu dikkate alma
  print(x)


#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.



for x in range(6):
  print(x)

for x in range(1, 3):
  print(x)
  print(fruits[x])


for x in range(2, 30, 3):
    print(x)
    
    #%%
#içe içe for (nested loops)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x + " " + y)    
    
#%%

    
#for with else 
# program to display student's marks from record
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
    
    

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
#%%
import math as sin, pi
a=pi/2
b=0
n = 1
sum = 0
for x in range(0,a):
    print(x)
    y = mat.sin(x/0.1*3.14/180)
    print(y)
    sum = sum + y
    
    #%%

a = 2
b= 0
n = 5
toplam = 0
h = 1/ n
for x in range(0,40):
    y = mat.pow(x*0.05,2)*0.05
    toplam = toplam + y
    
#%%    
# take multiple inputs in array 
input_str_array = input().split() 
  
print("array:", input_str_array) 
  
# take multiple inputs in array 
input_int_array = [ int(x) for x in input().split()] 
  
print("array:", input_int_array)     
#%%

#if test expression:
#    statement(s)    


num = 5

if num == 5:
    print("sayi 6 dan küçüktür")
num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
#%%

a = 5
b = 4

if a>b:
    pass
elif a==5:
    print("B")
else:
    print("A")
    
    #%%
    
import random as rnd

a = rnd.randint(1,2)   
b = rnd.randint(-5,1)   
c = rnd.randint(-10,-1)


rnd.randrange(0,101,15)
rnd.randrange(0,101)

numbers=[12,23,45,67,65,43]
rnd.shuffle(numbers) # dizi elemanlarını random dağıtmak

#%%

i = 1

while i<=6:
    print(i)
    i += 1
    
    #%%
    
a = rnd.randint(-5,5)
b = rnd.randint(-5,5)

carp = a*b

if a*b > 0:
    if a > 0:
        print("hem a hem b 0 dan büyüktür")
    else:
        print("a ve b 0 dan küçüktür")

elif a*b == 0:
    if a == 0:
        print("a 0'a eşittir")
    else:
        print("b 0'a eşittir")
     

else:
    if a>0:
        print("a 0 dan büyük, b 0 dan küçüktür")
    else:
        print("a 0 dan küçük, b 0 dan büyüktür")

#%%

pswrd = "123"
sifre=""
while(sifre != pswrd):
    sifre = input("sifre giriniz :")
     
else:
    print("doğru girdiniz")
    
    #%%
    
lower = "abcdefgh"
upper = "ABCDEFGH"
number = "12345678"
symbols = "{}[](),*/"

hepsi = lower + upper + number + symbols


length = 8

psswrd = "".join(rnd.sample(hepsi,length))

deneme = ""

while deneme != psswrd:
    deneme = input("sifre giriniz :")
    

    
else:
    print("doğru sifre")    
  #%%  
    