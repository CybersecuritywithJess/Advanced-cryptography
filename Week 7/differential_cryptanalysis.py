# Differential Cryptanalysis Simulation

print("=== Differential Cryptanalysis Simulator ===")

# Input two plaintext values
p1 = int(input("Enter Plaintext 1: "))
p2 = int(input("Enter Plaintext 2: "))

# Compute XOR difference
difference = p1 ^ p2

print("\nResults")
print("Plaintext 1:", p1)
print("Plaintext 2:", p2)
print("Difference (P1 XOR P2):", difference)

# Observation
if difference == 0:
    print("Observation: Both plaintexts are identical.")
else:
    print("Observation: The plaintexts differ.")
    print("A non-zero XOR value indicates bit changes between the plaintexts.")

# Binary display
print("\nBinary Representation")
print("P1 =", format(p1, '08b'))
print("P2 =", format(p2, '08b'))
print("Difference =", format(difference, '08b'))