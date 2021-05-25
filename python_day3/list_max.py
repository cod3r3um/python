# 최대값 구하기

# 리스트 안에 있는 가장 큰 숫자 찾기
# 최대값 변수에 리스트의 첫번째 값을 지정
# 리스트 수만큼 반복    : for
# 리스트의 값과 최대값 변수를 비교해서 리스트의 값이 더 크면    : if
# 최대값 변수에 저장
# 최대값 변수 출력

li = [4, 12, 15, 20, 18]
max_num = li[0]

for i in li:
    if i > max_num:
        max_num = i
print("최대값은", max_num, "입니다.")

min_num = li[0]
for i  in li:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i
print("최소값은 {}, 최대값은 {} 입니다.".format(min_num, max_num))