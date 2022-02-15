import argparse
def displace_encrypt(letter, step):
    if letter.islower():
        shift = 97
    else:
        shift = 65
    return chr((ord(letter) + step - shift) % 26 + shift)


def displace_decrypt(letter, step):
    if letter.islower():
        shift = 97
    else:
        shift = 65
    return chr((ord(letter) - step - shift) % 26 + shift)


def encrypt(our_text):
    encrypted = []
    key_index = -1
    i = 0
    for letter in our_text:
        if key_index == -1:
            key_letter = d['a']
        else:
            key_letter = d[encrypted[key_index]]
        if letter in d:
            encrypted.append(displace_encrypt(letter, key_letter))
            key_index = key_index + i + 1
            i = 0
        else:
            encrypted.append(letter)
            i += 1

    return ''.join(encrypted)


def decrypt(our_text):
    decrypted = []
    key_index = -1
    i = 0
    for letter in our_text:
        if key_index == -1:
            key_letter = d['a']
        else:
            key_letter = d[our_text[key_index]]
        if letter in d:
            decrypted.append(displace_decrypt(letter, key_letter))
            key_index = key_index + i + 1
            i = 0
        else:
            decrypted.append(letter)
            i += 1

    return ''.join(decrypted)


d = {}
iter = 0
for i in range(65, 91):
    d[chr(i)] = iter
    iter += 1
iter = 0
for i in range(97, 123):
    d[chr(i)] = iter
    iter += 1

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str)
parser.add_argument('-er', '--en_result', type=str)
parser.add_argument('-dr', '--de_result', type=str)
args = parser.parse_args()

with open(args.path, 'r', encoding="UTF-8") as fr:
    with open(args.en_result, 'w', encoding="UTF-8") as fw:
        for line in fr:
            fw.write(encrypt(line))

with open(args.en_result, 'r', encoding="UTF-8") as fr:
    with open(args.de_result, 'w', encoding="UTF-8") as fw:
        for line in fr:
            fw.write(decrypt(line))


