# 함수 선언

# 입력된 갯수만큼 "=" 출력
def print_line(num):
    print("=" * num)
    print("=" * num)

# 두 수 중에 더 큰 수 구하기
# 매개변수: int 값 두 개
def max(a, b):
    result = 0
    # 리턴: 큰 수(int)
    if a > b:
        result = a
    else:
        result = b
    return result

# 합계 구하기
def sum(*a):
    result = 0
    for i in a:
        result += i
    return result