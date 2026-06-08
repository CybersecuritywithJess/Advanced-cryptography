# avalanche_effect.py

def simple_encrypt(text):

    result = ""

    for ch in text:
        value = ord(ch)

        encrypted = value ^ 170

        result += format(encrypted, '08b')

    return result


text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

cipher1 = simple_encrypt(text1)
cipher2 = simple_encrypt(text2)

print("\nCiphertext 1:")
print(cipher1)

print("\nCiphertext 2:")
print(cipher2)

differences = 0

for a, b in zip(cipher1, cipher2):
    if a != b:
        differences += 1

print("\nDifferent Bits:", differences)

percentage = (differences / len(cipher1)) * 100

print("Avalanche Percentage:", round(percentage, 2), "%")