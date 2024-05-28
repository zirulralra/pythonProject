#lab 3-1
x1 = int(input("첫 번째 점의 x 좌표 : ")) #좌표를 사용자에게 입력받음.
y1 = int(input("젓 번째 점의 y 좌표 : "))
x2 = int(input("두 번째 점의 x 좌표 : "))
y2 = int(input("두 번째 점의 y 좌표 : "))

Distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 #Distance 변수에 거리 저장. 두 점 사이의 거리 공식을 이용한다.
#(x2-x1 값의 제곱) + (y2-y1 값의 제곱) 의 루트 값.(0.5제곱)
Distance = round(Distance, 2) #소수점 둘째 자리까지 표시

print("두 점 (", x1, ",", y1,"),","(",x2,",",y2,") 사이의 거리는", Distance, "입니다.")
#거리값을 프린트한다.

