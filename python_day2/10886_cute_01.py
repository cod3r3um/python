'''
1. 설문조사를 한 사람의 수: 5
2. 인원수만큼 반복해서 입력받아 리스트에 추가: for, append
3. 리스트의 요소수만큼 반복해서: for
    cute이면 카운트증가: if
4. cute의 수가 not cute 보다 크다면 "cute" 라고 출력: if
'''

number = int(input("설문조사 인원수를 입력하세요. > "))
count = 0

# 입력
answer = []
for i in range(number):
    answer.append(input("준희가 귀엽다면 1, 귀엽지 않다면 0으로 응답하세요. > "))

# 처리
for t in answer:
    if t == "1":
        count = count+1

# 출력
print("The truth is...", answer)
if count > number - count:
    print("You are cute!")
elif count == number-count:
    print("You are just okay...")
else:
    print("You are NOT cute.")