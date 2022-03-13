def caesarcipher(word):
    listxc = []
    xres = ''
    for i in range(len(word)):
        xcode = ord(list(word.strip())[i])
        if word.isupper():
            xc = (xcode + 3 - 65) % 26 + 65
        else:
            xc = (xcode + 3 - 97) % 26 + 97
        listxc.append(chr(xc))
        xres = ''.join(listxc)
    print(xres)