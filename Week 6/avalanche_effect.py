text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

hash1 = hash(text1)
hash2 = hash(text2)

print("\nHash 1:", hash1)
print("Hash 2:", hash2)

if hash1 != hash2:
    print("\nAvalanche Effect Observed")
else:
    print("\nNo Significant Difference")