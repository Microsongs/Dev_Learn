import json

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
data = response.json()

print(response.status_code)
print(response.json())

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("result.json 파일 저장 완료")
