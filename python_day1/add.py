# 두 수를 입력받아서 덧셈 처리를 하고 결과를 출력
# 1. 첫 번째 수 입력 > input
# 2. 두 번째 수 입력
# 3. 덧셈 +
# 4. 결과 출력 > print

num1 = float(input("첫 번째 숫자를 입력하세요. > "))
num2 = float(input("두 번째 숫자를 입력하세요. > "))
total = num1 + num2
print(num1, "+", num2, "=", total)

print()

print("num1", "=", type(num1))
print("num2", "=", type(num2))
print("total", "=", type(total))