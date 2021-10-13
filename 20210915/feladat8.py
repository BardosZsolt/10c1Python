#8


a=int(input("Kérek egy számot! a="))
b=int(input("Kérek egy másik számot! b="))
if a>b:
    print(a,'nagyobb,mint',b)
if a<b:
    print('b,nagyobb,mint' ,a)
if a==b:
    print('A két szám egyenlő.')
#ha feltétel:
#  utasítás
# egyirányú elágazás
if a>b:
    print('a,nagyobb,mint',a)
elif b>a:
    print('b,nagyobb,mint',a)
else:
    print('A két szám egyenlő.')
# több irányú elágazás

if a!=b:
    print(max(a,b),'nagyobb,mint',min(a,b)




