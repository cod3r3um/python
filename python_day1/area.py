# 반지름을 입력받아 원의 면적을 계산하는 프로그램
# 원의 면적을 구하는 공식 = (반지름 * 반지름) * 3.14 = (반지름 ** 2) * 3.14

import math
r = float(input("반지름을 입력하세요. > "))
# pi = 3.14
a = r ** 2 * math.pi
print("원의 면적은", a, "입니다.")