print("#"*50)
price=int(input("please enter the price\nPrice:").strip())
me=input("are you a member or not answer with Yes or No\nMember:").strip().lower()
discount=0
if price>=50 and price<=100:
    discount+=10
elif price>100:
    discount+=20
total=price-(price*(discount/100))
discount=0
if me=="yes":
    discount+=5
total=total-(total*(discount/100))
print(f"Final Total:${total}")