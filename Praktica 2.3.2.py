slovo = input('Введите слово с гласными буквами: ')
e=slovo.count('e') 
a=slovo.count('a') 
i=slovo.count('i') 
u=slovo.count('u') 
o=slovo.count('o') 
glassnye=e+a+i+u+o 
print("всего гласных",glassnye) 
print("всего согласных",len(slovo)-glassnye)  
if (e==0):
    print ("гласной e в слове False")
else:
    print("e=",e)
if (u==0):
    print ("гласной u в слове False")
else:
    print("u=",u)
if (o==0):
    print ("гласной o в слове False")
else:
    print("o=",o)
if (a==0):
    print ("гласной a в слове False")
else:
    print("a=",a)
if (i==0):
    print ("гласной i в слове False")
else:
    print("i=",i)