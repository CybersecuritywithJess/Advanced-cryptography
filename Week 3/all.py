# ============================================================
# RANDOMNESS TESTING PROGRAM
# Includes:
# - LCG Generator
# - Binary Sequence Generator
# - Frequency Test
# - Runs Test
# - Mean Test
# ============================================================

# ----------------------------
# LCG PARAMETERS
# ----------------------------
a = 1664525
c = 1013904223
m = 2**32
seed = 123

# ----------------------------
# LCG GENERATOR FUNCTION
# ----------------------------
def lcg(n, seed):
    numbers = []
    x = seed

    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)

    return numbers

# ----------------------------
# CONVERT TO BINARY SEQUENCE
# (Take last bit of each number)
# ----------------------------
def to_bits(numbers):
    bits = []
    for num in numbers:
        bits.append(num % 2)  # 0 or 1
    return bits

# ----------------------------
# FREQUENCY TEST
# ----------------------------
def frequency_test(bits):
    zeros = bits.count(0)
    ones = bits.count(1)
    n = len(bits)

    print("\n--- Frequency Test ---")
    print(f"0s: {zeros}, 1s: {ones}")

    ratio = zeros / n

    if 0.45 <= ratio <= 0.55:
        print("Result: Balanced (PASS)")
    else:
        print("Result: Biased (FAIL)")

# ----------------------------
# RUNS TEST
# ----------------------------
def runs_test(bits):
    runs = 1

    print("\n--- Runs Test ---")

    for i in range(1, len(bits)):
        if bits[i] != bits[i - 1]:
            runs += 1

    print(f"Total runs: {runs}")

    expected = len(bits) / 2

    if expected * 0.7 <= runs <= expected * 1.3:
        print("Result: Acceptable randomness (PASS)")
    else:
        print("Result: Poor randomness (FAIL)")

# ----------------------------
# MEAN TEST
# ----------------------------
def mean_test(bits):
    mean = sum(bits) / len(bits)

    print("\n--- Mean Test ---")
    print(f"Mean value: {mean:.4f}")

    if 0.45 <= mean <= 0.55:
        print("Result: Good randomness (PASS)")
    else:
        print("Result: Not random (FAIL)")

# ----------------------------
# MAIN PROGRAM
# ----------------------------
def main():
    print("===================================")
    print(" RANDOMNESS TESTING SYSTEM (LCG) ")
    print("===================================")

    # Generate 100+ values
    n = 100
    numbers = lcg(n, seed)

    # Convert to binary bits
    bits = to_bits(numbers)

    print("\nGenerated Bit Sequence:")
    print(bits)

    # Run tests
    frequency_test(bits)
    runs_test(bits)
    mean_test(bits)

    # Final conclusion
    print("\n--- FINAL CONCLUSION ---")

    zeros = bits.count(0)
    ones = bits.count(1)
    mean = sum(bits) / len(bits)

    if abs(zeros - ones) < 20 and 0.4 <= mean <= 0.6:
        print("Overall: Sequence shows acceptable randomness.")
    else:
        print("Overall: Sequence is weak / not truly random.")

# Run program
if __name__ == "__main__":
    main()