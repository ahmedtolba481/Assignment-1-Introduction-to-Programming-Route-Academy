sentence = input("Enter a sentence: ").lower().strip()

processed = sentence.replace(" ","")
reve=processed[::-1]
result =reve==processed
print(result)