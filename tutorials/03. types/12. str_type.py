

# 유니코드 문자열(str)
#   일련의 문자들을 가지는 시퀀스 문자 컨테이너 타입입니다.
#   파이썬 3.x 버전부터 str 타입은 기본적으로 유니코드를 지원합니다.


# 리터럴 선언 방식
#   작은 따옴표(')를 사용하거나 큰 따옴표(")를 사용합니다.
s = 'Python'
s = "Python"

# <class 'str'>
print(type(s))

# Python
print(s)


# 문자열 서식 지정자
#   문자열에는 여러 서식이 존재합니다.
#     - u'': 유니코드 문자열. 파이썬 3.x버전부터 기본적으로 제공하기에 생략해도 무관
#     - b'': 아스키(ASCII) 문자로 구성된 바이트(bytes) 문자열. 'bytes_type.py'에서 공부할 예정
#   포맷(format)
#     문자열 포맷을 지정하는 다양한 방식입니다.
#     - `%` 식별자
#         1. %d: decimal의 약어로, 10진수 정수를 지정
#         2. %xd: `10진수의 자리수 - x`만큼 문자열 정렬
#         3. %f: fixed point의 약어로, 고정 소수점을 지정
#         4. %.xf: `x` 자리만큼 고정 소수점을 지정
#         5. %s: string의 약어로, 문자열 삽입
#         6. %xs: `문자열의 자리수 - x` 만큼 문자열 정렬
#     - f'': 파이썬 3.6 이상부터 지원하는 포맷 문자열이며 f'{식별자}'를 통해 문자열로 변환해줌

s = u'유니코드 문자열'

# <class 'str'>
print(type(s))

# 유니코드 문자열
print(s)

s = b'bytes string'

# <class 'bytes'>
print(type(s))

# b'bytes string'
print(s)


s = 'decimal is %d' % 150

# decimal is 150
print(s)

s = 'number %5d' % 100

# number   100
print(s)

s = 'floating point is %f' % 10.234

# floating point is 10.234000
print(s)

s = 'fixed point is %.2f' % 3.1415

# fixed point is 3.14
print(s)

s = 'Hi, %s' % 'Python'

# Hi, Python
print(s)

s = 'Hi, %10s' % 'Python'

# Hi,     Python
print(s)

version = '3.9.1'
chapter = 12
subject = 'str types'

s = f'My Python Version is {version}.\n'\
     f'Chapter {chapter}. {subject}'

# My Python Version is 3.9.1.
# Chapter 12. str types
print(s)


# 이스케이프(Escape) 문자
#   이스케이프 문자는 이스케이프 시퀀스를 따르는 문자들로서 다음 문자가 특수 문자임을 알리는 백슬래시(\)를 사용합니다.
#   - \n: 줄바꿈 (개행문자; linefeed)
#   - \b: 백스페이스(backspace)
#   - \t: 탭(tab)
#   - \f: 폼피드(formfeed)
#   - \r: 캐리지 리턴(carriage return)
#   - \\: 역슬래시(\; backslash)
#   - \': 작은 따옴표(single quote)
#   - \": 큰 따옴표(double quote)


# Hello
# Python!
print('Hello\nPython!')

# HellPython!
print('Hello\bPython!')

# Hello   Python!
print('Hello\tPython!')

# Hello
#     Python!
print('Hello\fPython!')

# Python!
print('Hello\rPython!')

# Hello\Python!
print('Hello\\Python!')

# 'Hello Python!'
print('\'Hello Python!\'')

# "Hello Python!"
print('\"Hello Python!\"')


# 문자열의 기능
#   아래는 문자열의 기능들에 대해 설명합니다.

# isdecimal
#   해당 문자열이 10진수 정수면 참, 아니면 거짓을 반환합니다.
isdecimal = '10'.isdecimal()

# True
print(isdecimal)


# isdigit
#   해당 문자열이 숫자이면 참, 아니면 거짓을 반환합니다.
isdigit = '10'.isdigit()

# True
print(isdigit)


# isascii
#   해당 문자열이 아스키(ASCII) 문자열이면 참, 아니면 거짓을 반환합니다.
isascii = 'abcd'.isascii()

# True
print(isascii)


# isidentifier
#   해당 문자열이 파이썬에 정의된 키워드(keyword)면 참, 아니면 거짓을 반환합니다. 
is_identifier = 'import'.isidentifier()

# True
print(is_identifier)


s = 'this is PYthon TUTORIAL'


# title
#   문장의 첫 단어마다 대문자로 바꾸고 나머지는 소문자로 바꿔줍니다.
title = s.title()

# This Is Python Tutorial
print(title)


# capitalize
#   문장의 첫 단어를 제외한 나머지를 소문자로 바꿔줍니다.
capitalize = s.capitalize()

# This is python tutorial
print(capitalize)


# casefold
#   모든 문자열을 소문자로 바꿔줍니다.
casefold = s.casefold()

# this is python tutorial
print(casefold)


# center
#   첫번째 인자 `width` 만큼 두번째 인자 `fillchar` 문자를 채워넣습니다.
center = s.center(40, '!')

# !!!!!!!!this is PYthon TUTORIAL!!!!!!!!!
print(center)


# count
#   문자열 안에 인자값에 해당하는 문자의 갯수를 반환합니다. 
count = s.count('i')

# 2
print(count)


# encode
#   해당 유니코드 문자열을 바이트 문자열로 인코딩합니다.
encode = s.encode()

# b'this is PYthon TUTORIAL'
print(encode)


# startswith
#   문자열의 첫번째 문자가 인자값에 해당하는 문자와 일치하면 참, 아니면 거짓을 반환합니다.
startswith = s.startswith('t')

# True
print(startswith)


# endswith
#   문자열의 마지막 문자가 인자값에 해당하는 문자와 일치하면 참, 아니면 거짓을 반환합니다.
endswith = s.endswith('L')

# True
print(endswith)


s2 = 'Hello,\tThis is Python Tutorial!\tStudy is very funny!'


# expandtabs
#   문자열에 있는 탭(tab)의 크기를 인자값만큼 늘립니다. 
expandtabs = s2.expandtabs(10)

# Hello,    This is Python Tutorial!      Study is very funny!
print(expandtabs)

