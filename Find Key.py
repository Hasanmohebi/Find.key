
import string
import collections



ALPHABET_SIZE = 26

def count_chars(ciphertext, key_length, index):
    count = collections.Counter()
    for i, c in enumerate(ciphertext):
        if i % key_length == index:
            count[c] += 1
    return count



def count_unique_chars(ciphertext, key_length):
    if not ciphertext:
        return 0
    count = collections.Counter()
    for i, c in enumerate(ciphertext):
        if i % key_length == 0:
            count[c] += 1
    return len(count)

 

 

def index_of_coincidence (text):
    fi = collections.Counter(text)
    N = len(text)
    if N == 0:
        return 0
    ic = sum(n*(n-1) for n in fi.values()) / (N*(N-1))
    return ic

def find_key_length(ciphertext, max_key_length=16):
    best_ic = 0
    best_kl = 0
    for kl in range(1, max_key_length+1):
        ics = []
        for i in range(kl):
            subtext = ''
            ctr = 0
            for j in range(i, len(ciphertext), kl):
                subtext += ciphertext[j]
                ctr += 1
            ic = index_of_coincidence(subtext)
            if ic == 0:
                continue
            ics.append(ic)
        if not ics:
            continue
        avg_ic = sum(ics) / len(ics)
        if avg_ic > best_ic:
            best_ic = avg_ic
            best_kl = kl
    return best_kl

def find_key(ciphertext, key_length):
    key = ''
    for i in range(key_length):
        count = count_chars(ciphertext, key_length, i)
        sorted_items = sorted(count.items(), key=lambda x: -x[1])
        most_common_char = str(sorted_items[0][0]) 
        key += chr((ord(most_common_char) - ord('A') - 4) % ALPHABET_SIZE + ord('A'))
    return key

def enc(plainText, key):
    key = list(key)                            
    if len(plainText) == len(key):
        return(key)
    else:
        for i in range(len(plainText) -len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

ciphertext = input("Enter ciphertext: ").replace(' ', '').upper()

key_length = find_key_length(ciphertext)
print("Key length is: ", key_length)

key = find_key(ciphertext, key_length)
print("Key is: ", key)