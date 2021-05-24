# 점수를 입력받아 등급 계산
# >90 수 >80 우 나머지는 기타

# 입력
score = int(input("점수를 입력하세요. > "))
grade = ""

# 등급 계산 (처리)
if score > 90:
    grade = "수"
elif score > 80:
    grade = "우"
else:
    grade = "기타"

# 결과 (출력)
print("결과 > ", grade)