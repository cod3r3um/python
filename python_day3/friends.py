# 친구 추가, 삭제, 검색 프로그램
# append,  del, in

fr = ["모니카", "레이첼"]
no = "1"

while no != "0":
    no = input("0. 종료 1. 추가 2. 삭제 3. 검색 4. 전체조회 > ")
    if no == "0":
        break
    if no == "1":      # 리스트에 추가 p.146
        name = input("추가할 이름을 입력하세요. > ")
        fr.append(name)
    elif no == "2":    # remove p.152
        name = input("삭제할 이름을 입력하세요. > ")
        fr.remove(name)
    elif no == "3":    # p.154
        name = input("찾을 이름을 입력하세요. > ")
        print(name in fr)
    elif no == "4":    # for문 p.156
        for i in fr:
            print(i)