import json

import requests

url = "https://jsonplaceholder.typicode.com/posts"

# API 응답 수신
response = requests.get(url)

if response.status_code == 200:
    # 응답 내용을 json 문자열을 python 자료형으로 변환
    data = response.json()

    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print("posts.json 파일 저장 성공")
else:
    print(f"API 요청 실패: {response.status_code}")

# Status COde 정리
# 200: 성공
# 400: 잘못된 요청
# 401: 인증 실패
# 403: 권한 없음
# 404: 페이지 없음
# 500: 서버 오류
