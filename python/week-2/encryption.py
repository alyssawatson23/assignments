# 2.7
def encrypt(text):
    charList = list(text)
    newCharList = []
    encrypted = ""
    for x in charList:
        if(x.isalpha()):
            newCharList.append(chr(ord(x) + 5))
        else:
            newCharList.append(x)
    for c in newCharList:
        encrypted += c
    print(encrypted)
    decrypt(encrypted)


def decrypt(text):
    charList = list(text)
    newCharList = []
    decrypted = ""
    for x in charList:
        if(x.isalpha()):
            newCharList.append(chr(ord(x) - 5))
        else:
            newCharList.append(x)
    for c in newCharList:
        decrypted += c
    print(decrypted)


encrypt("hello world!")
