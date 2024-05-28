#lab 5-1
a = float(input("a의 값을 입력하시오.")) #값을 입력받는다.
b = float(input("b의 값을 입력하시오."))
c = float(input("c의 값을 입력하시오."))

Bigger = (-b+((b**2)-4*(a*c))**1/2)/2*a #근의 공식을 이용하여 근 두 개를 구해줌.
Smaller = (-b-((b**2)-4*(a*c))**1/2)/2*a
PrintType = 0

if Bigger == Smaller : #두 근이 같으면 중근으로 간주한다.
    Sentence = "중근"
    PrintType = 0

elif ((b**2)-4*(a*c)) < 0: #판별식을 이용하여 허근인지 실근인지 구한다.
    Sentence = "서로 다른 두 허근"
    real_part = -b / (2 * a)
    imaginary_part = ((abs((b**2) - 4 * a * c))**0.5) / (2 * a)
    PrintType = 1 #출력할 때 i를 이용한 식으로 표현할 수 있게 해준다.

else :
    Sentence = "서로 다른 두 실근" #판별식을 이용함.
    PrintType = 0

if PrintType == 0: #형식 지정자를 이용하여 출력해준다.
    print("방정식%.2f x^2 + %.2f x + %.2f는 %s %.2f 와 %.2f을 갖습니다."%(a, b, c, Sentence, Bigger, Smaller))
elif PrintType == 1:
    print("방정식%.2f x^2 + %.2f x + %.2f는 %s %.2f + %.2fi 와 %.2f - %.2fi을 갖습니다." %(a, b, c, Sentence, real_part, imaginary_part, real_part, imaginary_part))
