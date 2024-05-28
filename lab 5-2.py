#lab 5-2
a = 0
while a <= 4 : #다섯 번 반복한다.
    Score = int(input("점수를 입력하세요 : ")) #점수를 입력받는다.
    a += 1
    if Score >= 91: #91점 이상이면 A.
        print(Score,"점은 A입니다.")

    elif Score >= 81: #81점 이상이면 B.
        print(Score, "점은 B입니다.")

    elif Score >= 71:
        print(Score, "점은 C입니다.")

    elif Score >= 61:
        print(Score, "점은 D입니다.")

    else: #위의 if문 중 아무 곳에도 속하지 않으면 F이다.
        print(Score, "점은 F입니다.")