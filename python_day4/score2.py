# 학생 4명의 국어, 영어, 수학 성적을 저장
score = [
            [90, 70, 30],
            [40, 50, 50],
            [100, 90, 80],
            [80, 80, 80],
        ]

# 영어 성적의 합을 계산
eng_total = 0
for std in score:
    eng_total += std[1]
print(eng_total)

# 다르게 표현하기
eng_total = 0
for std in range(len(score)):
    eng_total += score[std][1]
print(eng_total)