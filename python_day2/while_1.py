# 무한 루프와 탈출 조건

while True:
    print("반복실행")    # 게임 로직
    input_text = input("종료를 원하시면 'y'를 입력하세요. > ")
    if input_text == 'y':
        break
    
print("'The End'")