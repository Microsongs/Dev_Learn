# Python practice
파이썬에 대해 연습하는 레포지토리입니다.

## Python Datatype
| 자료형 | 의미 | 예시 |
| --- | --- | --- |
| `str` | 문자열 | `"hello"` |
| `int` | 정수 | `10` |
| `float` | 실수 | `3.14` |
| `bool` | 참/거짓 | `True`, `False` |
| `list` | 여러 값을 순서대로 저장 | `[1, 2, 3]` |
| `dict` | key와 value로 저장 | `{"name": "dragon"}` |

## Python Conditional, Loop
```python
# Conditional
age = 20

if age >= 20:
    print("성인입니다")
else:
    print("미성년자입니다")

# Loop
```python
for number in range(3):
    print(number)
```

## Python Function
함수 → 반복을 줄이고, 코드를 읽기 쉽게 사용하기 위해 사용
```python
def check_pass(score):
    if score >= 60:
        return "합격"
    return "불합격"

print(check_pass(80))
print(check_pass(45))
```
## Python List, Dictionary
리스트: 여러 값을 순서대로 저장
딕셔너리: 이름표가 붙은 데이터 묶음
```python
server_names = ["web01", "web02", "db01"]

server_info = {
    "name": "web01",
    "ip": "10.0.0.10",
    "role": "web"
}

print(server_names)
print(server_info["name"])
print(server_info["ip"])
```

## File I/O
- 외부 파일 내용 가져오거나 저장
- 
```python
with open("server_check.txt", "w") as file:
    file.write("web01 정상\\n")
    file.write("web02 정상\\n")
    file.write("db01 확인 필요\\n")

with open("server_check.txt", "r") as file:
    result = file.read()

print(result)
```
