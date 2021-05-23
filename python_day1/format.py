# format 함수 연습

money = 5000
print("{0:,} 만원".format(money))       # print(money, "만원") # 콤마
print("{0:10,d} 만원".format(money))    # 10자리로 출력
print("{0:+,} 만원".format(money))      # 부호를 붙여 출력
print("{0:08,d} 만원".format(money))    # 8자리로 출력 + 빈 자리는 0을 채움

print()

menu = "김치찌개"
print("{} 는 {:,} 원 입니다.".format(menu, money))  # = {0}, {1}
print("{1} 는 {0} 원 입니다.".format(menu, money))

print()

print("{메뉴판")
print("-----------------")
print("{0:*^30} 선택하신 메뉴는 {1:,} 원 입니다.".format("팟타이", 12000))
print("{0:*^30} 선택하신 메뉴는 {1:,} 원 입니다.".format("똠얌꿍", 15000))
print("{0:*^30} 선택하신 메뉴는 {1:,} 원 입니다.".format("쌀국수", 7000))
print("-----------------")

print()

avg1 = 89.86
avg2 = 90.2
print("성적")
print("-----------------")
print("평균 1={0:6.1f} 평균 2={1:6.1f}".format(avg1, avg2))    # 전체 6자리, 소숫점은 한자리    # p.98
print("평균 1=%6.1f 평균 2=%6.1f"%(avg1, avg2))
print("-----------------")

print()

print("메뉴판")
print("-----------------")
print("{0:$^18} 선택하신 메뉴는 {1:,} 원 입니다.".format("소고기 쌀국수", 7000))
print("{0:@^18} 선택하신 메뉴는 {1:,} 원 입니다.".format("짜조", 4000))
print("%36s 선택하신 메뉴는 %d 원 입니다."%("파인애플 볶음밥", 9000))
print("-----------------")