# 입력받은 숫자가 홀수이면 홀수라고 출력
# 2로 나눈 값이 1이면 홀수

num = int(input("숫자를 입력하세요. > "))

if(num%2 == 1):
    print("입력하신 숫자는 홀수입니다.")
if(num%2 == 0):
    print("입력하신 숫자는 짝수입니다.")