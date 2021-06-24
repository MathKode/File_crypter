"""
A file write by : BiMathAx STUDIO
Using to convert all type of data in another type of data
"""

def hexa_to_binary(hexa):
    #Input : 2D4F48 or 2d4f48
    #Output : 001011010100111101001000
    """
                2   -   D   -   4   -   F   -   4   -   8
                |       |       |       |       |       |
    Position :  2       13      4       15      4       8
                |       |       |       |       |       |
    -> SI NB - 8 >= 0 ALORS bit + 1 SINON bit + 0
                |       |       |       |       |       |
                2-8=-6  13-8=5  4-8=-4  15-8=7  4-8=-4  8-8=0
                0       1       0       1       0       1
                |       |       |       |       |       |
    -> SI NB - 4 >= 0 ALORS bit + 1 SINON bit + 0
                |       |       |       |       |       |
                2-4=-2  5-4=1   4-4=0   7-4=3   4-4=0   1-4=-3
                0       1       1       1       1       0
                |       |       |       |       |       |
    -> SI NB - 2 >= 0 ALORS bit + 1 SINON bit + 0
                |       |       |       |       |       |
                2-2=0   1-2=-1  0-2=-2  3-2=1   0-2=-2  1-2=-1
                1       0       0       1       0       0
                |       |       |       |       |       |
    -> SI NB - 1 >= 0 ALORS bit + 1 SINON bit + 0
                |       |       |       |       |       |
                0-1=-1  1-1=0   0-1=-1  1-1=0   0-1=-1  1-1=-1
                0       1       0       1       0       0
                |       |       |       |       |       |
    Regroupe :  0010    1101    0100    1111    0100    1000
    """
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
    return finalbit

def binary_to_hexa(binary):
    #Input : 111101001000
    #Output : F48
    """
    1111    -    0100    -    1000
    |            |            ’---> 1*8 + 0*4 + 0*2 + 0*1 = 8
    |            ’----------------> 0*8 + 1*4 + 0*2 + 0*1 = 4
    ‘-----------------------------> 1*8 + 1*4 + 1*2 + 1*1 = 15
    Convertit en hexa :
    15 -> F
    4 -> 4
    8 -> 8
    Result = F48
    """
    l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    #If hex code is 101 -> 0101
    while len(binary)%4 != 0:
        binary = "0" + binary
    p=0
    finalhexa = ""
    for i in range(int(len(binary)/4)):
        bloc = binary[p:p+4]
        r = 0
        t = 8
        for i in bloc:
            r += int(i)*t
            t = int(t/2)
        finalhexa += l[r]
        p += 4
    return finalhexa

def number_to_binary(number):
    #Input : 13
    #Output : 1101
    """
            13%2 -> 1
    13//2 = 6
            6%2  -> 0
    6//2  = 3
            3%2  -> 1
    3//2  = 1
            1%2  -> 1
    1//2  = 0
            STOP
    1011 -> reverse -> 1101
    """
    r = ""
    while number != 0:r += str(number%2);number = int(number//2)
    r = r[::-1]
    return r

def binary_to_number(binary):
    #Input : 1011
    #Output : 11
    """
    1 0 1 1
    | | | 1*2^0 
    | | 1*2^1
    | 0*2^2
    1*2^3

    2^3+2^1+2^0 = 8+2+1 = 11
    """
    r = 0;t = 0
    for i in str(binary)[::-1]:
        r += int(i)*(2**t)
        t += 1
    return r

def number_to_octet(number):
    #Input : 34
    #Output : 00100010
    binary = str(number_to_binary(number))
    while len(binary)%8 != 0:
        binary = "0" + binary
    return binary

def number_to_hexa(number):
    #Input : 423
    #Output : 1A7
    binary = number_to_binary(number)
    hexa = binary_to_hexa(binary)
    return hexa

#print(hexa_to_binary("2D4F48"))
#print(binary_to_hexa("1110010101011"))
#print(number_to_binary(18))
#print(binary_to_number(10011))
#print(number_to_hexa(4167262))