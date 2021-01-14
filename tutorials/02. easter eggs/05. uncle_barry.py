
from __future__ import barry_as_FLUFL

# SyntaxError: with Barry as BDFL, use '<>' instead of '!='
print(0 != 1)

# True
print(0 <> 1)

# False
print(1 <> 1)


# 설명
#   `__future__` 모듈은 파이썬 2와 3의 버전 차이로 인해 생기는 문제를 방지하고 호환이 되도록 하기 위해 사용하는 모듈입니다.
#   다시말해 파이썬 2에서 3의 기능을 가져와서 사용할 수 있게 해줍니다.
#   위의 구문을 실행하면 python3에서 <> 구문을 활성화 할 수 있습니다.
#   웃긴 점은 `__future__`에서 기능을 가져 와서 역 호환성을 가져야한다는 것입니다.
