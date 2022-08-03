# HTML
## 웹사이트의 구성요소
- 웹사이트란 브라우저를 통해 접속하는 웹페이지 문서 모음
- 웹 페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 마우스 클릭으로 다른 페이지로 이동하는 링크가 있음. 링크를 통해 웹페이지를 연결한 것을 웹사이트라고 함.
  - HTML->구조
  - CSS->표현
  - Javascript->동작
## Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  - 대표적인 예 - HTML, Markdown
  --------------------------
# HTML 기본구조
## HTML 기본구조
- html:문서의 최상위(root)요소
- head:문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body:문서 본문요소
  - 실제 화면 구성과 관련된 내용
## head 예시
- \<title>:브라우저 상단 타이틀
- \<meta>:문서 레벨 메타데이터 요소
- \<link>:외부 리소스 연결 요소(CSS 파일, favicon 등)
- \<script>:스크립트 요소(JavaScript파일/코드)
- \<style>:CSS 직접 작성
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```
## 요소
- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 요소는 태그 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재(닫는 태그가 없음)
    - br, hr, img, input, link, meta
- 요소는 중접(nested)될수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음
## 속성
- 속성을 통해 태그의 부가적인 정보를 설정
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가 정보 제공
- 요소의 시작 태그에 작성 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용가능한 속성(HTML Global Attribute)들도 있음
## HTML Global Attribute
- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적 속성(몇몇 요소에는 아무 효과 없을 수 있음)
  - id:문서 전체에서 유일한 고유 식별자 지정
  - class:공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
  - data-*:페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  - style:inline 스타일
  - title:요소에 대한 추가 정보 지정
  - tabindex:요소의 탭순서
## 시맨틱 태그
- HTML5에서 의미론적 요소를 담는 태그 등장
  - 기존 영역을 의미하는 div 태그를 대체사용
- 대표적인 태그 목록
  - header:문서 전체나 섹션의 헤더(머리말 부분)
  - nav:내비게이션
  - aside:사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
- Non semantic요소는 div,span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용
## DOM트리
- 택스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
- HTML 문서에 대한 모델을 구성함
- HTML 문서 내에 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드 제공
# HTML 문서 구조화
## 텍스트 요소
|태그|설명|
|-|-|
|\<a>\</a>|href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성|
|\<b>\</b>|굵은 글씨 요소|
|\<i>>\</i>|기울임 글씨 요소|
|\<br>|텍스트 내에 줄 바꿈 생성|
|\<img>|src 속성을 활용하여 이미지 표현|
|\<span>\</span>|의미없는 인라인 컨테이너|
## 그룹 컨텐츠
|태그|설명|
|-|-|
|\<p>\</p>|href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성|
|\<hr>|문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨|
|\<ol>\</ol></br>\<ul>\</ul>|순서가 있는 리스트</br>순서가 없는 리스트|
|\<pre>\</pre>|HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지|
|\<blockquote>\</blockuote>|텍스트가 긴 인용문 주로 들여쓰기를 한 것으로 표현됨|
|\<div>\</div>|의미 없는 블록 레벨 컨테이너|
## form
- \<form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
- \<form>기본 속성
  - action:form을 처리할 서버의 URL(데이터를 보낼 곳)
  - method:form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
  - enctype:method가 post인 경우 데이터의 유형
    - apllication/x-www-form-urlencoded:기본값
    - multipart/form-data:파일 전송시(input type이 file인 경우)
    - text/plain:HTML5 디버깅 용
## input
- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공
- \<input> 대표적인 속성
  - name:form control에 적용되는 이름(이름/값 페어로 전송)
  - value:form control에 적용되는 값(이름/값 페어로 전송)
  - required, readonly, autofocus, autocomplete, disabled 등
## input label
- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 가능
  - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일 환경에서 편하게 사용
  - label과 input입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인
- \<input>에 id 속성을, \<label>에는 for 속성을 활용하여 상호 연관 
## input 유형-일반
- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용가능
  - text:일바텍스트 입력
  - password:입력시 값이 보이지 않고 특수기호로 표현
  - email 이메일 형식이 아닌경우 form 제출 불가
  - number:min, max, step속성을 활용하여 숫자 범위 설정가능
  - file:accept 속성을 활용하여 파일 타입 지정 가능
  - 일반적으로 label 태그와 함께 사용하여 선택항목을 작성
  - 동일 항목에 대해 name을 지정 선택 항목에 대한 value를 지정
    - checkbos:다중선택
    - radio:단일선택<br/>
<img src="img\input_type_box.png">

```
<body>
  <p>checkbox->다중선택</p>
  <input id="html" type="checkbox" name="language" valu="html">
  <label for="html">HTML</label>
  <input id="python" type="checkbox" name="language" valu="python">
  <label for="python">파이썬</label>
  <input id="java" type="checkbox" name="language" valu="java">
  <label for="java">HTML</label>
  <hr>
  <p>radio->단일선택</p>
  <input id="html1" type="radio" name="language" valu="html">
  <label for="html1">HTML</label>
  <input id="python1" type="radio" name="language" valu="python">
  <label for="python1">파이썬</label>
  <input id="java1" type="radio" name="language" valu="java">
  <label for="java1">HTML</label>
  <hr>
</body>
```
## input 유형-일반
- 다양한 종류의 input을 위한 picker를 제공
  - color:color picker
  - data:data picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden:사용자에게 보이지 않는 input
## input의 타입
- input 요소의 동작은 type에 따라 달라짐
https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input