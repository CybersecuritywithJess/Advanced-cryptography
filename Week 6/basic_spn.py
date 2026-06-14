# Simple SPN (Substitution-Permutation Network)

# S-Box (Substitution Table)
sbox = {
    '0': 'E',
    '1': '4',
    '2': 'D',
    '3': '1',
    '4': '2',
    '5': 'F',
    '6': 'B',
    '7': '8',
    '8': '3',
    '9': 'A'
}

# User Input
plaintext = input("Enter plaintext (numbers only): ")

# Substitution Step
substituted = ""
for char in plaintext:
    substituted += sbox.get(char, char)

print("After Substitution:", substituted)

# Permutation Step (Reverse Characters)
ciphertext = substituted[::-1]

print("Ciphertext:", ciphertext)