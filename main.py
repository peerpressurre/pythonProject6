import random
pas = ''
for x in range(8):
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
step = 4
message = pas
cipher = ''
for i in message:
    mesto = alfabet.find(i)
    new_mesto = mesto + step
    if i in alfabet:
        cipher += alfabet[new_mesto]
    else:
        cipher += i
print(cipher)
