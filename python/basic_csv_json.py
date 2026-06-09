import csv
import json

# csv 파일 쓰기
with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "score"])
    writer.writerow(["철수", 85])
    writer.writerow(["민지", 40])
    writer.writerow(["영희", 70])
    writer.writerow(["하늘", 50])

# csv 파일 읽기
results = []

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        score = int(row["score"])

        if score >= 60:
            passed = True
        else:
            passed = False

        results.append({"name": name, "score": score, "passed": passed})

# json 파일 쓰기
with open("students.json", "w", encoding="utf-8") as file:
    # result를 file(students.json)에 json형태로 저장
    # ensure_ascii=False -> 한글 안깨지도록, indent=2 -> 들여쓰기
    json.dump(results, file, ensure_ascii=False, indent=2)

# json 파일 읽기
with open("students.json", "r", encoding="utf-8") as file:
    datas = json.load(file)
    for data in datas:
        print(data["name"])
        print(data["passed"])
        print(data["score"])
