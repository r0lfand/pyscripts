import hashlib

target = 'd834'
candidate = 0
while True:
    plaintext = str(candidate)
    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()
    if hash[-4:] == target:
        print('plaintext:"' + plaintext + '", md5:' + hash)
        break
    candidate = candidate + 1