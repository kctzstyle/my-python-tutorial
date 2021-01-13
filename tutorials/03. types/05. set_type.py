
# 세트; 셋(set)
#   수학에서의 `집합`과 동일한 의미를 가집니다.
#   중복된 값을 가지지 않으며 순서를 갖지 않는 컨테이너 타입입니다.


s = {1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5}

# <class 'set'>
print(type(s))
# {1, 2, 3, 4, 5}
print(s)


# add
#   세트에 요소를 추가시킵니다.
#   리스트의 `append`와 동일한 역할을 하지만, 세트는 순서를 가지지 않으므로 요소 추가 시 매핑하여 정렬합니다.
s.add(6)

# {1, 2, 3, 4, 5, 6}
print(s)


# update
#   세트에 여러 요소를 한번에 추가합니다.
#   리스트의 `extend`와 동일합니다.
s.update({7, 8, 9})

# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s)


# pop
#   세트의 마지막 요소를 제거합니다.
#   리스트의 `pop`과 동일합니다.
item = s.pop()

# 1
print(item)
# {2, 3, 4, 5, 6}
print(s)


# remove
#   리스트의 `remove`와 동일합니다.
#   해당하는 요소를 제거합니다.
s.remove(3)

# {2, 4, 5, 6}
print(s)


# discard
#   `remove`와 동일하지만, `remove`는 사용 시 해당하는 요소가 없으면 `KeyError`를 발생하는 반면,
#   `discard`는 해당 요소가 없어도 에러를 발생시키지 않는다는 차이가 있습니다.
s.discard(2)

# {4, 5, 6, 7, 8, 9}
print(s)

s.discard(2)

# {4, 5, 6, 7, 8, 9}
print(s)


# clear
#   리스트의 `clear`와 동일합니다.
#   세트의 요소를 모두 제거합니다.
s.clear()

# set()
print(s)


s = {1, 2, 2, 3, 3, 3, 4, 4, 5, 6}

# copy
#   리스트의 `copy`와 동일합니다.
#   세트 객체를 복제시킵니다.
s2 = s.copy()

# {1, 2, 3, 4, 5, 6}
print(s2)


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}


# union
#   수학에서의 합집합과 동일합니다.
#   해당 이터러블(Iterable; 순회 가능한) 객체의 요소와 합쳐진 새로운 이터러블 객체를 반환합니다.
#   이터러블 객체 중에서는 리스트, 튜플, 세트 등이 있습니다.
uni = s2.union(s1)

# {1, 2, 3, 4, 5, 6, 7, 8}
print(uni)

l = [10, 20, 3, 4, 5, 60]
uni = s2.union(l)

# {3, 4, 5, 6, 7, 8, 10, 20, 60}
print(uni)

t = (10, 11, 12)
uni = s2.union(t)

# {4, 5, 6, 7, 8, 10, 11, 12}
print(uni)


# intersection
#   수학에서의 교집합과 동일합니다.
#   해당 이터러블 객체와 비교하여 같은 요소만 포함된 새로운 이터러블 객체를 반환합니다.
inter = s1.intersection(s2)

# {4, 5}
print(inter)


# difference
#   수학에서의 차집합과 동일합니다.
#   해당 이터러블 객체와 비교하여 다른 요소가 포함된 새로운 이터러블 객체를 반환합니다.
diff = s2.difference(s1)

# {8, 6, 7}
print(diff)


# symmetric_difference 
#   수학에서의 대칭차집합(합집합 - 교집합) 연산자와 동일합니다.
#   해당 이터러블 객체와 비교하여 서로 대칭되는 요소들을 포함한 새로운 이터러블 객체를 반환합니다.
sym_diff = s1.symmetric_difference(s2)

# {1, 2, 3, 6, 7, 8}
print(sym_diff)


# (차집합 or 교집합 or 대칭차집합)_update
#   각 기능에 `_update`가 붙은 함수는 모두 기능을 수행함과 동시에 해당 객체에 요소를 추가 `update` 시킵니다.

s2.difference_update(s1)

# {6, 7, 8}
print(s2)

s2.intersection_update(s1)

# set()
print(s2)

s2.symmetric_difference_update(s1)

# {1, 2, 3, 4, 5}
print(s2)


# 세트 연산자
#   위에 방식대로 할 수 있지만, 세트는 세트만의 고유한 연산자를 가지고 있습니다.
#   - 합집합: `|` 기호
#   - 차집합: `-` 기호
#   - 교집합: `&` 기호
#   - 대칭차집합: `^` 기호

uni = s1 | s2
diff = s1 - s2
inter = s1 & s2
sym_diff = s1 ^ s2

# {1, 2, 3, 4, 5}
print(uni)

# set()
print(diff)

# {1, 2, 3, 4, 5}
print(inter)

# set()
print(sym_diff)


s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}


# issubset
#   해당 이터러블에 대한 부분집합(subset)인지 여부를 확인합니다.
#   즉, 해당 이터러블 객체의 부분집합이라면 참, 아니면 거짓을 나타냅니다. 
result = s1.issubset(s2)

# False
print(result)

result = s2.issubset(s1)

# True
print(result)


# issuperset
#   `issubset`과 반대입니다.
#   해당 이터러블에 대한 상위집합(superset)인지 여부를 확인합니다.
#   즉, 해당 이터러블 객체의 상위집합이라면 참, 아니면 거짓을 나타냅니다.
result = s1.issuperset(s2)

# True
print(result)

result = s2.issuperset(s1)

# False
print(result)


# isdisjoint
#   해당 이터러블에 대한 교집합이 없으면 참, 있다면 거짓을 나타냅니다.
result = s1.isdisjoint(s2)

# False
print(result)

s3 = {6, 7, 8}
result = s1.isdisjoint(s3)

# True
print(result)
