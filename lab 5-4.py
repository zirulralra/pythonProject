#lab 5-4
height = float(input("키를 m단위로 입력하세요. ")) #사용자에게 입력받음.
weight = float(input("몸무게를 kg단위로 입력하세요."))

BMI = weight / (height**2) #BMI를 계산한다.

if BMI > 25.0: #범위에 맞게 조건문을 이용하여 출력.
    print("과체중입니다.")
elif 18.5 < BMI <= 25.0:
    print("적정 체중입니다.")
else :
    print('저체중입니다.')