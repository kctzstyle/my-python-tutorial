
# 리스트(list): 순서를 가지는 컨테이너(Container) 타입입니다.
#               여러 가지 요소들을 순서대로 가질 수 있습니다.


l = []

# []
print(l)

# <class 'list'>
print(type(l))

# False
print(l is None)


# index: 해당하는 요소의 인덱스(자리; index)를 반환합니다.
#        인덱스는 0부터 시작합니다.
l = [10, 20, 30, 40, 50]

# 3
print(l.index(40))


# 인덱스에 접근하여 요소를 찾으려면 다음과 같이 합니다.
# list[index]

# 20
print(l[1])


# 요소를 바꿀때 역시 같습니다.
l[3] = 10
# [10, 20, 30, 10, 50]
print(l)


# append: 가장 마지막 인덱스에 요소를 추가합니다.
l = []
l.append(1)
l.append(2)
l.append(3)

# [1, 2, 3]
print(l)

# pop: 가장 마지막 요소를 삭제한 후 반환합니다.
item = l.pop()

# [1, 2]
print(l)

# 3
print(item)


l = [10, 20, 30, 40, 50,]

# insert: 자리수에 해당하는 요소를 삽입합니다.
l.insert(2, 60)

# [10, 20, 60, 30, 40, 50]
print(l)


# remove: 해당하는 요소를 찾은 후 리스트에서 제거합니다.
l.remove(30)

# [10, 20, 60, 40, 50]
print(l)


l = [7, 3, 2, 1, 5, 8, 2, 2, 4, 6, 9]

# sort: 요소를 key에 해당하는 순서대로 정렬합니다.
#       key를 지정하지 않으면 오름차순으로 정렬합니다.
l.sort()

# [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)


# reverse: 요소의 순서를 반대(내림차순)로 정렬합니다.
l.reverse()

# [9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1]
print(l)


# count: 리스트 안에 해당하는 요소의 개수를 반환합니다.
count = l.count(2)

# 3
print(count)


# extend: 리스트에 요소를 추가하여 확장합니다.
#         + 연산과 동일합니다.
l.extend([10, 20, 30, 40, 50])

# [9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 10, 20, 30, 40, 50]
print(l)

l = [1, 2, 3]
l = l + [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
print(l)


# copy: 리스트를 복제합니다.
l2 = l.copy()

# [1, 2, 3, 4, 5, 6]
print(l2)


# clear: 리스트 안의 요소들을 전부 제거합니다.
l.clear()

# []
print(l)


# 멤버십 연산자(membership operator)
# `a in b`라고 했을 때, a라는 요소가 b라는 컨테이너 안에 있다면 참, 아니면 거짓의 결과를 나타냅니다.
# `a not in b`는 그와 반대의 결과를 나타냅니다.

a = 4
b = [1, 2, 3, 4, 5]

# a in b? True
print('a in b?', a in b)
# a not in b? False
print('a not in b?', a not in b)


# 컴프리헨션(comprehension)
# 컴프리헨션은 컨테이너 객체를 보다 더 쉽게 생성할 수 있도록 파이썬에서 지원되는 문법입니다.
# 단순 반복문을 통해 append 하는 코드에 비해 성능도 굉장히 좋아서 파이썬에서 권장되는 문법입니다. 
# 컴프리헨션은 다음과 같이 사용합니다.
# [ 식별자 for 식별자 in 컨테이너 ]

comp = [x for x in [1, 2, 3, 4, 5]]

# [1, 2, 3, 4, 5]
print(comp)
