
# 파이썬과 프로그래밍 패러다임
# 파이썬은 멀티 패러다임 언어입니다.
# 패러다임이란, 생각하는 방식을 의미합니다.
# 프로그래밍 패러다임이라고 한다면 프로그램 하는 방식을 의미하는 것입니다.
# 따라서 파이썬에서 가능한 프로그래밍 패러다임은 종류가 많지만 크게 세 가지로 나눌 수 있습니다.

# 첫번째로, 절차지향 방식입니다.
# 절차지향 방식이란 말그대로 입력(input)과 출력(output)을 통해
# 절차적인 방식을 우선하여 데이터 중심으로 프로그래밍 하는 방식을 의미합니다.

# 두번째로, 객체지향 방식입니다.
# 객체지향이란, 프로그래밍에 필요한 모든 요소를 추상화라는 작업을 거친 뒤에
# 하나의 객체를 정의하고 그것을 투영하고 반영하여 프로그래밍을 하는 방식을 의미합니다.
# 따라서 프로그래밍에 필요한 데이터를 관리하는 방식을 객체를 통해 관리를 하게 됩니다.
# 객체의 정의는 밑에서 설명하는 '파이썬과 객체'를 참고해주세요.

# 파이썬과 객체
# 파이썬에는 여러 가지 type이 존재하는데, 파이썬에 정의된 모든 타입은 객체입니다.

# object: 객체(object)란 현실세계에 존재하는 속성(특징)과 행위를 가진 주체를 의미합니다.
#         이것을 프로그래밍 코드로 작성하면 클래스(class)라고 합니다.
#         하지만 객체가 가지는 속성과 행위는 너무나도 광범위하고 많기 때문에
#         객체가 가지는 속성과 행위 중 프로그래밍에 필요한 것만을 추려내는 작업을 '추상화'라고 합니다. 
# class: 클래스란, 추상화를 통해 정의한 객체를 프로그래밍 코드로 정의한 것을 의미합니다.
#        그리고 이 클래스 또한 하나의 타입으로 정의됩니다.
# type: 타입(type)은 말그대로 데이터의 유형을 의미합니다.
#       파이썬에서 type이라는 객체가 존재하는데, type 객체는 정의된 타입을 반환합니다.
#       뿐만 아니라 새로운 타입을 정의하여 생성하는 것도 가능합니다.


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


# 클래스를 정의할 때 암묵적으로 파스칼(Pascal) 스타일로 클래스명을 정의합니다.
# 각 언어에서 선호되고 권장되는 코딩 스타일(Coding Style)이 있는데,
# 파이썬에서는 이를 PEP8 문서에서 이러한 코딩 스타일들을 권장하고 있습니다.

class MyClass:
    pass

# pass: 아무런 동작을 실행하지 않는 키워드입니다.
#       주로 구현을 하지 않은 상태에서 코드 블럭을 유지하기 위해 사용됩니다.


# <class 'type'>
print(type(MyClass))

# <class '__main__.MyClass'>
print(MyClass)

# 결과가 이렇게 나오는 이유는 후에 '객체지향 및 클래스 튜토리얼'에서 공부해볼 것입니다.