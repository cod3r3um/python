# 조건에 맞는 갯수 알아보기

cnt = 0
li = [10, 20, 35, 15]
for i in li:
    if i > 20:
        print(i)
        cnt += 1
    if i >= 20:
        print(i)
        cnt += 1
print(cnt, "건")