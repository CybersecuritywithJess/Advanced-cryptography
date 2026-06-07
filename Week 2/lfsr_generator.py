def lfsr(seed, taps, length):
    state = seed.copy()
    output = []

    for _ in range(length):
        output.append(state[-1])
        feedback = 0

        for t in taps:
            feedback ^= state[t]

        state = [feedback] + state[:-1]

    return output


seed = [1, 0, 0, 1]
taps = [0, 2]  # positions used for XOR
length = 20

result = lfsr(seed, taps, length)
print("LFSR Output:", result)