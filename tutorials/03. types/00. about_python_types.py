
# 파이썬과 프로그래밍 패러다임
#   파이썬은 멀티 패러다임 언어입니다.
#   패러다임이란, 생각하는 방식을 의미합니다.
#   프로그래밍 패러다임이라고 한다면 프로그램 하는 방식을 의미하는 것입니다.
#   따라서 파이썬에서 가능한 프로그래밍 패러다임은 종류가 많지만 크게 세 가지로 나눌 수 있습니다.

# 첫번째로, 절차지향 방식입니다.
#   절차지향 방식이란 말그대로 입력(input)과 출력(output)을 통해 데이터의 상태를 바꾸고 관리하는 것에 초점을 둡니다.
#   프로그램의 동작 또한 데이터의 절차적 흐름을 우선하여 데이터를 중심으로 프로그래밍 하는 방식을 의미합니다.

# 두번째로, 객체지향 방식입니다.
#   객체지향이란, 프로그래밍에 필요한 모든 요소를 추상화라는 작업을 거친 뒤에
#   하나의 객체를 정의하고 그것을 투영하고 반영하여 프로그래밍을 하는 방식을 의미합니다.
#   따라서 프로그래밍에 필요한 데이터를 관리하는 방식을 객체를 통해 관리를 하게 됩니다.
#   객체에 대한 정의는 아래에서 설명하는 '파이썬과 객체'를 참고해주세요.

# 세번째로, 함수지향 방식입니다.
#   함수지향이란, 데이터 처리를 수학적 함수의 계산으로 취급하고 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임의 하나입니다.
#   절차지향 방식에서는 상태를 바꾸는 것을 강조하는 것과는 달리, 함수형 프로그래밍은 함수의 응용을 강조합니다.
#   프로그래밍이 문이 아닌 식이나 선언으로 수행되는 선언형 프로그래밍 패러다임을 따르고 있습니다.


# 파이썬과 객체
#   파이썬에는 여러 가지 type이 존재하는데, 파이썬에 정의된 모든 타입은 객체입니다.

# 객체(object)
#   객체란, 현실세계에 존재하는 속성(특징)과 행위를 가진 주체를 의미합니다.
#   이것을 프로그래밍 코드로 작성하면 클래스(class)라고 합니다.
#   하지만 객체가 가지는 속성과 행위는 너무나도 광범위하고 많기 때문에
#   객체가 가지는 속성과 행위 중 프로그래밍에 필요한 것만을 추려내는 작업을 하는데
#   이를 '추상화'라고 합니다.

# 클래스(class)
#   클래스란, 추상화를 통해 정의한 객체를 프로그래밍 코드로 정의한 것을 의미합니다.
#   그리고 이 클래스 또한 하나의 타입으로 정의됩니다.

# type
#   타입(type)은 말그대로 데이터의 유형을 의미합니다.
#   파이썬에서 type이라는 객체가 존재하는데, type 객체는 정의된 타입을 반환합니다.
#   뿐만 아니라 새로운 타입을 정의하여 생성하는 것도 가능합니다.


# type
# <class 'type'>
print(type(type))

# 정수
# <class 'int'>
print(type(10))

# 실수
# <class 'float'>
print(type(3.14))

# 복소수
# <class 'complex'>
print(type(1 + 3j))

# 문자열
# <class 'str'>
print(type('Hi'))


# 대표적인 코딩 스타일(Coding Style)

# 헝가리안 표기법(Hungarian Notation)
#   프로그래밍 언어에서 변수 및 함수의 인자 이름 앞에 데이터 타입을 명시하는 코딩 규칙입니다.
#   요즘 프로그래밍 코딩 스타일에는 권장되는 방식이 아닙니다.
#   ex) intNumber = 1
#       intA = 10
#       floatPi = 3.14
#       strHello = 'Hello'

# 파스칼 표기법(Pascal Case)
#   각 문장의 명사, 동사, 형용사 등 앞에 영문 대문자를 사용하여 구분하는 코딩 규칙입니다.
#   ex) Apple = 'apple'
#       AirConditional = 'airconditional'
#       HelloPython = 'Hello, Python'
#       FooBar = 'foo bar'
#       IsThis = 'is this'
#       YouAndMe = 'you and me'

# 스네이크 표기법(Snake Case)
#   각 문장의 명사, 동사, 형용사 등 앞에 언더스코어(underscore; `_` 기호)를 사용하여 구분하는 코딩 규칙입니다.
#   문장의 구성이 마치 뱀의 몸체처럼 생겼다고 해서 스네이크 표기법이라는 명칭이 지어졌습니다.
#   ex) hello_python = 'Hello, Python'
#       foo_bar = 'foo bar'
#       you_and_me = 'you and me'

# 카멜 표기법(Camel Case)
#   맨 앞의 문장은 영문 소문자, 그 뒤 각 문장의 명사, 동사, 형용사 등 앞에 영문 대문자를 사용하여 구분하는 코딩 규칙입니다.
#   문장의 구성이 마치 낙타의 혹처럼 생겼다고 해서 카멜 표기법이라는 명칭이 지어졌습니다.
#   ex) helloPython = 'Hello, Python'
#       fooBar = 'foo bar'
#       youAndMe = 'you and me'


# 클래스를 정의할 때 암묵적으로 파스칼(Pascal) 표기법으로 클래스명을 정의합니다.
# 각 언어에서 선호되고 권장되는 코딩 스타일(Coding Style)이 있는데,
# 파이썬에서는 이를 PEP8 문서에서 이러한 코딩 스타일들을 권장하고 있습니다.

class MyClass:
    pass

# pass
#   아무런 동작을 실행하지 않는 키워드입니다.
#   주로 구현을 하지 않은 상태에서 코드 블럭을 유지하기 위해 사용됩니다.


# <class 'type'>
print(type(MyClass))

# <class '__main__.MyClass'>
print(MyClass)

# <class '__main__.MyClass'>
print(type(MyClass()))

# 결과가 이렇게 나오는 이유는 후에 '객체지향 및 클래스 튜토리얼'에서 공부해볼 것입니다.


# type으로 새로운 type 정의하기
#   type 객체를 다음과 같이 사용하면 새로운 타입을 정의할 수 있습니다.

MyType = type('MyType', (object,), {})

# <class '__main__.MyType'>
print(MyType)


# 상수; 리터럴(literal)
#   변하지 않는 고정된 값 그 자체를 의미합니다.
#   예를 들면 정수 1, 실수 3.14, 복소수 1 + 3j 등 고정된 값을 한번 선언하였기에
#   이 값은 더 이상 변하지 않습니다.

a = 1

# 여기서 `a = 1`을 바인딩 하였을 때 고정된 값 `1`을 리터럴 상수라고 합니다.

# 타입의 종류
#   숫자 타입(Numeric types)
#     숫자 타입에는 크게 총 4 가지가 있습니다.
#     각각 논리(bool), 정수(int), 실수(float), 복소수(complex)입니다.
#     `bool`은 논리 타입이기도 하지만, 엄밀히 따지면 `0` 과 `1`로 각각 `거짓`과 `참`을 구분 짓습니다.
#   컨테이너 타입(Container types)
#     각 객체(데이터)들을 특징적인 구조로 가질 수 있는 자료 구조(data structure) 객체 입니다.
#     컬렉션(Collection) 타입이라고도 합니다.
#     컨테이너 타입에는 리스트(list), 튜플(tuple), 세트(set), 프로즌세트(frozenset), 딕셔너리(dict)가 있습니다.
#   문자열 타입(String types)
#     문자열 역시 각 문자들에 대한 선형 구조이기 때문에 컨테이너 타입에 속합니다.
#     문자열은 바이트(bytes), 바이트 배열(bytesarray), 유니코드 문자열(str)이 있습니다.
