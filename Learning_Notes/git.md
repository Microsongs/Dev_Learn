# Git Practice
깃에 대해 연습하는 레포지토리입니다.

## Created README.md
```bash
touch "README.md" #mac
New-item README.md #Windows
```

## Git Cheatsheet
| 명령어 | 설명 | 사용 시기 |
| :---: | :--- | :--- |
| git init| 현재 폴더를 git 저장소로 생성 | 새 프로젝트 시작 시 |
| git status | 현재 변경 상태 확인 | 상태 확인 시 |
| git add 파일명 | 커밋할 파일 준비 | 변경 내용 기록 전 |
| git add . | 현재 폴더를 전부 커밋할 준비 | 여러 파일을 한 번에 올릴 때 |
| git commit -m "메세지" | 변경 내용을 하나의 기록으로 저장 | 작업 단위가 끝났을 때 |
| git log --oneline | 커밋 기록 확인 | 작업 기록 확인 시 |

## git link Cheatsheet
| 명령어 | 설명 | 사용 시기 |
| :---: | :--- | :--- |
| git remote add origin 주소 | Github 레포지토리에 주소 연결(origin은 주소의 별명) | 처음 원격 저장소 연결 시 |
| git remote -v | 원격 저장소 주소 확인| |
| git branch -M main | 현재 브랜치 이름을 main으로 변경 | Github 기본 branch로 변경 시 |
| git push -u origin main | origin 주소에 main branch를 올림 | 첫 push떄 |
| git push | 위 -u로 연결 후 부터 git push만으로 원격 저장소 업로드 | |

## git branch・merge Cheatsheet
| 명령어 | 설명 | 사용 시기 |
| :---: | :--- | :--- |
| git branch | 브랜치 목록 확인 | 현재 브랜치 확인 시|
| git branch 브랜치명 | 새 브랜치 생성 | 작업 공간 나눌 시 |
| git switch 브랜치명 | branch 이동 | 새로운 작업 공간(branch)로 이동 시 |
| git switch -c 브랜치명 | 브랜치 생성 및 이동 | |
| git checkout 브랜치명 | 브랜치 이동(예전 방식) | |
| git merge 브랜치명 | 현재 브랜치에 다른 브랜치를 병합 | 작업 결과 병합 시 |
