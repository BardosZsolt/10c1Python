'''Írj programot, ami beolvassa a háromszög oldalainak hosszát, és megmondja, hogy ilyen oldalakkal szerkeszthető-e háromszög! háromszög akkor szerkezthető,ha bármely két oldal összege nagyobb a harmadiknál'''
a=float(input("Kérem a háromszög a oldalát a="))
b=float(input("Kérem a háromszög b oldalát b="))
c=float(input("Kérem a háromszög c oldalát c="))
legnagyobb=max(a,b,c)
if a==legnagyobb:
    if a<b+c:
        print("A háromszög szerkezhető.")
    else:
        print("A háromszög nem szerkezhető.")
if b==legnagyobb:
    if b<a+c:
        print("A háromszög szerkezhető.")
    else:
        print("A háromszög nem szerkezhető.")
if c==legnagyobb:
    if c<b+a:
        print("A háromszög szerkezhető.")
    else:
        print("A háromszög nem szerkezhető.")
print("Másik megoldás")
if a==legnagyobb:
    if a<b+c:
        print("A háromszög szerkezhető.")
    else:
        print("A háromszög nem szerkezhető.")
else: b==legnagyobb
if b==legnagyobb:
    if b<a+c:
        print("A háromszög szerkezhető.")
    else:
        print("A háromszög nem szerkezhető.")
else:
    if c<b+a:
        print("A háromszög szerkezhető.")
    else:
        print("A háromszög nem szerkezhető.")
szamok=[]
szamok.append(a)
szamok.append(b)
szamok.append(c)
print(szamok)
szamok.sort()
print(szamok)
if szamok[2]<szamok[0]+szamok[1]:
    print("Szerkezthető")
else:
    print("nem szerkezthtő")




