# 백준 2577번
# https://www.acmicpc.net/problem/2577

# a, b, c 입력
# 세 수의 곱 계산

a = int(input("첫 번째 숫자를 입력하세요. > "))
b = int(input("두 번째 숫자를 입력하세요. > "))
c = int(input("세 번째 숫자를 입력하세요. > "))

cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# str으로 변환해서 반복문 만들기
for i in str(a * b * c):
# 숫자에 해당하는 리스트의 값을 1 증가
    cnt[int(i)] += 1
for i in cnt:
    print(i)