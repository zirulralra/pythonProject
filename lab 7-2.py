#lab 7-2
n = int(input("정수를 입력하세요 : ")) #입력 받음.
fac = 1

for i in range(1,n): #n-1 까지 반복.
    i += 1 #i에 1씩 더해가며 값을 갱신
    fac *= i #팩토리얼을 구함

print(fac)
