# ai 시계 문제풀이_1
# https://www.acmicpc.net/problem/2530
# 1. 시, 분, 초 입력
# 2. 조리시간 입력
# 3. 조리시간을 60초로 나누어서 나머지를 구함
# 4. 초(현재시간)에 나머지를 더하고
# 5. 조리시간을 60초로 나누어서 몫을 구함
# 6. 분(현재시간)에 몫을 더함

h, m, s = map(int, input("현재 시각을 입력하세요. > ").split())
time = int(input("조리시간을 입력하세요. > "))

s += int(time % 60)
m += int(time // 60)

print(h, m, s)

