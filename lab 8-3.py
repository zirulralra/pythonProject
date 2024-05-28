import numpy as np
import matplotlib.pyplot as plt

a = int(input("Enter a number: ")) #계수를 입력받음.
x = np.arange(-10,10,0.1) #그래프 시작 값, 끝값, 사이의 길이 입력
y = a*x**2

plt.plot(x, y) #그래프 표시
plt.show()
ㄴ