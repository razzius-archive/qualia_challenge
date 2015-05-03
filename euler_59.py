from __future__ import division

import string


LETTERS = string.ascii_lowercase

RELATIVE_ENGLISH_FREQUENCIES = {
    'A': .08167,
    'B': .01492,
    'C': .02782,
    'D': .04253,
    'E': .12702,
    'F': .02228,
    'G': .0201,
    'H': .06094,
    'I': .06996,
    'J': .00153,
    'K': .00772,
    'L': .04025,
    'M': .02406,
    'N': .0674,
    'O': .07507,
    'P': .01929,
    'Q': .00095,
    'R': .05987,
    'S': .06327,
    'T': .09056,
    'U': .0275,
    'V': .00978,
    'W': .02360,
    'X': .00150,
    'Y': .01974,
    'Z': .00074,
}

with open('p059_cipher.txt') as f:
    ciphertext = f.read()


codes = map(int, ciphertext.strip().split(','))


def shift_char(char, index):
    return chr(char ^ index)

def shift(s, i):
    """Shift a string s by i characters."""
    out = []
    for c in s:
        out.append(shift_char(c, i))

    return ''.join(out)


def get_counts(text):
    """Returns the counts of english letters in order."""
    out = {}
    for c in string.ascii_uppercase:
        out[c] = text.count(c)

    return out.values()


def chi_squared(a, b):
    result = 0
    for observed, expected in zip(a, b):
        result += ((observed - expected) ** 2) / expected
    return result

def argmin(l):
    return l.index(min(l))

def get_shift(col):
    ratios = []
    for i in range(255):
        text = shift(col, i)
        count_ratios = [c / len(text) for c in get_counts(text)]
        ratios.append(chi_squared(count_ratios, RELATIVE_ENGLISH_FREQUENCIES.values()))

    # return the lowest chi-squared value
    return argmin(ratios)


shifts = []
for i in range(3):
    column = codes[i::3]
    shifts.append(chr(get_shift(column)))


def get_plaintext(ciphertext, key):
    index = 0
    output = []

    for c in ciphertext:
        new_code = c ^ ord(key[index])
        index = (index + 1) % len(key)
        output.append(chr(new_code))

    return ''.join(output)

print(get_plaintext(codes, ''.join(shifts)))

# the answer the Euler project was looking for
print(sum(ord(k) for k in shifts))

