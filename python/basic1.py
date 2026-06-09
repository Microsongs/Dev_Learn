name = "carrot"
score = 60
skills = ["python", "JS", "TS"]

print(name)
print(type(score))  # score의 type을 출력(=int)

if score >= 60:
    print("good")
else:
    print(f"{score} is not good")

for skill in skills:
    print(skill)


def check_pass(score):
    if score >= 60:
        print("pass")
    else:
        print(f"{score} is fail")


scores = [30, 40, 50, 60, 70, 80]
for s in scores:
    check_pass(s)

students = {"철수": 60, "민지": 80, "영희": 45}

def check_pass_name(name, score):
    if score >= 60:
        print(f"{name} passed")
    else:
        print(f"{name} failed")


for name, score in students.items():
    check_pass_name(name, score)
