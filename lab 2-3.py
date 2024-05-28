#lab 2-3
Radius = int(input("반지름을 입력하시오: ")) #반지름을 사용자에게 정수형태로 입력받아 변수에 넣음.
Extent = Radius * Radius * 3.14 #원의 넓이를 계산함.
print("반지름이 %dcm인 원의 넓이는 %.2lfcm^2입니다." % (Radius, Extent))
#형식지정자를 이용하여 문자열과 함께 소수점 둘째 자리까지 출력한다.
