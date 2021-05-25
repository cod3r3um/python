# 사각형 면적 계산

# 함수 선언
def rect_area():
    # 가로, 세로 입력
    a, b = map(int, input("가로와 세로 길이를 입력하세요. > ").split())

    # 면적 계산
    r = a * b

    # 결과 출력
    print(r)

# 함수 호출
rect_area()