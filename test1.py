"""
Code qui teste la lecture d'un fichier en binaire 
et l'écriture d'un fichier à partir du binaire
"""
import binascii
def open_(name):
    #Output : b2b3de2076582858505d909a4989422ff3af...
    file = open(name,'rb')
    content = file.read()
    file.close()
    hexa = str(binascii.hexlify(content))[2:-1]
    return hexa

def create_(name,hexa):
    #Input : 89504e470d0a1a0
    hexa = binascii.unhexlify(hexa) #Transform into : b'\x89PNG\r\n\x1a\n\x00\x00\
    file = open(name,'wb')
    file.write(hexa)
    file.close()

if __name__ == "__main__":
    hexa = open_("3.png")
    create_("3vr2.png",hexa)