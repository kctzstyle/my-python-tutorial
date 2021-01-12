
# bool: 불(bool)은 boolean의 약어로써, 참과 거짓을 의미하는 논리 타입입니다.
#       참은 `True`, 거짓은 `False`로 정의합니다.

# <class 'bool'>
print(type(True))
# <class 'bool'>
print(type(False))

# True
print(True)
# False
print(False)


# 비교하기
# 각 객체와 값에 대한 참과 거짓을 비교할 때는 키워드와 논리 연산자를 통해 비교합니다.

# 키워드(keyword)로 비교하기
# in: 멤버십 연산자로써, `list_type.py`의 '멤버십 연산자'를 참고해주세요.
# is: 값이 참조하는 객체의 아이덴티티(주소값)가 같은 주소값을 참조하면 참, 아니면 거짓의 결과를 나타냅니다.
# not: 참이면 거짓, 거짓이면 참의 결과를 나타냅니다. `is` 키워드 및 `in` 키워드와 혼용해서 사용할 수 있습니다.
# and: 둘 다 참이면 참, 아니면 거짓을 나타냅니다.
# or: 둘 중 하나라도 참이면 참, 아니면 거짓을 나타냅니다.

# 논리 연산자(operator)로 비교하기
# `==` 연산자: 값이 같은가를 비교하여 같으면 참, 아니면 거짓을 나타냅니다.
# `!=` 연산자: `not` 키워드와 동일하게 값이 틀리면 참, 아니면 거짓을 나타냅니다.
# `<` 연산자: `a < b`에서 a가 b보다 작으면 참, 아니면 거짓을 나타냅니다.
# `>` 연산자: `a > b`에서 a가 b보다 크면 참, 아니면 거짓을 나타냅니다.
# `<=` 연산자: `a <= b`에서 a가 b보다 작거나 같으면 참, 아니면 거짓을 나타냅니다.
# `>=` 연산자: `a >= b`에서 a가 b보다 크거나 같으면 참, 아니면 거짓을 나타냅니다.


a = 1
b = 2

# False
print('a is b?', a is b)

# True
print('a is not b?', a is not b)

# True
print('(1 + 1) == 2?', ((1 + 1) == 2))
# False
print('(1 - 1) == 2?', (1 - 1) == 2)
