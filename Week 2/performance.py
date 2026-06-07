import time
start = time.time()

# simulate encryption
data = "HELLO" * 1000
encrypted = ''.join(chr(ord(c) ^ 5) for c in data)

end = time.time()

print("Time taken:", end - start)