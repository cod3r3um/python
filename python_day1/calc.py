# 백준 10869번 https://www.acmicpc.net/problem/10869
# 두 수를 입력받아 사칙연산하는 프로그램

num1, num2 = map(int, input("두 수를 입력하세요. > ").split(","))

print()

print("두 수의 덧셈은 (", num1+num2, ") 입니다.")
print("두 수의 뺄셈은 (", num1-num2, ") 입니다.")
print("두 수의 곱셈은 (", num1*num2, ") 입니다.")
print("두 수의 나눗셈은 (", num1/num2, ") 입니다.")

print()

print("두 수를 나눈 몫은 (", num1//num2, ") 입니다.")
print("두 수를 나눈 나머지는(", num1%num2, ") 입니다.")