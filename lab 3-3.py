#lab 3-3
from datetime import datetime
from pytz import timezone

current_time = datetime.now(timezone("GMT"))

print("검증코드를 사용한 현재 시간은 %d시 %d분 %d초 입니다."%(current_time.hour, current_time.minute, current_time.second))

# 여기까지는 검증용 풀그림입니다.

import time
fseconds = time.time() # GMT 기준 1970년 1월 1일 이후 흘러온 전체 초
Hour = (fseconds // 3600) % 24 #전체 초를 한 시간 단위로 나누고 24로 나눈 나머지를 표시하여 몇 시인지 표시.
Minute = (fseconds // 60) % 60 #전체 초를 분 단위로 나누고 60으로 나눈 나머지를 표시하여 몇 분인지 표시.
Seconds = fseconds % 60 #전체 초를 60으로 나눈 나머지를 표시하여 몇 초인지 표시.

print("time()를 사용한 현재 시간은 %d시 %d분 %d초 입니다."%(Hour, Minute, Seconds))
#구한 값을 프린트한다.