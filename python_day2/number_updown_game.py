# 숫자 맞추기 게임

'''
1. 임의의 수 생성
2. 숫자 입력
3. 입력값이 크다면 크다라고 출력
4.        작으면 작다라고 출력
5.        맞으면 맞다라고 출력하고 프로그램 종료
6. 2~5번까지를 4번 복사해서 반복
7. "게임 오버"라고 출력
'''

import random
com = random.randrange(1,10)

insert = int(input("숫자를 입력하세요. > "))
if com > insert:
    print("입력하신 수가 컴퓨터의 수보다 작습니다.")
elif com < insert:
    print("입력하신 수가 컴퓨터의 수보다 큽니다.")
elif com == insert:
    print("정답입니다.")
    exit()

insert = int(input("숫자를 입력하세요. > "))
if com > insert:
    print("입력하신 수가 컴퓨터의 수보다 작습니다.")
elif com < insert:
    print("입력하신 수가 컴퓨터의 수보다 큽니다.")
elif com == insert:
    print("정답입니다.")
    exit()

insert = int(input("숫자를 입력하세요. > "))
if com > insert:
    print("입력하신 수가 컴퓨터의 수보다 작습니다.")
elif com < insert:
    print("입력하신 수가 컴퓨터의 수보다 큽니다.")
elif com == insert:
    print("정답입니다.")
    exit()

insert = int(input("숫자를 입력하세요. > "))
if com > insert:
    print("입력하신 수가 컴퓨터의 수보다 작습니다.")
elif com < insert:
    print("입력하신 수가 컴퓨터의 수보다 큽니다.")
elif com == insert:
    print("정답입니다.")
    exit()

print("'Game Over'")