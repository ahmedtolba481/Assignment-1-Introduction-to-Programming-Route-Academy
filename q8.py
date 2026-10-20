numbers = list(map(int, input("Enter numbers: ").strip().split(",")))

freq = {}

for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(list(freq.items()))