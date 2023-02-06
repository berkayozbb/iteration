#!İTERASYON YÖNTEMİ DENKLEM ÇÖZME
a=float(input("ax2+bx+c=0 denklemindeki a katsayısı : ")) 
b=float(input("ax2+bx+c=0 denklemindeki b katsayısı : ")) 
c=float(input("ax2+bx+c=0 denklemindeki c sabitsayısı : "))
x=0
solveCheck=False
while solveCheck==False:
    denklem=a*(x**2)+b*(x)+c
    if denklem-0<=0.0001:
        solveCheck=True
        print(f"Denklemi 0'a eşitleyen değer : {round(x)} ")
    else:
        x=((-c)-a*(x**2))/b