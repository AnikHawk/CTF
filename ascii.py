cipher = '8i4 q5tt/>/>1se g1s 8i4 di5mm4oa4 t284 2t; 4mju4 ';
ascii = []
plain = ''
for c in cipher:
    if c is not ' ':
        ascii.append(ord(c)-1)
        plain += (chr(ord(c)-1))
    else:
        plain += ' '

print(ascii)
print(plain)



enc = "849091049091019091129099790911590911590911990911190911490910090910"
enc += "59091159091009091019099990999909111909110909118909101909114909116"

codes = [int(t, 10) for t in enc.split("909")]
chars = [chr(t) for t in codes]
msg = "".join(chars)
print(msg)


a = 'kvfifiihloyfkkyokoxkkhcoeqjtkjhzvagokhszksophqojhzeamcoeqjtkkvfikoxkjhzvagokhpfmckvopfqiktaqkszkuvakfalkaydfmnhpuvomjhzaqoqoacfmnkvfijhzayqoacjcfckvaktaqkamclzevlhqoihyokichkvoioehmctaqkfkilzevoaifoqsoeaziojhzvagoayqoacjkvovaqcoqtaqklzwipyycofjeygvpefcelqz'
print(len(a))
n = '40204060402070304020306030307040403040204030504030401020702040303070403070304040304040204020306040304060703040703060403080210'
n = n.replace('0','')
n = '424642734236337443424354341272433743734434424236434673473643821'
print(len(n))

print(381/3)