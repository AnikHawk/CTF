c = '80 080 050 40 010 70 70 110 30 60 040 090 70 080 30 060 060 10 010 20'.split(' ')
alphabet = "_abcdefghijklmnopqrstuvwxyz"

dct = {}
dct['00'] = '_'
for i in range(1,13):
    s0 = '0' + str((i)*10)
    dct[s0] = alphabet[i]

    s1 = str(i*10)
    dct[s1] = alphabet[i+12]

x = ''
for i in c: x += dct[i]

print(x)