class Circle:
    count = 0
    def __init__(self, radius):
        self.radius = radius # 원의 반지름을 입력받아 인스턴스 변수로 설정
        Circle.count += 1

    def area(self):
        return 3.14 * self.radius ** 2 # 원의 면적을 계산

    def cf(self):
        return 2 * 3.14 * self.radius # 원의 둘레를 계산

# 5개의 원(인스턴스)을 만들어 리스트에 저장
circles = []
for i in range(5): #다섯 번.
    radius = int(input("반지름을 입력하세요: "))
    circle = Circle(radius)
    circles.append(circle)

print("Object의 수는 %d 개 입니다." % (Circle.count))

n = 0
for circle in circles:
    n += 1
    area = circle.area()
    circumference = circle.cf()
    print('%d번 원 - 반지름 : %d, 원의 면적 : %.2f, 원의 둘레 : %.2f '%(n, circle.radius, area, circumference))
