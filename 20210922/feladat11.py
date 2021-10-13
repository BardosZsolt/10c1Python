from math import *


'''Írj programot, mely beolvas két pozitív egész számot, és kiírja a számtani és mértani 
közepüket! A gyökvonáshoz használd a beépített gyökfüggvényt!'''
# beolvasunk 2 számot
a=int(input("kérek egy számot! a=")
b=int(input("Kérek egy másik számot! b=")
# számtani közép
szamtanikozep=(a+b)/2
print("A számtani közepük",szamtanikozep)
# mértani közép a szorzatuk négyzetgyöke két szám esetén
mertanikozep=sqrt(a*b)
print("A mértani közepük",mertanikozep)