# ==============================
# LFSR GENERATOR
# ==============================

def lfsr(seed, taps, length=50):
    state = seed
    seen_states = {}
    sequence = []

    for i in range(length):
        if state in seen_states:
            print("\nREPETITION DETECTED!")
            print(f"State repeated at step {i}")
            print(f"Estimated period: {i - seen_states[state]}")
            break

        seen_states[state] = i

        # output bit (last bit)
        output_bit = state[-1]
        sequence.append(output_bit)

        # XOR calculation for new bit
        new_bit = 0
        for t in taps:
            new_bit ^= int(state[t])

        state = str(new_bit) + state[:-1]

    print("\nGenerated Sequence:")
    print("".join(sequence))


# ==============================
# RUN PROGRAM
# ==============================
seed = "1100101"
taps = [0, 2]   # example tap positions

lfsr(seed, taps, 100)