# Advanced SPN Implementation

# Larger S-Box
sbox = {
    0:14, 1:4, 2:13, 3:1,
    4:2, 5:15, 6:11, 7:8,
    8:3, 9:10, 10:6, 11:12,
    12:5, 13:9, 14:0, 15:7
}

def substitute(value):
    return sbox[value]

def permute(bits):
    return bits[::-1]

plaintext = int(input("Enter plaintext (0-15): "))
key = int(input("Enter key (0-15): "))
rounds = int(input("Enter number of rounds: "))

current = plaintext

print("\nEncryption Process")

for r in range(rounds):
    print(f"\nRound {r+1}")

    current = current ^ key
    print("After Key Mixing:", current)

    current = substitute(current)
    print("After Substitution:", current)

    binary = format(current, '04b')
    binary = permute(binary)

    current = int(binary, 2)
    print("After Permutation:", current)

print("\nCiphertext:", current)