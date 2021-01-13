
# frozenset(프로즌세트)
#   리스트와 역할은 동일하지만, 요소를 바꿀 수 없는 컨테이너 타입은 튜플이 있었다.
#   세트도 마찬가지로 프로즌세트라는 것이 그러하다.
#   이름에서도 알 수 있듯 요소를 변경할 수 없는, 얼어붙은(frozen) 집합이라는 의미를 가지고 있다.

# 프로즌세트는 리터럴 형식이 존재하지 않는다.
# 따라서 생성자(constructor) 방식으로 바인딩을 해야한다.
# 생성자에 대해서는 '파이썬과 객체지향 및 클래스 튜토리얼'에서 공부할 예정이다.

fs = frozenset()

# <class 'frozenset'>
print(type(fs))

# frozenset()
print(fs)


# 세트와의 차이점
#   요소를 변경할 수 있는 기능: `add`, `update`, `discard`, `clear` 등을 사용할 수 없다.
#   나머지 합집합, 차집합, 교집합, 대칭차집합 등은 가능하다.


fs = frozenset({1, 2, 3, 4, 5})


# copy
#   세트의 `copy`와 동일하다.
fs2 = fs.copy()

# frozenset({1, 2, 3, 4, 5})
print(fs2)


fs2 = {3, 4, 5, 6}


# union
#   세트의 `union`과 동일하다.
uni = fs.union(fs2)

# frozenset({1, 2, 3, 4, 5, 6})
print(uni)


# difference
#   세트의 `difference`와 동일하다.
diff = fs.difference(fs2)

# frozenset({1, 2})
print(diff)


# intersection
#   세트의 `intersection`과 동일하다.
inter = fs.intersection(fs2)

# frozenset({3, 4, 5})
print(inter)


# symmetric_difference
#   세트의 `symmetric_differencer`과 동일하다.
sym_diff = fs.symmetric_difference(fs2)

# frozenset({1, 2, 6})
print(sym_diff)
