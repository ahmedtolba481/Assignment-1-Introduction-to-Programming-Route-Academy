import string as str
print("#"*50)
pa=input("please enter your password:\n").strip()
# =======================================
def validpa(pa):
    v = False
    up=0
    sp=0
    if not (len(pa) in range(8, 17)):
        v = False
        return v
    for s in pa:
        if s.isupper():
            up+=1
        elif s in str.punctuation:
            sp+=1
    if up>0 and sp>0:
        v=True
    return v
# =======================================
if validpa(pa):
    print("Password is Secure.")
else:
    print("Invalid password. Please re-enter your password.")
print("#"*50)