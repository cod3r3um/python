# 리스트 속 요소들을 모두 더해주는 함수 만들기

def my_sum(li):
    total = 0
    for i in li:
        total += i
    return total

print(my_sum([1, 2, 3]))
print(my_sum([3, 3, 3]))