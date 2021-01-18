
# 레인지(range)
#   range 객체는 시작(start) 부터 끝(stop)-1 까지 일정한 간격(step)으로 순차적인 요소를 가지는 객체입니다.
#   주로 루프문에서 많이 사용합니다. 


# range 객체는 리터럴 선언 방식이 존재하지 않습니다.

r = range(1, 10)

# <class 'range'>
print(type(r))

# range(1, 10)
print(r)

r = range(0, 10, 2)

# range(0, 10, 2)
print(r)


# 컴프리헨션에 많이 응용되곤 합니다.
l = [x for x in range(1, 10)]
l2 = [x for x in range(1, 10, 2)]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)

# [1, 3, 5, 7, 9]
print(l2)
