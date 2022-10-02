import random
pas = ''
for x in range(8):
    pas = pas + random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
step = 4
message = pas
cipher = ''
for i in message:
    place = alfabet.find(i)
    new_place = place + step
    if i in alfabet:
        cipher += alfabet[new_place]
    else:
        cipher += i
print('Cipher: Cezar\'s')
print(f'Your password is:',cipher)