# 백준 10886번 문제풀이
# https://www.acmicpc.net/problem/10886

'''
1. 설문조사를 한 사람의 수: 5
2. 인원수만큼 반복해서 입력받아 리스트에 추가: for, append
    1이면 카운트 증가: if
3. cute의 수가 not cute 보다 크다면, "cute" 라고 출력: if
'''

number = int(input("설문조사 인원수를 입력하세요. > "))
count = 0

for i in range(number):
    answer = input("준희가 귀엽다면 1, 귀엽지 않다면 0으로 응답하세요. > ")
    if(answer == '1'):
        count = count + 1

if count > number - count:
    print("cute!")
else:
    print("NOT cute")