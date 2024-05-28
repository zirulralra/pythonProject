#lab 7-1
import math #라이브러리를 불러옴.

t = 0

def fine_y(x) : #함수의 y값을 구하는 함수
    y = x * math.exp(x)
    return y
def approx(n) : #함수의 근삿값을 구하는 함수
    t = ((b-a)/n)
    t_area = 0
    for i in range(n): #사용자가 정한 횟수만큼 반복.
        period = ((b-a)/n) #주기는 전체 범위 / 사용자가 정한 횟수
        x = a + (period * t) #x값. 범위 시작 값(a)에 주기 * 사각형의 가로를 곱함.
        y = fine_y(x) #y함수를 이용하여 y값을 구해줌.
        area = period * y #주기 * 높이를 하여 각각의 사각형 넓이를 구해준다.
        t_area = t_area + area #총 넓이를 저장해준다.
        t += 1 #t에 1씩 더해가며 값을 갱신. 주기만큼 x값이 늘어나도록 해줌.
    return t_area

def integral(a,b) : #적분 값을 구하는 함수. 부분적분 이용
    num = (math.exp(a)*(1-a))+(math.exp(b)*(b-1))
    return num

a = int(input("적분 구간을 입력하세요 a : "))
b = int(input("적분 구간을 입력하세요 b : "))
n = int(input("몇 등분할지 입력하세요 n : "))

t_area = approx(n)

#출력해준ㄷ.ㅏ
print("함수 te^t에 대한 구간 %.2f부터 %.2f까지의 적분값은 %.4f %d등분 했을 때의 근삿값은 %.4f입니다." %(a,b,integral(a,b),n,t_area))