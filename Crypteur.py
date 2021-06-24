import convertion
import test1

def XOR(A,B):
    result = ""
    for i in range(0,len(A)):
        if A[i] == "0" and B[i] == "1":
            result += "1"
        elif A[i] == "1" and B[i] == "0":
            result += "1"
        else :
            result += "0"
    return result
def XAND(A,B):
    result = ""
    for i in range(0,len(A)):
        if A[i] == "0" and B[i] == "1":
            result += "0"
        elif A[i] == "1" and B[i] == "0":
            result += "0"
        else :
            result += "1"
    return result
def rotate_left(bits,s):
    for i in range(s):
        bits = bits[1:] + bits[0]
    return bits

def rotate_right(bits,s):
    for i in range(s):
        bits = bits[-1] + bits[:-1]
    return bits

def crypt(ls_k,group_ls):
    t = 0
    tour_total = 0
    for group in group_ls: 
        if t > len(ls_k)-1:
            t = 0
        octet = []
        for i in range(0,4):
            octet.append(group[i*8:(i+1)*8])
        octet[0] = XAND(octet[0],convertion.number_to_octet(ls_k[t]))
        octet[1] = rotate_left(octet[1],(ls_k[t]**2)%8)
        octet[2] = XAND(octet[2],convertion.number_to_octet((ls_k[t]**3)%255))
        octet[0] = rotate_left(octet[0],ls_k[t]**3%8)
        octet[1] = XOR(octet[1],convertion.number_to_octet(ls_k[t]))
        octet[2] = XOR(octet[2],convertion.number_to_octet(ls_k[t]**2%255))
        octet[3] = XOR(octet[3],convertion.number_to_octet(ls_k[t]))
        final = "".join(octet)
        group_ls[tour_total] = final
        t += 1
        tour_total += 1
    binary = "".join(group_ls)
    hexa = convertion.binary_to_hexa(binary).lower()
    test1.create_(name,hexa)
    print('-------\nDONE !\n-------')

def decrypt(ls_k,group_ls):
    t = 0
    tour_total = 0
    for group in group_ls: 
        if t > len(ls_k)-1:
            t = 0
        octet = []
        for i in range(0,4):
            octet.append(group[i*8:(i+1)*8])
        octet[3] = XOR(octet[3],convertion.number_to_octet(ls_k[t]))
        octet[2] = XOR(octet[2],convertion.number_to_octet(ls_k[t]**2%255))
        octet[1] = XOR(octet[1],convertion.number_to_octet(ls_k[t]))
        octet[0] = rotate_right(octet[0],ls_k[t]**3%8)
        octet[2] = XAND(octet[2],convertion.number_to_octet((ls_k[t]**3)%255))
        octet[1] = rotate_right(octet[1],(ls_k[t]**2)%8)
        octet[0] = XAND(octet[0],convertion.number_to_octet(ls_k[t]))
        final = "".join(octet)
        group_ls[tour_total] = final
        t += 1
        tour_total += 1
    binary = "".join(group_ls)
    hexa = convertion.binary_to_hexa(binary).lower()
    test1.create_(name,hexa)
    print('-------\nDONE !\n-------')

while True:
    name = input('Name -> ')
    print("Loading doc ...",end='\r')
    hexa = test1.open_(name)

    #Convertir en binaire
    binary = convertion.hexa_to_binary(hexa)
    
    #Padding at the end until %32 == 0
    while len(binary)%32 != 0:
        binary += "0"
    
    #Coupe en groupe de 32 bits:
    group_ls = []
    p = 0
    b = ""
    for i in binary:
        if p%32 == 0 :
            group_ls.append(b)
            b = ""
        b += str(i)
        p += 1
    del group_ls[0]

    choice = input("[C]rypt or [D]ecrypt : ").lower()

    key = input('Key : ')
    ls_k = []
    for i in key :
        ls_k.append(ord(i))
    if ls_k == []:
        ls_k.append(5)
    
    print("Treatment ...",end='\r')

    if choice == "c":
        crypt(ls_k,group_ls)
    else :
        decrypt(ls_k,group_ls)