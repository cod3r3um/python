# 백준 10869번 https://www.acmicpc.net/problem/10869
# 두 수를 입력받아 사칙연산하는 프로그램

num1, num2 = map(int, input("두 수를 입력하세요. > ").split())
op = input("연산자 > ")

if op == "+":
    print("두 수의 덧셈은", num1+num2)
elif op == "-":
    print("두 수의 뺄셈은", num1-num2)
elif op == "*":
    print("두 수의 곱셈은", num1*num2)
elif op == "/":
    print("두 수의 나눗셈은", num1/num2)
