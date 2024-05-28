# 단어 수를 출력
f = open('Lab11-2_sample.txt', 'r', encoding='utf-8')

count1 = 0
for line in f:
    words = line.split()
    count1 += len(words)
print("단어 수:", count1)

f = open('Lab11-2_sample.txt', 'r', encoding='utf-8')

# 글자 수, 문장 수를 출력
f = open('Lab11-2_sample.txt', 'r', encoding='utf-8')

count2 = 0
count3 = 0
for line in f:
    count2 += len(line.strip())
    count3 += line.count(".")
print("글자 수:", count2)
print("문장 수:", count3)

f.close()
