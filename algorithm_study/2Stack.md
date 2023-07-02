# 스택
## 스택의 특성
- 물건을 쌓아 올리듯 쌓아 올린 자료구조
- 선형 구조
  - 선형 구조 : 자료간의 관계가 1대1 관계
  - 비선형구조 : 자료간의 관계가 1대N 관계
- 후입선출(LIFO,Last-in-First-out)구조 마지막 자료를 먼저 꺼냄
- 자료를 삽입하거나 꺼낼 수 있음
## 연산
- 삽입 : 자료 저장, push
- 삭제 : 자료 꺼내기, 역순으로 꺼내짐 pop
- 공백인지 확인, isEmpty
- 스택 마지막 자료(top)의 원소를 반환, peek