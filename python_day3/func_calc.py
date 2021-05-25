# 백준 10869번
# https://www.acmicpc.net/problem/10869

# 두 수를 입력받아 사칙연산하는 프로그램

def func_calc(num1, num2, op):

    # return 결과를 저장할 변수를 선언
    result = 0

    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1-num2
    elif op == "*":
        result = num1*num2
    elif op == "/":
        result = num1/num2
    return result

i = func_calc(10, 20, "*")
print(i)