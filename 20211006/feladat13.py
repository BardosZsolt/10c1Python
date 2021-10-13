# 13.feladat
'''
for i in range(1,17):
    print(pow(2,i), end=" ")
print()
for i in range(1,17):
    print("2 a(z)" ,i,"hatványon:", pow(2,i))
print()
'''


# 17.feladat
a=int(input("Kérek egy pozitív egész számot! a="))
osszeg=0
for i in range(1,a+1):
    if a%i==0:
        osszeg+=i #osszeg=osszeg+i
print("A(z)", a,"osztóinak összege",osszeg)


