n = int(input("Enter a number: "))

fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i

for i in range(1, n + 1):
    total += i

if fact % total == 0:
    print(f"Factorial is {fact}, Sum is {total}. {fact} is divisible by {total}.")
else:
    print(f"Factorial is {fact}, Sum is {total}. {fact} is not divisible by {total}.")