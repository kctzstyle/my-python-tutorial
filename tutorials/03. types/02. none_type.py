
# None
#   아무 것도 존재하지 않음을 의미합니다.


# None을 선언할 때는 리터럴 선언 방식만 존재합니다.
x = None

# <class: 'NoneType'>
print(type(x))

# None
print(x)


# None은 참과 거짓이 모두 아니기에 아래의 결과에서 알 수 있듯 `False`가 출력되는 것을 확인할 수 있습니다.

# False
print('None is True?', None is True)
# False
print('None is False?', None is False)

# False
print('None == True?', None == True)
# False
print('None == False?', None == False)
