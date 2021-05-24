# 입력받은 두 수가 모두 10보다 큰지 검사

n1, n2 = map(int, input("두 수를 입력하세요. > ").split())
if n1>10 and n2>10 :
    print("모두 10보다 크다")
else:
    print("모두 10보다 크지는 않다")
print("The end")