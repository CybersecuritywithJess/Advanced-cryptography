# lfsr_analysis.py

def lfsr(seed, taps, length):
    """
    Generate a binary sequence using an LFSR.

    seed  : Initial register state (e.g., [1,0,1,1])
    taps  : Positions used for feedback XOR
    length: Number of bits to generate
    """

    register = seed.copy()
    sequence = []

    for _ in range(length):
        output_bit = register[-1]
        sequence.append(output_bit)

        feedback = 0
        for tap in taps:
            feedback ^= register[tap]

        register = [feedback] + register[:-1]

    return sequence


def analyze_sequence(sequence):
    ones = sequence.count(1)
    zeros = sequence.count(0)

    print("\n--- Sequence Analysis ---")
    print("Sequence Length:", len(sequence))
    print("Number of 1s:", ones)
    print("Number of 0s:", zeros)

    if ones > zeros:
        print("Observation: More 1s than 0s.")
    elif zeros > ones:
        print("Observation: More 0s than 1s.")
    else:
        print("Observation: Equal number of 1s and 0s.")


# Main Program
print("LFSR Analysis Program")

seed = [1, 0, 1, 1]      # Initial register
taps = [0, 1]            # Feedback taps
length = 20              # Number of bits to generate

sequence = lfsr(seed, taps, length)

print("\nGenerated Sequence:")
print("".join(map(str, sequence)))

analyze_sequence(sequence)