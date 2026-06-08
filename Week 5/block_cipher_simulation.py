# block_cipher_simulation.py

def substitute(block):
    substitution = {
        '0000': '1110',
        '0001': '0100',
        '0010': '1101',
        '0011': '0001',
        '0100': '0010',
        '0101': '1111',
        '0110': '1011',
        '0111': '1000',
        '1000': '0011',
        '1001': '1010',
        '1010': '0110',
        '1011': '1100',
        '1100': '0101',
        '1101': '1001',
        '1110': '0000',
        '1111': '0111'
    }

    result = ""

    for i in range(0, len(block), 4):
        chunk = block[i:i+4]
        result += substitution[chunk]

    return result


def permute(block):
    permutation = [2,4,6,8,1,3,5,7]

    output = ""

    for p in permutation:
        output += block[p-1]

    return output


def encrypt(text):

    encrypted_blocks = []

    for char in text:
        binary = format(ord(char), '08b')

        substituted = substitute(binary)

        permuted = permute(substituted)

        encrypted_blocks.append(permuted)

    return encrypted_blocks


plaintext = input("Enter text: ")

ciphertext = encrypt(plaintext)

print("\nEncrypted Blocks:")

for block in ciphertext:
    print(block)