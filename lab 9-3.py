fpname=input("입력파일이름:")#파일.이름.입력
fp = open(fpname,'r')#파일열기
fpo = open(fpname[0:-4]+ '_copy'+fpname[-4:],'w')
#읽고쓰기
s = fp.read()
fpo.write(s)
fp.close()
fpo.close()