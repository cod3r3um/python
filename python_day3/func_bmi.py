def bmi(w, h):
    r = w / (h/100 * h/100)
    if r < 18.5:
        i = "저체중"
    elif r < 23:
        i = "정상"
    elif r < 25:
        i = "과체중"
    else:
        i = "고도비만"
    return i

result = bmi(50, 170)
print("결과는", result, "입니다.")