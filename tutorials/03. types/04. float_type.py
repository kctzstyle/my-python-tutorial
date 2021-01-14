
# 실수(float)
#   파이썬 실수 타입이며, floating point를 표현합니다.


# 리터럴 선언 방식
f = 1.
f = 1.0

# 생성자 선언 방식
f = float(1.)
f = float(1.0)

# <class 'float'>
print(type(f))

# 1.0
print(f)


# `real`, `imag`, `conjugate`
#   정수 타입 튜토리얼에서 다뤘듯 복소수에 관련된 유용한 기능들입니다.

f = 3.14

# 3.14
print(f.real)

# 0.0
print(f.imag)

# 3.14
print(f.conjugate())


# is_integer
#   float가 정수값이면 `참`, 아니면 `거짓`을 반환합니다.
is_integer = f.is_integer()

# False
print(is_integer)

n = 10.

# True
print(n.is_integer())


# as_integer_ratio
#   float의 값을 분수로 표현합니다
ratio = f.as_integer_ratio()

# (7070651414971679, 2251799813685248)
print(ratio)

# 3.14
print(7070651414971679 / 2251799813685248)


# hex
#   float의 값을 16진수(hex)로 변환시켜줍니다.
#   반환되는 타입은 `str`로 반환됩니다.
h = f.hex()

# 0x1.91eb851eb851fp+1
print(h)


# fromhex
#   hex의 값을 float 값으로 변환시켜줍니다.
fh = f.fromhex(h)

# 3.14
print(fh)
