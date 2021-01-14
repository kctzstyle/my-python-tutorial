
# 복소수(complex)
#   실수와 허수로 구성된 숫자 타입입니다.
#   `real + imag * 1j` 값을 가진 복소수를 돌려주거나 문자열 또는 숫자를 복소수로 변환합니다.

# 리터럴 선언 방식
c = 3j

# <class 'complex'>
print(type(c))

# 3j
print(c)

# 생성자 선언 방식
#   첫 번째 인자는 실수 `real`, 두 번째 인자는 허수 `imag` 입니다.
c = complex(0, 3)

# 3j
print(c)


# real
#   복소수의 실수 부분을 반환합니다.
real = c.real

# 0.0
print(real)


# imag
#   복소수의 허수 부분을 반환합니다.
imag = c.imag


# 3j
print(imag)


# conjugate
#   복소수의 켤레를 나타냅니다.
#   다시말해, `x + yj`를 `x - yj`로 바꿔 반환됩니다.
conjugate = c.conjugate()

# -3j
print(conjugate)
