import ast

original = ast.literal_eval(input("Enter a dictionary: "))
flipped = {}

for key, value in original.items():
    if value in flipped:
        flipped[value].append(key)
    else:
        flipped[value] = [key]

print(flipped)