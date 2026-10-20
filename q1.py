print("#"*50)
st=input("please input the string:\n").strip()
l1s=[]
l2n=[]
for s in st:
    if s.isalpha():
        l1s.append(s)
    elif s.isdigit():
        l2n.append(s)
l2n=list(map(int,l2n))
stri="".join(l1s)
tol=sum(l2n)
print("=" * 40)
print(f'Word : "{stri}"')
print(f"Sum  : {tol}")
print("=" * 40)
print("#"*50)