for i in range(12):     # 0-tól 11-ig írja ki
    print(i, end=" ")
print()
for i in range(3,12):   # 3 tól 11-ig írja ki
    print(i, end=" ")
print()
for i in range(3,12,2): # 3-tól 11-ig írja ki 2-vel növekedve
    print(i, end=" ")
print()


# másképp
# 0-tól 11-ig írja ki
i=0
while i<12: #i<=11
    print(i, end=" ")
    i=i+1 #i=i+1
print()

# 3-tól 11-ig írja ki
j=3
while j<12:
    print(j, end=" ")
    j=j+1
print()
# 3-tól 11-ig írja ki 2-vel növekedve
cv=3
while cv<12:
    print(cv, end=" ")
    cv=cv+2
print()

# while feltétel:
# utasítások
# előltesztelős ciklus
# ha van ciklusvátozó, akkor a ciklusmagban(utasítások) változtatni kell