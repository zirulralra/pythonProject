class Car:
    def __init__(self, speed, color):
        self.speed = speed # 차의 현재 속도를 나타내는 변수를 초기화
        self.color = color # 차의 색상을 나타내는 변수를 초기화

    def drive(self):
        self.speed = 60 # 주행 메서드가 호출되면 속도를 60으로 설정
        print('%s %d km, 주행중입니다.' % (self.color, self.speed)) # 색상과 속도를 출력

    def stop(self):
        self.speed = 0 # 정지 메서드가 호출되면 속도를 0으로 설정
        print("%s 정지했습니다." %(self.color)) # 색상과 함께 정지 메시지를 출력


#차 인스턴스 생성
white_car = Car(0, "white")
white_car.drive()
white_car.stop()

green_car = Car(0, "green")
green_car.drive()
green_car.stop()

yellow_car = Car(0, "yellow")
yellow_car.drive()
yellow_car.stop()