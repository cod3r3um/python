# 함수를 만드는 방법

def greet_3times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print("사샤")
greet_3times()    # 함수 실행 (함수 호출)

print("피비")
greet_3times()

# 함수 선언
def greet():
    for i in range(3):
        print("안녕하세요")

def greet_3times(name, cnt):
    print(name)
    for i in range(cnt):
        print("안녕")

print("start > ")
greet()
greet_3times("사샤", 1)
print("end < ")