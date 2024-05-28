#lab 3-4
Radius = int(input("밑면의 반지름 길이를 입력 : ")) #사용자에게 값을 입력받음.
Height = int(input("원기둥의 높이 입력 : "))
Pi = 3.14 #파이 값 설정.

Volume = (Radius ** 2 * Pi) * Height #부피를 구해준다. (밑넓이 * 높이)
Area = (Radius ** 2 * Pi * 2) + (Height * (Radius * 2 * Pi)) #겉넓이를 구해준다. ((밑넓이 * 2) + 옆 사각형 넓이)

print("겉넓이 : %.2f, 부피 : %.2f" %(Area, Volume)) #값을 프린트해준다.

