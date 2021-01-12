
# 주석(comment)
# 주석은 주로 코드 혹은 어떤 것에 대한 설명을 하기 위해 작성합니다.
# 주석은 코드를 실행할 때 무시됩니다.
# 이런식으로 해시태그 `#` 기호를 사용하고 한칸 띄어쓰면 됩니다.


# import: 별도로 정의되어 있는 파이썬 모듈을 포함시킵니다.

import hi


# 패키지 내부로 접근할 때는 참조 기호(점; dot)를 사용합니다.
# 아래는 `my_package` 안에 있는 `hi.py` 모듈을 사용하는 코드입니다.

import my_package.hi


# from: 패키지 내부의 모듈로 접근할 때 사용합니다.
#       후에 공부할 '제너레이터와 yield'에서 다른 기능을 공부할 것입니다.

from my_package import hello


# as: 패키지 모듈 혹은 클래스(class)에 별칭을 붙여 사용할 수 있도록 해줍니다.
#     클래스는 '파이썬과 객체'와 '객체지향'을 공부할 때 다룰 예정입니다.

from my_package.first import a as b

# 1
print(b)
