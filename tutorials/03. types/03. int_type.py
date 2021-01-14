
# 정수(int)
#   int는 integer의 약어로써 정수를 의미합니다.


# 리터럴 선언 방식
n = 1

# 생성자 선언 방식
n = int(1)

# <class 'int'>
print(type(n))

# 1
print(n)


# 기본적인 산술 연산
#   복소수를 제외한 모든 숫자 타입은 다음과 같은 연산들을 지원합니다.
#   - `x + y`: x 와 y 의 합
#   - `x - y`: x 와 y 의 차
#   - `x * y`: x 와 y 의 곱
#   - `x / y`: x 와 y 의 몫
#   - `x // y`: x 와 y 의 정수로 내림한 몫
#   - `x % y`: x / y 의 나머지
#   - `-x`: 음의 x
#   - `+x`: 양의 x (x 그대로)
#   - `x ** y` x 의 y 거듭제곱

x = 10
y = 2

# x + y = 12
print('x + y =', x + y)

# x - y = 8
print('x - y =', x - y)

# x * y = 20
print('x * y =', x * y)

# x / y = 5.0
print('x / y =', x / y)

# x // y = 5
print('x // y =', x // y)

# x % y = 0
print('x % y =', x % y)

# -x = -10
print('-x =', -x)

# +x = 10
print('+x =', +x)

# x ** y = 100
print('x ** y =', x ** y)


# 비트 연산
#   비트 연산은 정수에 대해서만 의미가 있습니다.
#   비트 연산의 결과는 무한한 부호 비트를 갖는 2의 보수로 수행되는 것처럼 계산됩니다.
#   이진 비트 연산의 우선순위는 모두 숫자 연산보다 낮고 비교보다 높습니다;
#     일항 연산 `~`` 은 다른 일항 연산들 (`+` 와 `-`) 과 같은 우선순위를 가집니다.
#   아래는 비트 연산을 나열하는데, 우선순위에 따라 오름차순으로 정렬되어 있습니다.
#     - `x | y`: x 와 y 의 비트별 or
#     - `x ^ y`: x 와 y 의 비트별 배타적 or (exclusive or)
#     - `x & y`: x 와 y 의 비트별 and
#     - `x << n`: x 를 n 비트만큼 왼쪽으로 시프트
#     - `x >> n`: x 를 n 비트만큼 오른쪽으로 시프트
#     - `~x`: x 의 비트 반전


# x | y = 10
print('x | y =', x | y)

# x ^ y = 8
print('x ^ y =', x ^ y)

# x & y = 2
print('x & y =', x & y)

# x << y = 40
print('x << y =', x << y)

# # x >> y = 2
print('x >> y =', x >> y)

# ~x = -11
print('~x =', ~x)


# 진법
#   정수형은 다음과 같이 진법을 변환시킬 수 있습니다.
#   - 2진법(bin; 바이너리)
#   - 8진법(oct)
#   - 16진법(hex)


# 각각의 진법들은 아래와 같이 리터럴을 가집니다.

# 10
print(0b1010)
# 10
print(0o12)
# 10
print(0xa)

# 10진법을 n진법으로 변환시킬 때는 아래와 같습니다.

n = 10

# 0b1010
print(bin(n))
# 0o12
print(oct(n))
# 0xa
print(hex(n))


# 정수 타입의 기능
#   아래는 정수 타입의 기능을 설명합니다.


# abs
#   `abs` 함수는 절댓값을 나타냅니다.

# 10
print(abs(-10))
# 10
print(abs(10))


# divmod
#   `x // y`와 `x % y`의 쌍을 나타냅니다.

x = 10
y = 3

# (3, 1)
print(divmod(x, y))


# pow
#   거듭 제곱을 나타냅니다.
#   `**` 연산과 동일한 결과를 나타냅니다.

x = 10
y = 2

# 100
print(pow(x, y))


# bit_length
#   부호와 선행 `0`을 제외하고, 이진수로 정수를 나타내는 데 필요한 비트 수를 돌려줍니다.
#   좀 더 정확하게 말하자면, `x`가 `0`이 아니면, `x.bit_length()`는 `2**(k-1) <= abs(x) < 2**k`를 만족하는 유일한 양의 정수 `k` 입니다.
#   동등하게, 절댓값 `x`가 정확하게 반올림된 로그값을 가질 만큼 아주 작으면,
#   `k = 1 + int(log(abs(x), 2))` 가 됩니다. `x`가 `0`이면, `x.bit_length()`는 `0`을 돌려줍니다.

n = -37
b = bin(n)

bit_length = n.bit_length()

# -0b100101
print(b)
# 6
print(bit_length)


# to_bytes
#   정수를 나타내는 바이트의 배열을 돌려줍니다.
#   바이트는 '파이썬 바이트 타입 튜토리얼'에서 공부할 예정입니다.

n = 1024

b = n.to_bytes(2, byteorder='big')

# b'\x04\x00'
print(b)


# from_bytes
#    주어진 바이트 배열로 표현되는 정수를 돌려줍니다.
#    `byteorder` 인자는 정수를 나타내는 데 사용되는 바이트 순서를 결정합니다.
#    `byteorder`가 `big`인 경우, 최상위 바이트는 바이트 배열의 처음에 있습니다.
#    `byteorder`가 `little`인 경우, 최상위 바이트는 바이트 배열의 끝에 있습니다.

n = int.from_bytes(b'\x00\x10', byteorder='big')

# 16
print(n)


# as_integer_ratio
#   비율이 원래 정수와 정확히 같고 양의 분모를 갖는 정수 쌍을 돌려줍니다.
#   정수(whole numbers)의 정수 비율은 항상 분자가 그 정수이고 분모는 `1`입니다.

n = 10

ratio = n.as_integer_ratio()

# (10, 1)
print(ratio)


# conjugate
#   복소수의 켤레를 나타냅니다.
#   정수 타입에서는 켤레가 값 자체입니다.
#   다시말해, `x + yj`를 `x - yj`로 바꿔도 어떤 정수 타입이든 자기 자신이 반환됩니다.

n = 12

# 12
print(n.conjugate())


# real
#   복소수의 실수 부분를 반환합니다.
#   정수에서는 정수 값 자체가 실수 부분이니 어떤 정수 타입이든 자기 자신이 반환됩니다.

n = 16

# 16
print(n.real)


# imag
#    복소수의 허수 부분을 나타냅니다.
#    정수 타입에서는 허수 부분이 존재하지 않으니 `0`을 반환합니다.

n = 10

# 0
print(n.imag)


# denominator
#   분수를 반환해줍니다.
#   정수에서의 분수는 `1`이므로, 어떤 정수 타입이든 `1`을 반환합니다.

n = 100

# 1
print(n.denominator)
