# bmi 지수 계산 프로그램
# bmi 지수 = 몸무게(kg) / (신장(m) * 신장(m)) = 몸무게(kg) / (신장(m) ** 2)
# 선출된 값이 18.5 이하면 저체중
# 18.5 ~ 23 정상
# 23 ~ 25 과체중
# 25 ~ 30 비만,
# 30 이상은 고도비만으로 나누어진다.

weight = float(input("몸무게(kg)를 입력하세요. > "))
height = float(input("키(m)를 입력하세요. > "))
bmi = weight / (height/100 * height/100)    # = ( height ** 2 )   
result = ""

if bmi < 18.5:
    result = "저체중"
elif bmi < 23:
    result = "정상"
elif bmi < 25:
    result = "과체중"
else:
    result = "고도비만"

print("bmi 지수는 {} 이고 결과는 {} 입니다.".format(bmi, result))