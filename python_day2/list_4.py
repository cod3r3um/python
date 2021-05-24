# 검색: 모니카
# 있다 혹은 없다로 결과 출력

friends = ["모니카", "레이첼", "피비"]

name = input("이름을 입력하세요. > ").strip()
if name in friends:
    print("있다.")
else:
    print("없다.")