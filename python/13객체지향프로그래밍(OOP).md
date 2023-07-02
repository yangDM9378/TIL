# OOP
## 객체
- 객체지향 프로그래밍
  - 컴퓨터 프로그램의 패러다임(방법론) 중 하나
  - '객체'들의 모임으로 파악하고자 하는 것
  - 객체의 특징
    - 타입(type):어떤 연산자와 조작이 가능한가?
    - 속성(attribute):어떤 산태(데이터)를 가지는가?
    - 조작법(method):어떤 행위(함수)를 할 수 있는가?
- 객체(Object)=속성(Attribute)+기능(Method)
## 객체지향 프로그래밍
- 객체지향 프로그래밍이란?
  - 프로그램을 여러개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
  - 객체->정보와 행동을 가진 것(정보-변수/행동-함수)
    - ex) 가수-이쁨(정보)//춤춘다(행동)
## 절차지향프로그래밍
- 객체를 순차적으로 처리하기 위해 프로그램 전체가 유기적으로 연결되어 있는 구조
- 실행속도가 빠르지만 유지보수가 어려움
## 객체지향 프로그래밍
- 데이터와 기능(메서드 분리), 추상화된 구조(인터페이스)
## 객체지향 프로그래밍이 필요한 이유
- 현실세계를 프로그램 설계에 반영(추상화)

## 객체지향의 장점/단점
- 장점
  - 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
  - 필요한 부분만 수정하기 쉽고 때문에 프로그램의 유지보수가 쉬움
- 단점
  - 설계 시 많은 노력과 시간이 필요
    - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
  - 실행 속도가 상대적으로 느림
    - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행속도가 빠름
-------------------------------------------------------
# OOP 기초
## 객체
- 속성과 행동으로 구성된 모든 것
- 파이썬은 모든 것이 객체인 객체지향프로그래밍(모든 것에 속성과 행동이 존재)
- ex) [3,2,1].sort()->리스트.정렬->객체.행동
- ex) 'banana'.sort()->문자열.대문자로->객체.행동
- 객체는 특정타입의 인스턴스이다.
  - 123,900,5는 모두 int의 인스턴스
  - [232,89,1],[]은 모두 list 의 인스턴스
## 객체와 인스턴스
- 클래스로 만든 객체를 인스턴스라고 함
## 클래스와 객체
- 클래스와 객체
- 클래스를 만든다==타입을 만든다
----------------------------------------------------
# 객체와 클래스 문법
## 기본 문법
- 클래스 정의 class MyClass:
- 인스턴스 생성 my_instance=MyClass()
- 메서드 호출 my_instance.my_method()
- 속성 my_instance.my_attribute
## 클래스와 인스턴스
- 객체의 설계도(클래스)을 가지고, 객체(인스턴스)를 생성한다.
## 객체 비교하기
- ==
  - 동등한
  - 변수가 참조하는 객체가 동등한(내용이 같은)경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
  - 동일한
  - 두 변수가 동일한 객체를 가리키는 경우 True
```
a=[1,2,3]
b=[1,2,3]
print(a==b, a is b) # True False

a=[1,2,3]
b=a
print(a==b, a is b) # True True
```
## OOP 속성
- 속성
  - 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
  - 클래스 변수/인스턴스 변수가 존재
```
class Person:
  blood_color='red'
  population=100

  def __init__(self, name):
    self.name=name
  
person1=Rerson('지민')
print(person1.name)
```
## 인스턴스 변수
- 인스턴스 변수란?
  - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  - 각 인스턴스들의 고유한 변수
- 생성자 메서드(__init__)에서 self.\<name>으로 정의
- 인스턴스가 생성될 이후 \<instance>.\<name>으로 접근 및 할당
```
class Person:
  def __init__(self, name):
    self.name=name
john=Person('john')
print(john.name) # john
john.name='john Kim'
print(john.name) # john Kim
```
## 클래스 변수
- 클래스변수
  - 한 클래스의 모든 인스턴스가 공유하는 값
  - 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
  - 예)특정사이트의 User 수 등은 클래스 변수를 사용
  - 클래스 선언 내부에서 정의
  - \<classname>.\<name>으로 접근 할당
```
class Circle():
  pi=3.14 # 클래스 변수 정의

  def _init__(self,r):
    self.r=r # 인스턴스변수

c1=Circle(5)
c2=Circle(10)

print(Circle.pi) # 3.14
print(c1.pi) # 3.14
print(c2.pi) # 3.14

Circle.pi =5 
print(Circle.pi) # 5
print(C1.pi) # 5
print(c2.pi) # 5
```
## 클래스 변수 활용(사용자 수 계산)
- 사용자가 몇명인지 확인?
  - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정하면 됨
```
class Person:
  count=0
  
  def __init__(self, name):
    self.name=name
    Person.count +=1

person1=Person('아이유')
person2=Person('이찬혁')
```
## 클래스 변수와 인스턴스 변수
- 클래스 변수를 변경할 때는 항상 클래스. 클래스변수 형식으로 변경
-------------------------------------
# OOP메서드
## 메서드
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
## 메서드의 종류
- 인스턴스 메서드
- 클래스 메서드
- 정적 메서드
## 인스턴스 메서드
- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신 전달
```
class MyClass:

  def instance_method(self, arg1,...)

my_instance=MyClass()
my_instance.instance_method(...)
```
## self
- 인스턴스 자기자신
- 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
  - 매개변수 이름으로 self를 첫번째 인자로 정의
  - 다른 단어로 써도 작동하지만, 파이썬의 암묵적 규칙
## 생성자 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정
  - 인스턴스 생성
  - __init__메서드 자동 호출
## 매직 메서드
- Double underscore(__)가 있는 메서든느 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 불림
- 특정 상황에 자동으로 불리는 메서드
- 예시
  - \__str__:출력형태 변경
  - \__gt__:부등호연산자
---------------------------------
# 클래스
## 클래스 메서드
- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨
```
class Myclass:

  @classmethod
  def class_method(cls, arg1,...):

Myclass.class_method(..)
```
## 데코레이터
- 함수를 어떤 함수로 꾸며서 새로운 기능 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 적용 되기 때문에 작성 순서가 중요
## 데코레이터 사용 예시
- 데코레이터 없이 함수 꾸미기
```
def hello():
  print('hello')

# 데코레이팅 함수
def add_print(original): # 파라미터로 함수를 받는다.
  def wrapper(): # 함수 내에서 새로운 함수 선언
    print('함수 시작') # 부가기능->original 함수를 꾸민다.
    original()
    print('함수 끝') # 부가기능->original 함수를 꾸민다.
  return wrapper # 함수를 return 한다.

add_print(hello)()
# 함수시작
# hello
# 함수 끝

print_hello=add_print(hello)
print_hello()
# 함수시작
# hello
# 함수 끝 
```
- 데코레이터를 활용하면 쉽게 여러 함수를 원하는 대로 변경할 수 있음 
```
# 데코레이팅 함수
def add_print(original) # 파라미터로 함수를 받는다.
  def wrapper() # 함수 내에서 새로운 함수 선언
    print('함수 시작') # 부가기능->original 함수를 꾸민다.
    original()
    print('함수 끝') # 부가기능->original 함수를 꾸민다.
  return wrapper # 함수를 return 한다.

@ add_print # add_print를 사용해서 print_hello()함수를 꾸며주도록 하는 명령어
def print_hello():
  print('hello')

print_hello()
# 함수시작
# hello
# 함수 끝 
```
## 클래스 메서드와 인스턴스 메서드
- 클래스메서드->클래스변수 사용
- 인스턴스 메서드->인스턴스 변수 사용
- 클래스는 인스턴스 변수 사용 불가능
- 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘다 사용가능
## 스태틱 메서드
- 인스턴스변수, 클래스 변수를 전혀 다루지 않는 메서드
- 속성을 다루지 않고 기능만을 하는 메서드 정의시 사용
- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용
  - 객체 상태나 클래스 상태를 수정할 수 없음
- @staticmethod 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
  - 주로 해당 클래스로 한정하는 용도로 사용
## 스태틱 메서드 사용 예시
```
class Person:
  count=0
  def __init__(self, name):
    self.name=name
    Person.count+=1

  @staticmethod
  def check_rich(money): # 스태틱은 cls. self 사용 X
    return money>10000

person1 = Person('아이유')
person2 = Person('이찬혁')
print(Person.check_rich(100000)) # True 스태틱은 클래스로 접근 가능
print(person1.check_rich(100000)) # True 스태틱은 인스턴스로 접근 가능
```
-------------------------------
# 메서드 정리
## 메서드 정리
- 인스턴스 메서드
  - 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스 조작
- 클래스 메서드
  - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
- 스태틱 메서드
  - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
    - 객체 상태나 클래스 상태를 수정할 수 없음
-------------------------------
# 객체지향의 핵심개념
## 객체지향의 핵심 4가지
- 추상화
- 상속
- 다형성
- 캡슐화
## 추상화
- 현실 세계를 프로그램 설계에 반영
  - 복잡한것 숨기고, 필요한것 들러내기
## 상속
- 상속이란
  - 두 클래스 사이 부모-자식 관계를 정립
- 클래스는 상속이 가능함
  - 모든 파이썬 클래스는 object를 상속받음
- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 상속 받음
- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성 높아짐
## 상속-상속 없이 구현하는 경우
- 학생/교수 정보를 나타내기 어려움
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def talk(self): # 중복
    print(f'반갑습니다. {self.name}입니다.')

class Professor:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.department=department

  def talk(self): # 중복
    print(f'반갑습니다. {self.name}입니다.')

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.gpa=dpa

  def talk(self): # 중복
    print(f'반갑습니다. {self.name}입니다.')
```
## 상속-상속으로 구현
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def talk(self): # 메서드 재사용
    print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.department=department

class Student(Person):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.gpa=dpa
```
## 상속관련 함수와 메서드
- isinstance(object, classinfo)
  - classinfo의 instance거나 subclass인 경우 True
- issbclass(class, classinfo)
  - class가 classinfo의 subclass면 True
- super()
  - 자식클래스에서 부모클래스를 사용하고 싶은 경우
## 상속정리
- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
- super()를 통해 부모클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능
- 상속관계에서의 이름 공간은 인스턴스, 자식클래스, 부모클래스 순으로 탐색
## 다중 상속
- 두개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정
```
class Person:
  def __init__(self, name):
    self.name = name
  
  def greeting(self):
    return f'안녕, {self.name}'

class MoM(Person):
  gene='XX'

  def swim(self):
    return '엄마가 수영'

class Dad(Person):
  gene='XY'

  def walk(self):
    return '아빠가 걷기


class FirstChild(Dad, Mom): -> 여기 부모의 순서에 따라 불러오는 순서가 바뀜 앞에꺼 먼저
  def swim(self):
    return '첫째가 수영'

  def cry(self):
    return '첫째가 응애'

baby1=FirstChild('아가')
print(baby1.cry()) # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene) # XY
```
## 상속 관련 함수와 메서드
- mro 메서드
  - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인
  - 기존의 인스턴스->클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스->자식->부모 순으로 확장
```
print(FirstChild.mro())
```
-----------------------
# 다형성
## 다형성
- 다형성이란?
  - 여러 모양을 뜻하는 그리스어
  - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음
  - 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답가능
## 메서드 오버라이딩
- 상속받은 메서드를 재정의
  - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
  - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정기능을 바꾸고 싶을 때 사용
- 상속받은 메서드를 재정의
  - 상속받은 클래스에서 같은 이름의 메서드로 덮어씀
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 super을 사용
```
class Person:
  def __init__(self, name, age):
    self.name = name

  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')

# 자식 클래스-Professor
class Professor(Person):
  def talk(self):
    print(f'{self.name}일세')

# 자식 클래스-Student
class Student(Person):
  def talk(self):
    super().talk()
    print(f'{self.name}일세')

p1=Professor('김교수')
p1.talk() # 김교수일세

s1=Student('이학생')
s1.talk()
# 반갑습니다. 이학생입니다.
# 저는 학생입니다.
```
-------------------------------------
# 캡슐화
## 캡슐화
- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
- 파이썬에서 암묵적으로 존재하지만, 언어적으로 존재x
## Public Member
- 언더바 없이 시작하는 메서드나 속성
- 어디서나 호출가능, 하위 클래스 override 허용
- 일반적으로 작성되는 메서드와 속성의 대다수 차지
```
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = 30

# Person 클래스의 인스턴스인 p1은 이름(name)과 나이(age) 모두 접근 가능
p1=Person('김싸피',30)
print(p1.name) # 김싸피
print(p1.age) # 30
```
## Protected Member
- 언더바 1개로 시작하는 메서드나 속성
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출
- 하위 클래스 override 허용
```
class Person:

  def __init__(self, name, age):
    self.name = name
    self._age = age
  
  def get_age(self):
    return self._age

# 인스턴스를 만들고 get_age 메서드를 활용하여 호출 
p1=Person('김싸피',30)
print(p1.get_age()) # 30

# _age에 직접 접근하여도 확인이 가능
print(p1.get_age()) # 30
```
## Private Member
- 언더바 2개로 시작하는 메서드나 속성
- 내부에서만 사용가능
- 하위클래스 상속 및 호출 불가능
- 외부 호출 불가능
```
class Person:

  def __init__(self, name, age):
    self.name = name
    self.__age = age
  
  def get_age(self):
    return self.__age

# 인스턴스를 만들고 get_age 메서드를 활용하여 호출 
p1=Person('김싸피',30)
print(p1.get_age()) # 30

# _age에 직접 접근 불가능
print(p1.get_age) # 30
```
## getter 메서드와 setter 메서드
- 변수에 접근할 수 있는 메서드를 별도로 생성
  - getter 메서드:변수의 값을 읽는 메서드
    - @property 데코레이터사용
  - setter 메서드:변수의 값을 설정하는 성격의 메서드
    - @변수.setter사용
```
class Person:

  def __init__(self, name, age):
    self.age = age
  
  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, new_age):
    if new_age<=19:
      raise ValueError('Too Young For SSafy)
      return
p1=Person('김싸피',30)
print(p1.get_age()) # 30

# _age에 직접 접근 불가능
print(p1.get_age) # 30
```