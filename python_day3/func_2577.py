# 백준 2577번
# https://www.acmicpc.net/problem/2577

def f_2577(a, b, c):
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in str(a * b * c):
        cnt[int(i)] += 1
    return cnt

li = f_2577(150, 266, 427)
for i in li:
    print(i)