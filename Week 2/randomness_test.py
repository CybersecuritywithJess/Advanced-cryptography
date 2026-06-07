import random

data = [random.randint(0, 1) for _ in range(100)]

ones = data.count(1)
zeros = data.count(0)

print("Ones:", ones)
print("Zeros:", zeros)
print("Balance Ratio:", ones / len(data))