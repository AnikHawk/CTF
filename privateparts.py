
import string

d = 9440767265896423601
n = 16513720463601767803

FILE = open('netenc.hex', 'r')
c = FILE.read()
N = 16
c = c.replace('\n', '').replace('\r', '')
m = [hex(pow(int(c[i:i+N], 16), d, n)).rstrip("L") for i in range(0, len(c), N)]
DECRYPTED_ = string.join(m, '')
DECRYPTED_ = DECRYPTED_.replace("0x", "")


f = open('decrypted.hex', 'w')
f.write(DECRYPTED_)
f.close()