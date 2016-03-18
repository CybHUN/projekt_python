#Hello World program -egyszerü szöveg kiírtás, minden programozási nyelv első programja
print("Hello World")
#Köszönő program - egy változót bekérünk és vele dolgozunk
nev = input("Add meg a neved:")
print("Udvozollek,"+nev)

a=input('a oldal hossza:')
#type(a)
b=input("b oldal hossza:")
#type(b)

t=int(a)*int(b)
print("A négyzet területe:"+str(t))
k=2*(int(a)+int(b))
print("A négyzet kerülete:"+str(k))

szam=input('Adjon meg egy számot:')
if int(szam)>0 :
    print('a szám pozitív')
elif int(szam)<0 :
    print('a szám negatív')