import hashlib
import sys

phrase = sys.argv[1]

hashp = str(hashlib.sha512(phrase.encode()).hexdigest())[:32]
print(str(hashp))
passw = '' 
for i in range(0, len(hashp), 2):
    hex_char = hashp[i:i+2]
    dec_char = (int(hex_char,16) % 126)
    
    
    if dec_char < 33:
        dec_char += 33
    char = chr(dec_char)
    print(dec_char+8, hex_char, dec_char, char, sep='\n')
    passw += char

passw = passw + '9oL.'


print('Your password\n'+passw)



