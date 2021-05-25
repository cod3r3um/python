# 최대값 구하기

li = [4, 12, 15, 20, 18]
max_num = li[0]

for i in li:
    if i < max_num:
        continue
    max_num = i
print("최대값은", max_num, "입니다.")