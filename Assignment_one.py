# # ==================== Question 1 ====================
# print("#"*50)
# st=input("please input the string:\n").strip()
# l1s=[]
# l2n=[]
# for s in st:
#     if s.isalpha():
#         l1s.append(s)
#     elif s.isdigit():
#         l2n.append(s)
# l2n=list(map(int,l2n))
# stri="".join(l1s)
# tol=sum(l2n)
# print("=" * 40)
# print(f'Word : "{stri}"')
# print(f"Sum  : {tol}")
# print("=" * 40)
# print("#"*50)
#
# # ==================== Question 2 ====================
# import string as str
# print("#"*50)
# pa=input("please enter your password:\n").strip()
# # =======================================
# def validpa(pa):
#     v = False
#     up=0
#     sp=0
#     if not (len(pa) in range(8, 17)):
#         v = False
#         return v
#     for s in pa:
#         if s.isupper():
#             up+=1
#         elif s in str.punctuation:
#             sp+=1
#     if up>0 and sp>0:
#         v=True
#     return v
# # =======================================
# if validpa(pa):
#     print("Password is Secure.")
# else:
#     print("Invalid password. Please re-enter your password.")
# print("#"*50)
#
# # ==================== Question 3 ====================
# print("#"*50)
# price=int(input("please enter the price\nPrice:").strip())
# me=input("are you a member or not answer with Yes or No\nMember:").strip().lower()
# discount=0
# if price>=50 and price<=100:
#     discount+=10
# elif price>100:
#     discount+=20
# total=price-(price*(discount/100))
# discount=0
# if me=="yes":
#     discount+=5
# total=total-(total*(discount/100))
# print(f"Final Total:${total}")
#
# # ==================== Question 4 ====================
# l1=input("please enter the first names seperated by columns\nFirst_names: ").split(",")
# l2=input("please enter the second names seperated by columns\nSecond_names: ").split(",")
# l3=[]
# for i in l1:
#     for j in l2:
#         if i.strip()==j.strip():
#             l3.append(i.strip())
# print(f"Common names :{l3}")
#
# # ==================== Question 5 ====================
# student={}
# n = int(input("How many students? "))
# for i in range(n):
#     name = input("Enter the name of the student: ")
#     scores = list(map(int, input("Enter scores separated by commas: ").split(",")))
#     student[name] = scores
#
# for s ,v in student.items():
#     avge = sum(v) / len(v)
#     print(f"{s}: Average: {avge:.2f} -Honor Roll")
#
# # ==================== Question 6 ====================
# w1=input("input the word one make it same length with two\n")
# w2=input("input the word two make it same length with one\n")
# w3=""
# n=len(w1)
# for i in range(n):
#     w3=w3+w1[i]+w2[i]
# print(w3)
#
# # ==================== Question 7 ====================
# n = input("Enter a number: ")
# digits = list(n)
# while len(digits)>1:
#     m=sum(map(int, digits))
#     digits=list(str(m))
# print(f"Digital Root: {''.join(digits)}")
#
# # ==================== Question 8 ====================
# numbers = list(map(int, input("Enter numbers: ").strip().split(",")))
#
# freq = {}
#
# for i in numbers:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
#
# print(list(freq.items()))
#
# # ==================== Question 9 ====================
# n = int(input("Enter a number: "))
#
# fact = 1
# total = 0
#
# for i in range(1, n + 1):
#     fact *= i
#
# for i in range(1, n + 1):
#     total += i
#
# if fact % total == 0:
#     print(f"Factorial is {fact}, Sum is {total}. {fact} is divisible by {total}.")
# else:
#     print(f"Factorial is {fact}, Sum is {total}. {fact} is not divisible by {total}.")
#
# # ==================== Question 10 ====================
# store = {
#     "apple": 0.5,
#     "bread": 2.0,
#     "milk": 1.5
# }
# s=input("what you want to do add delete or you are done").strip().lower()
# cart=[]
# while s!="done":
#    if s=="add":
#        name=input(f"what you want to add {list(store.keys())}").strip().lower()
#        if name in store:
#            cart.append(name)
#            print(f"{name} added to cart.")
#        else:
#            print("Error: Item not available in store.")
#    elif s=="delete":
#        name = input(f"what you want to delete {list(store.keys())}").strip().lower()
#        if name in cart:
#            cart.remove(name)
#            print(f"{name} removed from cart.")
#        else:
#            print("Error: Item not found in cart.")
#    else:
#        print("Invalid action. Choose Add, Remove, or Done.")
#    s = input("what you want to do add delete or you are done").strip().lower()
# total=0
# for i in cart:
#     total+=store[i]
# print(total)
#
# # ==================== Question 11 ====================
# sentence = input("Enter a sentence: ").lower().strip()
#
# processed = sentence.replace(" ","")
# reve=processed[::-1]
# result =reve==processed
# print(result)
#
# # ==================== Question 12 ====================
# n=int(input("enter the number"))
# for i in range(n):
#         print(str(i+1)*n)
#
# # ==================== Question 13 ====================
# numbers = list(map(int,input("Enter numbers:").strip().split(",")))
# peaks = []
#
# for i in range(1, len(numbers) - 1):
#     if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
#         peaks.append(numbers[i])
#
# print("Peaks:", peaks)
#
# # ==================== Question 14 ====================
# import ast
#
# original = ast.literal_eval(input("Enter a dictionary: "))
# flipped = {}
#
# for key, value in original.items():
#     if value in flipped:
#         flipped[value].append(key)
#     else:
#         flipped[value] = [key]
#
# print(flipped)
#
# ==================== Question 15 ====================
stri = input("Enter the word: ").strip().lower()
mydi = {}

for i in range(len(stri)):
    if stri[i] in "aeiou":
        if stri[i] in mydi:
            mydi[stri[i]].append(i)
        else:
            mydi[stri[i]] = [i]

print(mydi)
