# 세 반의 영어성적

eng = [[90, 70, 30],
       [100, 50],
       [60, 50, 50, 70]]

# 전체 합계
total = 0
for i in range(len(eng)):
    for j in range(len(eng[i])):
        total += eng[i][j]
print(total)
print("=====")

total = 0
for ban in eng:
    for eng_score in ban:
        total += eng_score
print(total)

# 각 반의 합계
print("=====")
print("각 반의 합계")
for ban in range(len(eng)):
    print(ban+1, "반: ", sum(eng[ban]))

# sum 함수 쓰지 않고 각 반의 합계 구하기