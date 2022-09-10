# git
## git 설명
작업폴더 -> staging are -> repository\
    git add         git commit
## git 로그인
- git config --global user.email [git 아이디]
- git config --global user.name [git 이름]

## git 기본 명령어
- git init -> 초기 설정
- git add 파일명 -> 해당파일 staging 상태로
- git commit -m 메시지 -> 저장할때 메시지 작성
- git log --oneline --all -> 현재 커밋내용 미리보기 커밋 아이디 확인가능
- git difftool 86554a3 86554a3 -> 두개의 커밋 파일 비교하기
- git status -> 현재 브런치위치 보기->이걸 잘 못마추면 push시 오류 발생
- git log -> 로그 확인
- git branch 이름 -> branch 만들기
- git switch 브랜치이름 -> 브랜치로 이동
- git switch master/main -> 초기 브랜치로 이동
- git merge 브랜치이름 -> 브랜치 합치기
## 레포지토리에 올리기
- git branch -M main -> 브랜치 이름을 메인으로 바꾸기
- git remote add [로컬저장이름] [깃허브주소] -> 로컬저장소를 만들기
- git remote -v -> 로컬정보 확인
- git push [로컬저장이름] [레포지토리저장할곳이름] -> 로컬저장소(origin)의 것을 main이라는 github로 이동
	- 이과정에서 오류 발생시 git pull origin main --allow-unrelated-histories 명령어를 통해 로컬과 레포지토리저장소 형태 같게 만들기
