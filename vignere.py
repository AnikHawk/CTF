cipher = 'vychxqxyrrrqhpcxxdqirwxqnujnvlvxdgackjrwxyksuglqtw'
plain = 'thesecretpasswordforthechallengepageisthekeyweused'
alphabet = "abcdefghijklmnopqrstuvwxyz"

a=[]
key = ''
for i,j in zip(cipher,plain):
    c = (ord(i) - ord(j) + 26)%26
    a.append(c)
    key += alphabet[c]
print(key)