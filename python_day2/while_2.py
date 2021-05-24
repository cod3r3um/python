# 무한 루프와 탈출 조건

cnt = 0
end = input()

while True:
    print("*****")      
    cnt += 1
    if cnt >= 5:
        break

print("'The End'")