#THIS IS MY FIRST TEST, IT WORKS ONLY ON MAC OS (the real code is nammed main.py
"""
Test d'ouverture d'un fichier Unicode (pas utf8) avec python
xxd : ouvre le fichier en hex
"""
def hexa_to_binary(hexa):
    hexa = hexa.upper()
    l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    finalbit = ""
    for i in str(hexa):
        nb = 0
        t = 0
        for j in l:
            if j == i:
                nb = t
            t += 1
        bit = ""
        if nb-8 >= 0 : bit += "1"; nb = nb - 8
        else : bit += "0"
        if nb-4 >= 0 : bit += "1"; nb = nb - 4
        else : bit += "0"
        if nb-2 >= 0 : bit += "1"; nb = nb - 2
        else : bit += "0"
        if nb-1 >= 0 : bit += "1"; nb = nb - 1
        else : bit += "0"
        finalbit += bit
    while len(finalbit) < 8:
        finalbit = "0" + finalbit
    return finalbit

def bin_to_hex(bits):
    final = ""
    p = 0
    for i in range(int(len(bits)/4)):
        b = bits[p:p+4]
        result = 0
        t = 0
        for i in str(b)[::-1]:
            result += int(i) * (2**t)
            t += 1
        final += list("0123456789ABCDEF")[result]
        p += 4
    return final

def rotate_left(bits,s):
    for i in range(s):
        bits = bits[1:] + bits[0]
    return bits

def rotate_right(bits,s):
    for i in range(s):
        bits = bits[-1] + bits[:-1]
    return bits

from os import popen
import os
name = input("name -> ")
cmd=popen(f"xxd -p {name}")
contenu = cmd.read().split('\n')
ls_hexa = []
for i in contenu :
    if i != "" :
        ls_hexa.append(i)

ls_binary = []

for hexa in ls_hexa:
    p = 0
    l = []
    for t in range(0,int(len(hexa)/2)):
        mot = hexa[p:p+2]
        l.append(hexa_to_binary(mot))
        p += 2
    ls_binary.append("".join(l))

c = input("[C]rypt or [D]ecrypt : ")
k = input("Key :")
ls_k = [2]
for i in k :
    ls_k.append(ord(i))
print(ls_k)
total = len(ls_binary)
print(total)
if c.lower() == "c":
    t = 0
    p = 0
    tt = 0
    ls_finalbit = []
    for i in ls_binary:
        ls_finalbit.append(rotate_left(i,p))
        p = (p + int(ls_k[t])) % int(ls_k[0])
        t += 1
        if t > len(ls_k)-1:
            t = 0
        tt += 1
        print(str(tt*100/total)[:4],"%",p,end='\r')
else :
    t = 0
    p = 0
    tt = 0
    ls_finalbit = []
    for i in ls_binary:
        ls_finalbit.append(rotate_right(i,p))
        p = (p + int(ls_k[t])) % int(ls_k[0])
        t += 1
        if t > len(ls_k)-1:
            t = 0
        tt += 1
        print(str(tt*100/total)[:4],"%",p,end='\r')

final_file = []
for binary in ls_finalbit:
    final_file.append(bin_to_hex(binary).lower())

file = open("1.txt",'w')
file.write("\n".join(final_file))
file.close()
os.system(f"xxd -p -r 1.txt {name}")
