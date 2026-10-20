store = {
    "apple": 0.5,
    "bread": 2.0,
    "milk": 1.5
}
s=input("what you want to do add delete or you are done").strip().lower()
cart=[]
while s!="done":
   if s=="add":
       name=input(f"what you want to add {list(store.keys())}").strip().lower()
       if name in store:
           cart.append(name)
           print(f"{name} added to cart.")
       else:
           print("Error: Item not available in store.")
   elif s=="delete":
       name = input(f"what you want to delete {list(store.keys())}").strip().lower()
       if name in cart:
           cart.remove(name)
           print(f"{name} removed from cart.")
       else:
           print("Error: Item not found in cart.")
   else:
       print("Invalid action. Choose Add, Remove, or Done.")
   s = input("what you want to do add delete or you are done").strip().lower()
total=0
for i in cart:
    total+=store[i]
print(total)