student={}
n = int(input("How many students? "))
for i in range(n):
    name = input("Enter the name of the student: ")
    scores = list(map(int, input("Enter scores separated by commas: ").split(",")))
    student[name] = scores

for s ,v in student.items():
    avge = sum(v) / len(v)
    print(f"{s}: Average: {avge:.2f} -Honor Roll")