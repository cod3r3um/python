# bmi 지수 계산 프로그램
# bmi 지수 = 몸무게(kg) / (신장(m) * 신장(m)) = 몸무게(kg) / (신장(m) ** 2)
# 선출된 값이 18.5 이하면 저체중
# 18.5 ~ 23 정상
# 23 ~ 25 과체중
# 25 ~ 30 비만,
# 30 이상은 고도비만으로 나누어진다.

weight = float(input("몸무게(kg)를 입력하세요. > "))
height = float(input("키(m)를 입력하세요. > "))
bmi = weight / ( height ** 2)
print("당신의 bmi 지수는", bmi, "입니다.")