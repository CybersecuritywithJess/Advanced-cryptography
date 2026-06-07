def KSA(key):
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def PRGA(S, text):
    i = j = 0
    result = []

    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        result.append(chr(ord(char) ^ K))

    return ''.join(result)


key = [1, 2, 3]
text = "HELLO"

S = KSA(key)
cipher = PRGA(S, text)

print("Encrypted:", cipher)