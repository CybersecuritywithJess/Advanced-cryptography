from collections import Counter

print("=== MINI CRYPTANALYSIS TOOLKIT ===")

# Step 1: Input Plaintexts
p1 = input("Enter Plaintext 1: ")
p2 = input("Enter Plaintext 2: ")

# --------------------------------------------------
# 1. Calculate Input Differences
# --------------------------------------------------

min_len = min(len(p1), len(p2))

differences = 0

for i in range(min_len):
    if p1[i] != p2[i]:
        differences += 1

differences += abs(len(p1) - len(p2))

print("\n--- INPUT DIFFERENCE ANALYSIS ---")
print("Number of differences:", differences)

# --------------------------------------------------
# 2. Frequency Analysis
# --------------------------------------------------

combined = p1 + p2

frequency = Counter(combined)

print("\n--- FREQUENCY ANALYSIS ---")

for char, count in frequency.items():
    print(f"{char}: {count}")

# --------------------------------------------------
# 3. Statistical Bias
# --------------------------------------------------

total_chars = len(combined)

most_common = frequency.most_common(1)[0]

bias = (most_common[1] / total_chars) * 100

print("\n--- STATISTICAL BIAS ---")
print("Most Common Character:", most_common[0])
print("Frequency:", most_common[1])
print(f"Bias: {bias:.2f}%")

# --------------------------------------------------
# 4. Automatic Results
# --------------------------------------------------

print("\n--- SECURITY OBSERVATION ---")

if bias > 50:
    print("High statistical bias detected.")
    print("Data may be vulnerable to frequency analysis.")
elif bias > 25:
    print("Moderate statistical bias detected.")
else:
    print("Low statistical bias detected.")
    print("Character distribution appears stronger.")

print("\nAnalysis Complete.")