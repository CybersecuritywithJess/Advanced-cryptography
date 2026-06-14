# Mini AES Inspired Encryption Simulator

sbox = {
    0:14, 1:4, 2:13, 3:1,
    4:2, 5:15, 6:11, 7:8,
    8:3, 9:10, 10:6, 11:12,
    12:5, 13:9, 14:0, 15:7
}

inverse_sbox = {v:k for k,v in sbox.items()}

def substitute(value):
    return sbox[value]

def inverse_substitute(value):
    return inverse_sbox[value]

def permute(bits):
    return bits[::-1]

plaintext = int(input("Enter plaintext (0-15): "))
key = int(input("Enter key (0-15): "))

# Encryption
state = plaintext

for round in range(3):

    state ^= key

    state = substitute(state)

    binary = format(state, '04b')
    binary = permute(binary)

    state = int(binary, 2)

ciphertext = state

print("\nEncrypted Ciphertext:", ciphertext)

# Decryption

state = ciphertext

for round in range(3):

    binary = format(state, '04b')
    binary = permute(binary)

    state = int(binary, 2)

    state = inverse_substitute(state)

    state ^= key

print("Decrypted Plaintext:", state)