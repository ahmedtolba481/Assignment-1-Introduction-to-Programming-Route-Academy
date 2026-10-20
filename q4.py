l1=input("please enter the first names seperated by columns\nFirst_names: ").split(",")
l2=input("please enter the second names seperated by columns\nSecond_names: ").split(",")
l3=[]
for i in l1:
    for j in l2:
        if i.strip()==j.strip():
            l3.append(i.strip())
print(f"Common names :{l3}")