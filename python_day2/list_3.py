# 리스트에 요소를 추가/삭제/삽입/조회

friends = ["모니카", "레이첼", "피비"]

# 추가 append()
friends.append("챈들러")
print(friends)

# 삽입 insert(i, v)
friends.insert(0, "조이")
print(friends)

# 조회 [idx]
print(friends[1])

# 수정
friends[1] = "로스"
print(friends)

# 삭제
friends.pop(1)
friends.pop()
print(friends)

del friends[0]
print(friends)

friends.remove("레이첼")
print(friends)

# 모두 제거
friends.clear()
print(friends)

# 검색 in
friends = ["모니카", "레이첼", "피비"]
print("피비" in friends)

# 전체조회 # 리스트 안 요소수 만큼 for문 반복
print(friends)
for n in friends:
    print(n, end="-")

# 요소의 가장 첫 글자만
for n in friends:
    print(n[0])

# 요소의 첫 글자와 나머지 글자들
for n in friends:
    print("{} {}".format(n[0], n[1:]))