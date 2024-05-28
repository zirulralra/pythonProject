#lab 4-1
List1 = [] #리스트 생성.

#리스트의 요소 다섯 개를 사용자에게 입력받고 즉시 리스트에 추가한다.
res = int(input("리스트의 첫 번째 요소 : "))
List1.append(res)
res = int(input("리스트의 두 번째 요소 : "))
List1.append(res)
res = int(input("리스트의 세 번째 요소 : "))
List1.append(res)
res = int(input("리스트의 네 번째 요소 : "))
List1.append(res)
res = int(input("리스트의 다섯 번째 요소 : "))
List1.append(res)

#입력받은 리스트 출력.
print('\n입력받은 리스트 :', List1)

#리스트 인덱스 번호를 이용하여 평균을 계산한다.
Avg = (List1[0] + List1[1] + List1[2] + List1[3] + List1[4])/5

#편차 계산 과정.
#편차(deviation) : 변량에서 평균을 뺀 값
Deviation1 = List1[0] - Avg
Deviation2 = List1[1] - Avg
Deviation3 = List1[2] - Avg
Deviation4 = List1[3] - Avg
Deviation5 = List1[4] - Avg

#분산 계산 과정.
#편차의 제곱해서 더한 후 구한 평균 (편차 제곱의 평균)
Dispersion = ((Deviation1**2) + (Deviation2**2) + (Deviation3**2) + (Deviation4**2) + (Deviation5**2))/5

#구한 평균과 분산을 출력한다.
print('\n1. 평균 =', Avg, ', 분산 = ', Dispersion)

#역순 리스트 생성
Reverse_List = []
#인덱스 뒷 번호부터 역순 리스트에 추가한다.
Reverse_List.append(List1[4])
Reverse_List.append(List1[3])
Reverse_List.append(List1[2])
Reverse_List.append(List1[1])
Reverse_List.append(List1[0])

#역순 리스트 출력
print('2. 역순 :', Reverse_List)

#가장 작은 요소의 최소값을 0으로 변환
Min = min(List1) #Min 변수에 함수를 이용하여 가장 작은 요소 값을 찾음.
index = List1.index(Min) #인덱스 번호 추출 함수를 이용하여 index 변수에 저장한다.
List1[index] = 0 #요소 값을 변환해줌.
print('3. 최소값 변환 :', List1) #최소값을 변환한 리스트를 출력.