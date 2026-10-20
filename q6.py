w1=input("input the word one make it same length with two\n")
w2=input("input the word two make it same length with one\n")
w3=""
n=len(w1)
for i in range(n):
    w3=w3+w1[i]+w2[i]
print(w3)