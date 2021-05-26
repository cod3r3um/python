li = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

for el in li:
    print(el)

for el in li:
    for num in el:
        print(num, end=",")

print()

print("마지막 요소는", li[2][2], "입니다.")
print("정중앙에 위치한 요소는", li[1][1], "입니다.")

for i in range(len(li)):
    print(i)

for i in range(len(li)):
    print(li[i])