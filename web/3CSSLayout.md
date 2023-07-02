# Float
## CSS 원칙1
- 모든 요소는 네모(박스모델)이고 위에서부터 아래로 왼쪽부터 오른쪽으로 쌓인다.
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함
- 요소가 Normal flow를 벗어나게 함
----------------------------------
# Flexbox
## CSS Flexible Box Layout
- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - main axis(메인축)
  - cross axis(교차 축)
- 구성요소
  - Flex Container(부모 요소)
  - Flex Item(자식 요소)
- Flexbox를 사용하는 이유
  - 기존의 Float와 Position은 수직정렬과 아이템의 너비와 높이 혹은 간격을 동일하게 배치하기 힘들었음
  - Flexbox는 아이템의 너비와 높이 혹은 간격을 동일하게 배치시킨다
## Flex 속성
- 배치 설정
  - flex-direction
  - flex-wrap
- 공간 나누기
  - justify-content(main axis)
  - align-content(cross axis)
- 정렬
  - align-items(모든 아이템을 cross axis 기준으로)
  - align-self(개별 아이템)
## flex-direction
- Main axis를 기준 방향으로 설정
- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의
<img src="img\flex_direction.png">

## flex-wrap
- 아이템이 컨터이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 기본적으로 컨테이너 영역 벗어나지 않도록 함
<img src="img\flex_wrap.png">

## flex-direction & flex-wrap
- flex-direction:Main axis 방향 설정
- flex-wrap:요소들이 강제로 한줄 배치 결정
  - nowrap(기본 값):한줄에 배치
  - wrap:넘치면 다음줄 배치
- flex-flow
  - flex-direction과 flex-wrap의 shorthand
  - flex-direction과 flex-wrap 설정 값 차례로 작성
## justify-content & align-content
- justify-content:main axis 기준
- align-content:cross axis 기준
<img src="img\content.png">