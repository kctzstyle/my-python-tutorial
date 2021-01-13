
# 주석(comment)
#   주석은 주로 코드 혹은 어떤 것에 대한 설명을 하기 위해 작성합니다.
#   주석은 코드를 실행할 때 무시됩니다.
#   이런식으로 해시태그 `#` 기호를 사용하고 한칸 띄어쓰면 됩니다.


# 결과 출력하기
# print
#   콘솔에 해당 입력값을 출력하는 함수입니다.
#   함수에 대해서는 '파이썬 함수 튜토리얼'에서 공부해볼 예정입니다.


# Hello, Python!
print('Hello, Python!')

# 식별자(identifier)
#   변수(value; 파이썬에서는 식별자(identifier) 혹은 이름(name)이라고도 함)를 선언할 때는 `=` 기호를 사용합니다.
#   파이썬에서는 선언과 동시에 값이 대입되기 때문에 바인딩(binding)이라고 합니다.

# 식별자를 선언하는 방식은 다음과 같습니다.
a = 1

# 1
print(a)


# 식별자 정의 규칙
#   1. 식별자는 파이썬에 기본적으로 정의되어 있는 키워드(keywords)와 같은 명칭을 사용할 수 없습니다.
#   2. 아스키(ASCII) 문자 혹은 유니코드(Uni-code) 문자를 사용할 수 있습니다.
#      하지만 유니 코드로 식별자를 사용하는 것은 권장되지 않습니다.
#      아스키 코드란 숫자, 영문자, 특수문자 같은 `1 byte` 크기의 문자를 의미하며
#      유니코드는 한국어, 중국어, 일본어와 같은 `2 byte` 크기의 문자를 의미합니다.
#   3. 식별자 이름 앞에 숫자가 먼저 오면 안 됩니다.
#   4. 특수문자 사용 시 파이썬에 정의되어 있는 기본 연산자와 일치되는 문자는 사용할 수 없습니다.
#      연산자는 '파이썬 연산자' 튜토리얼에서 공부해볼 예정입니다.

# 파이썬에 정의되어 있는 키워드를 확인하려면 다음 코드를 실행해봅니다.
import keyword
kwlist = keyword.kwlist

# [
#    'False', 'None', 'True',
#    '__peg_parser__', 'and',
#    'as', 'assert', 'async',
#    'await', 'break', 'class',
#    'continue', 'def', 'del',
#    'elif', 'else', 'except',
#    'finally', 'for', 'from',
#    'global', 'if', 'import',
#    'in', 'is', 'lambda',
#    'nonlocal', 'not', 'or',
#    'pass', 'raise', 'return',
#    'try', 'while', 'with',
#    'yield'
# ]
print(kwlist)

# 튜토리얼을 진행하면서 각각의 키워드들에 대해 공부해볼 예정입니다.
