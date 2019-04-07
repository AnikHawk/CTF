
cipher = "qpb asc qcqgaoq bad 1 jao a maeag aa".replace(' ', '')
plain = ''
for i in range(0, len(cipher), 2):
    front, back = ord(cipher[i]) , ord(cipher[i + 1])
    print(front, back)
    temp = chr((front & 0b11110000) + (back & 0b00001111))
    plain += temp

print(plain)