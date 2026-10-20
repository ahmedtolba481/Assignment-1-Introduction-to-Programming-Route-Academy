stri = input("Enter the word: ").strip().lower()
mydi = {}

for i in range(len(stri)):
    if stri[i] in "aeiou":
        if stri[i] in mydi:
            mydi[stri[i]].append(i)
        else:
            mydi[stri[i]] = [i]

print(mydi)