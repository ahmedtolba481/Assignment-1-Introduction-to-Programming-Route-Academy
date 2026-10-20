n = input("Enter a number: ")
digits = list(n)
while len(digits)>1:
    m=sum(map(int, digits))
    digits=list(str(m))
print(f"Digital Root: {''.join(digits)}")