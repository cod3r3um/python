# 백준 10871번
# https://www.acmicpc.net/problem/10871

# 수열 안에서 x보다 작은 수를 모두 출력하는 프로그램
# 입력값: 10 5 / 1 10 4 9 2 3 8 5 7 6

n, x = map(int, input("수열 안의 숫자 갯수와 x값을 입력하세요. > ").split())
li = list(input("수열을 입력하세요. > ").split())
cnt = 0

for i in li:         # 리스트 반복
    if int(i) < x:   # x보다 작으면 카운트 증가
        print(i, end=", ")
        cnt += 1
print("> x보다 작은 수의 갯수는", cnt, "개 입니다.")