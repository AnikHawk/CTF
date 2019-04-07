cipher = 'B8 9B 8C E0 89 9F 9D 98 8C 89 91 91 8E 9C E0 97 8D E0 BD 91 AB 92 8C'.split(' ')

p = ''
for c in cipher:
    ascii = 256 - int(c,16)
    p += chr(ascii)

print(p)

