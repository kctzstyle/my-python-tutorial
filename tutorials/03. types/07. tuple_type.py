
# 튜플(tuple)
#   리스트와 마찬가지로 순서가 있는 컨테이너 타입입니다.
#   단, 리스트처럼 안의 요소를 변경할 수 없습니다.


t = ()

# <class 'tuple'>
print(type(t))

# 리스트처럼 값을 변경하는 기능은 없기 때문에
# `append`, `pop`, `insert`, `remove` 등의 기능을 사용할 수는 없지만
# `count`, `index`의 기능은 정의되어 있습니다.
# 이 함수들은 리스트에서의 `count`, `index`와 역할도 같습니다.

t = (1, 2, 2, 3, 2, 4, 8, 5)

# 3
print(t.count(2))

# 6
print(t.index(8))


# 제너레이터(generator)
#   튜플은 요소의 값을 변경하고 싶지 않을 경우에도 사용합니다.
#   그러나 튜플을 컴프리헨션을 하게 되면 제너레이터(generator)가 생성이 됩니다.
#   제너레이터를 사용하여 메모리를 보다 더 효율적으로 사용할 수 있도록 해줍니다.
#   제너레이터에 대해서는 '제네레이터와 yield'에서 공부할 예정입니다.

g = (x for x in range(1, 5+1))

# <class 'generator'>
print(type(g))


# next
#   튜플에 저장되어 있는 다음 값을 불러오며 메모리에서 해제하는 함수입니다.
#   순서대로 값을 불러오다가 더 이상 값이 존재하지 않으면 `StopIteration` 예외를 발생시킵니다.
#   리스트의 `pop`과 비슷해 보이지만, 성능면에서 뛰어난 면을 보여줍니다.

# 1
print(next(g))
# 2
print(next(g))
# 3
print(next(g))
# 4
print(next(g))
# 5
print(next(g))
# StopIteration
print(next(g))
