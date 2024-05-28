fp=open("Lab11-1_data.txt",'r',encoding='utf-8')#데이터파일불러오기
fpo = open ('datao txt','w',encoding='utf-8') #새파일만들기
hap=0.#합계변수
s=0 #갯수변수
for i in fp:#모든.데이터.더하기
    hap = hap + float(i)
    s=s+1
#합계와.평균쓰기
fpo.write('합계=%.1f'%(hap))
fpo.write ('\navg=%.1f' % (hap/s) )
fp. close ()
fpo. close ()