'''
{}
key: value
key로 값을 추가하거나 key로 값을 조회/삭제
'''

# 사번, 이름, 이메일
emp = [ ["100", "사샤", "a@a.com"],
        ["101", "피비", "b@a.com"],
        ["102", "모니카", "c@a.com"] ]

# 두 번째 사원의 이름
print(emp[1][1])

# 모든 사원의 이름 출력
for i in range(len(emp)):
    print(emp[i][1])

# 입력한 사원의 이름이 있으면 있다, 없으면 없다 출력
name = input("찾는 이름을 입력하세요. > ")
for i in emp:
    if name == i:
        print("있다.")
    if name != i:
        print("없다.")

# 입력한 사원의 이름이 있으면 있다, 없으면 없다 출력
name = input("찾는 이름을 입력하세요. > ")
find_result = False
for i in range(len(emp)):
    if name == emp[i][1]:
        find_result = True
        break
if find_result:
    print("있다.")
else:
    print("없다.")

# list -> dictionary
emp1 = {"no":"100", "name":"사샤", "mail":"a@a.com"}
print(emp1["name"])

emp_dict = [ {"no":"100", "name":"사샤", "mail":"a@a.com"},
             {"no":"101", "name":"피비", "mail":"b@a.com"},
             {"no":"102", "name":"모니카", "mail":"c@a.com"} ]
print("두 번째 사원의 이름은? > ", emp_dict[1]["name"])