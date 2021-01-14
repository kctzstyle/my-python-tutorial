
# dict(딕셔너리; dictionary) 
#   사전 타입은 고유 키와 값의 한 쌍(key-value pair)을 이루는 구조를 가진 컨테이너 타입입니다.
#   `사전`이라는 명칭에서 알 수 있듯 고유 키(key)를 통해 값(value)을 참조(reference)할 수 있습니다.
#   이러한 구조를 매핑(mapping)형 구조라고 합니다.
#   키 값은 고유(unique)한 값을 가져야 합니다.

# 리터럴 선언 방식
d = {}

# 생성자 선언 방식
d = dict()

# <class 'dict'>
print(type(d))

# {}
print(d)


# 키 값을 통해 값 참조하기
d = {'a': 1, 'b': 2}

# 1
print(d['a'])

# 2
print(d['b'])

# 값을 바꿀 때는 다음과 같이 할 수 있습니다.
d['a'] = 3

# 3
print(d['a'])

# 새로운 키-값을 생성할 때는 다음과 같이 할 수 있습니다.
d['c'] = 3

# {'a': 3, 'b': 2, 'c': 3}
print(d)


d = {1: 'one', 2: 'two'}


# setdefault
#   딕셔너리 내에 키-값의 쌍을 추가합니다.
#   값을 따로 지정해주지 않으면 기본 값은 `None`이 됩니다.
default = d.setdefault(3)

# None
print(default)
# {1: 'one', 2: 'two', 3: None}
print(d)

default = d.setdefault(4, 'four')

# four
print(default)
# {1: 'one', 2: 'two', 3: None, 4: 'four'}
print(d)


d = {1: 'one', 2: 'two'}


# update
#   세트의 `update`와 역할은 비슷합니다.
#   딕셔너리 내에 존재하는 키-값의 쌍을 수정합니다.
#   해당 키가 존재하면 키-값의 쌍을 추가합니다.

# 아래처럼 파라미터(parameter)를 지정하는 방식을 키워드(keyword) 방식이라고 하는데, 사용할 때 키 값은 문자열만 가능합니다.
# 파라미터와 키워드 방식은 '파이썬 함수 튜토리얼'에서 공부할 예정입니다.
d.update(three='three')

# {1: 'one', 2: 'two', 'three': 'three'}
print(d)

d.update(three='THREE')

# {1: 'one', 2: 'two', 'three': 'THREE'}
print(d)

# 이터러블 객체를 통해 여러 개의 키-값의 쌍을 추가할 수 있습니다.
d.update([[3, 'three'], [4, 'four']])

# {1: 'one', 2: 'two', 'three': 'THREE', 3: 'three', 4: 'four'}
print(d)


d = {'a': 1, 'b': 2}
keys = ['c', 'd', 'e', 'f']


# fromkeys
#   이터러블 객체 안에 존재하는 요소들을 키 값으로 가지는 새로운 딕셔너리를 생성합니다.
#   이때 기본 값을 정해주지 않으면 기본 값은 `None`입니다.
d2 = d.fromkeys(keys)

# {'c': None, 'd': None, 'e': None, 'f': None}
print(d2)

d2 = d.fromkeys(keys, 10)

# {'c': 10, 'd': 10, 'e': 10, 'f': 10}
print(d2)


# get
#   키 값에 해당하는 값을 가져옵니다.
#   딕셔너리 내에 해당하는 키가 존재하지 않으면 `None`을 반환합니다.
value = d.get('a')

# 1
print(value)

value = d.get('c')

# None
print(value)


# pop
#   키 값에 해당하는 값을 삭제합니다.
value = d.pop('a')

# 1
print(value)

# {'b': 2}
print(d)


d = {'a': 1, 'b': 2}


# popitem
#   리스트의 `pop`과 동일하게 마지막 키-값 쌍의 요소를 삭제하고 튜플로 반환합니다.
item = d.popitem()

# ('b', 2)
print(item)

# {'a': 1}
print(d)


d = {'a': 1, 'b': 2}


# keys
#   딕셔너리 내에 존재하는 모든 키 값을 반환합니다.
keys = d.keys()

# dict_keys(['a', 'b'])
print(keys)


# values
#   딕셔너리 내에 존재하는 모든 값을 반환합니다.
values = d.values()

# dict_values([1, 2])
print(values)


# items
#    딕셔너리 내에 존재하는 모든 키-값 쌍을 각각 튜플로 반환합니다.
items = d.items()


# dict_items([('a', 1), ('b', 2)])
print(items)


# copy
#   리스트의 `copy`와 동일하게 딕셔너리의 모든 요소를 복사하여 새로운 딕셔너리를 생성합니다.
d2 = d.copy()

# {'a': 1, 'b': 2}
print(d2)


# clear
#    리스트의 `clear`와 동일하게 딕셔너리의 모든 요소를 제거합니다.
d.clear()

# {}
print(d)


# 딕셔너리 컴프리헨션
d = {k: v for k, v in [('a', 1), ('b', 2), ('c', 3)]}

# {'a': 1, 'b': 2, 'c': 3}
print(d)
