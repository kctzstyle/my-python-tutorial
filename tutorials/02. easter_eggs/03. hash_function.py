
# The Hash of Infinity: 314159
print('The Hash of Infinity:', hash(float('inf')))

# The Hash of NaN: 0
print('The Hash of NaN:', hash(float('nan')))


# 설명
#   본래 float('inf') 혹은 float('infinity')는 'inf'를 반환하지만,
#   hash 함수에서는 이렇게 사용할 수 없기 때문에
#   무한대의 의미를 지닌 원주율을 표현한 것입니다.
#   float('NaN')의 경우도 'nan'을 반환하지만,
#   위와 같은 이유로 없음을 의미하는 0을 반환시키도록 한 것입니다.
