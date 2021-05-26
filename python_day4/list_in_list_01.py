li = [[0, 2, 3],
      [4, 1, 6],
      [7, 8, 2]]

for i in range(len(li)):
    for j in range(len(li[i])):
        # i행 j열이 같은 경우만 출력
        if i == j:
            print(li[i][j])