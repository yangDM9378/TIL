# CSS
## CSS
- 스타일을 지정하기 위한 언어 선택하고, 스타일 지정한다.
## CSS 구문-용어정리
<img src="img\CSS_rn.png">

## CSS
- CSS 구문은 선택자를 통해 스타일을 지정 HTML 요소 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 ㄴ선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성:어떤 스타일 기능을 변경할지 결정
  - 값:어떻게 스타일 기능을 변경할지 결정
## CSS 정의 방법
- 인라인->인라인을 쓰게 되면 실수가 잦아짐(중복도 있고 찾기 어려워)
- 내부참조->코드가 너무 길어짐
- 외부 참조->가장많이 사용\<link>를 통해 외부 CSS 파일 불러오기
------------------------------
# CSS Selectors
## CSS 선택자 정리
- 요소 선택자
  - HTML태그를 직접 선택
- 클래스 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - #문자로 시작하며, 해당 아이디가 적용된 항목 선택
  - 일반적으로 하나의 문서에 1번 사용
  - 여러번 사용하여도 동작, 단일 id 권장
## CSS적용 우선순위
- CSS 우선순위 지어볼 수 있다.
  - 1.중요도-사용시 주의
  - 2.우선순위
    - 인라인>class, 속성, pseudo-class>요소,pseudo-element
  - 3.CSS파일 로딩 순서
## 예제
```
<p>1</p> # 오랜지
<p class="blue">2</p> # 블루
<p class="blue green">3</p> # 그린
<p class="green blue">4</p> # .green CSS에서 아래쪽에 있는것이 실행된다->그린
<p id="red" class="blue">5</p> # 클래스와 아이디가 있으면 아이디->레드
<h2 id="red" class="blue">6<h2> # !important가 최우선->다크바이올릿
<p id="red" class="blue" style="color:yellow;">7</p> # 인라인 우선->엘로우
<h2 id="red" class="blue" style="color:yellow;">8</h2>->다크바이올릿
```
```
h2 {
  color:darkviolet !important;
}
p {
  color:orange;
}
.blue {
  color:blue;
}
.green {
  color:green;
}
#red {
  color:red;
}
```
## CSS 상속
- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속
  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속 되는 것 예시
    예) Text관련 요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것 예시
    예) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom//left, z-index) 등
```
<body>
  <p>안녕하세요<span>테스트</span>입니다.</p>
</body>
```
```
<style>
  p{
    /* 상속됨 */
    color:red;
    /* 상속 안됨 */
    border: 3px solid black;
  }
  span{
  }
</style>
```
------------------
# CSS 기본 스타일
## 크기단위
- px
  - 모니터 해상도의 한 화소인 픽셀 기준
  - 픽셀의 크기는 변지않기에 고정적
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수단위, 요소에 지정된 사이즈에 상대적인 사이즈로 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단윌를 가짐
- viewport
  - 웹페이지를 방문한 유저에게 바로 보이게 되는 웹컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정
  - vw, vh, vmin, vmax
- px는 브라우저의 크기를 변경해도 그대로
- vw는 브라우저의 크기에 따라 크기 변함
## 색상 단위
- 색상 키워드
  - 대소문자 구분x
  - red,blue 등과 같은 특정색을 직접 글자로 나타냄
- RGB 색상
  - 16진수 표기법 혹은 함수형 표기법을 사용해 특정 색을 표현하는 방식
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
## 결합자
- 자손결합자(공백)
  - selectorA 하위의 모든 selectorB 요소
```
<style>
  div span {
    color:red;
  }
</style>

<div>
  <span>이건 빨강입니다.</span>
  <p>이건 빨강이 아닙니다.</p>
  <p>
    <span>이건 빨강입니다.</span>
  </p>
</div>
```
- 자식결합자(>)
  - selectorA 바로 아래의 selectorB 요소
```
<style>
  div > span {
    color:red;
  }
</style>

<div>
  <span>이건 빨강입니다.</span>
  <p>이건 빨강이 아닙니다.</p>
  <p>
    <span>이건 빨강이 아닙니다.</span>
  </p>
</div>
```
- 일반 형제 결합자(~)
  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB요소 모두 선택
```
<style>
  div ~ span {
    color:red;
  }
</style>

<div>
  <span>이건 빨강이 아닙니다.</span>
  <p>문단</p>
  <b>코드</b>
  <span>이건 빨강</span>
  <b>코드</b>
  <span>이건 빨강</span>

</div>
```
- 인접 형제 결합자(+)
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택
```
<style>
  div + span {
    color:red;
  }
</style>

<div>
  <span>이건 빨강이 아닙니다.</span>
  <p>문단</p>
  <b>코드</b>
  <span>이건 빨강</span>
  <b>코드</b>
  <span>이건 빨강아닙니다</span>
</div>
```
-------------
# CSS Box model
## CSS 원칙 1
- 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다(좌측 상단에 배치)
## Box model
- 모든 HTML 요소는 box 형태로 되어있음
- 하나의 박스는 네부분으로 이루어짐
  - margin
  - border
  - padding
  - content

<img src="img\box_model.png">

## Box model 구성
- margin
```
.margin{
  margin-top:10px;
  margin-right:20px;
  margin-bottom:30px;
  margin-left:40px;
}
```
- padding
```
.margin-padding{
  margin:10px
  padding:30px
}
```
- border
```
.border{
  border-width:2px;
  border-style:dashed;
  border-color:black;
}
```
## box-sizing
- 기본적으로 모든 요소의 box_sizing은 content-box
  - padding을 제외한 순수 contents영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그경우 box-sizing을 border-box로 설정
## CSS 원칙 2
- 모든 요소는 네모(박스모델)이고, 좌측상단에 배치.
- display에 따라 크기와 배치가 달라진다.
## 대표적으로 활용되는 display
- display:block
  - 줄바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- display:inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정
- 블록레벨 요소와 인라인 레벨 요소
  - 블록 레벨 요소와 일라인 레벨 요소 구분
  - 대표적인 블록 레벨 요소
    - div/ul,ol,li/p/hr/from등
  - 대표적인 인라인 레벨 요소
    - span/a/img/input,label/b,em,i,strong 등
## display
- display:inline-block
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- display:none
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility:hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
----------------------------
# CSS position
## CSS position
- 문서 상에서 요소의 위치를 지정
- static:모든 태그의 기본값(기본위치)
  - 일반적인 요소의 배치 순서에 따름(좌측상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치
- 좌표 프로퍼티를 사용하여 이동가능
  - relative:상대 위치
    - 자기 자신의 static 위치를 기준으로 이동
    - 레이아웃에서 요소가 차지하는 공간은 static일때와 같음
  - absolute:절대위치
    - 요소를 일반적인 문서흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동
  - fixed:고정위치
    - 요소를 일반적인 문서 흐름에서 제거후 레이아웃 공간을 차지 하지 않음
    - 부모 요소와 관계없이 viewprot를 기준으로이동
      - 스크롤시 항상 같은 곳에 유지
  - sticky:스크롤에 따라 static->fixed로 변경
    - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 박스를 고정 가능
## CSS 원칙
- CSS 원칙 1,2 Nomal flow
  - 모든 요소는 네모, 좌측상단에 배치
  - display에 따라 크기와 배치가 달라짐
- CSS 원칙 3
  - position으로 위치의 기준을 변경
    - relative:본인원래위치
    - absolute:특정부모의 위치
    - fixed:화면 위치
    - sticky:static이나 스크롤 이동에 따라 fixed로 변경
