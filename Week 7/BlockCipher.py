from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import os
import numpy as np
from collections import Counter

# =========================
# CONFIG
# =========================
BLOCK_SIZE = 16

# =========================
# KEY GENERATION
# =========================
def generate_key():
    return os.urandom(16)

# =========================
# ENCRYPTION
# =========================
def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext.encode(), BLOCK_SIZE)
    return cipher.encrypt(padded)

# =========================
# DIFFERENCE ANALYSIS
# (Hamming Distance)
# =========================
def hamming_distance(b1, b2):
    length = min(len(b1), len(b2))
    return sum(bin(x ^ y).count("1") for x, y in zip(b1[:length], b2[:length]))

# =========================
# AVALANCHE EFFECT
# =========================
def avalanche_effect(ct1, ct2):
    diff_bits = hamming_distance(ct1, ct2)
    total_bits = len(ct1) * 8
    return (diff_bits / total_bits) * 100

# =========================
# FREQUENCY DISTRIBUTION
# =========================
def frequency_distribution(ciphertext):
    return dict(Counter(ciphertext))

# =========================
# STATISTICAL REPORT
# =========================
def statistical_report(avalanche_values):
    return {
        "mean_avalanche": float(np.mean(avalanche_values)),
        "max_avalanche": float(np.max(avalanche_values)),
        "min_avalanche": float(np.min(avalanche_values)),
        "std_dev": float(np.std(avalanche_values))
    }

# =========================
# MAIN ANALYZER
# =========================
def run_analyzer():
    key = generate_key()

    print("\n🔐 BLOCK CIPHER SECURITY ANALYZER")
    print("=" * 40)

    base_text = input("Enter original plaintext: ")
    modified_text = input("Enter modified plaintext: ")

    # Encrypt both
    ct1 = encrypt(base_text, key)
    ct2 = encrypt(modified_text, key)

    # Avalanche effect
    avalanche = avalanche_effect(ct1, ct2)

    # Frequency distribution
    freq = frequency_distribution(ct1)

    # Statistical report (single run wrapped in list)
    report = statistical_report([avalanche])

    # =========================
    # OUTPUT RESULTS
    # =========================
    print("\n📊 RESULTS")
    print("-" * 40)

    print(f"🔁 Hamming Distance: {hamming_distance(ct1, ct2)} bits")
    print(f"⚡ Avalanche Effect: {avalanche:.2f}%")

    print("\n📉 Frequency Distribution (Ciphertext 1)")
    for k, v in list(freq.items())[:10]:  # show first 10 bytes
        print(f"{k}: {v}")

    print("\n📈 Statistical Report")
    for k, v in report.items():
        print(f"{k}: {v}")

    print("\n✅ Analysis Complete")

# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":
    run_analyzer()