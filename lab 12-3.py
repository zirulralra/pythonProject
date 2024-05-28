class TV:
    def __init__(self, state, channel, volume): #TV 초기화
        self.state = state
        self.channel = channel
        self.volume = volume

    def turnOn(self):
        self.state = True #TV가 켜짐.

    def turnOff(self): #TV가 꺼짐.
        self.state = False
        self.channel = 0  # TV가 꺼질 때 채널을 0으로 초기화
        self.volume = 0 # TV가 꺼질 때 볼륨을 0으로 초기화

    def setVolume(self, volume): #TV의 볼륨 설정
        if 0 < volume < 10: #1~9 사이가 아니면 볼륨을 바꾸지 않음.
            self.volume = volume

        if not self.state: #TV가 켜져있지 않으면 볼륨을 바꾸지 않음.
            self.volume = 0

    def setChannel(self, channel): #TV의 채널 설정.
        if 0 < channel < 10:  # 1~9 사이가 아니면 채널을 바꾸지 않음.
            self.channel = channel

        if not self.state: #TV가 켜져있지 않으면 채널을 바꾸지 않음.
            self.channel = 0

state = False #초깃값
vol = 0
ch = 0

strTVOn = "tv on"
strTVOff = "tv off"
strSetVol = "set vol"
strSetCh = "set ch"

tv = TV(state, ch, vol)

while True:
    print('tv state: %s , channel: %d , volume: %d' % (tv.state, tv.channel, tv.volume))
    selOpt = input('Select Function : %s, %s, %s x, %s x: '
                   % (strTVOn, strTVOff, strSetCh, strSetVol))

    if selOpt == 'tv on': #TV 켬
        tv.turnOn()

    if selOpt == 'tv off': #TV 끔
        tv.turnOff()

    if selOpt.startswith('set ch'): #set ch라는 문자열이 입력되면
        ch = int(selOpt[7:]) #문자열에 이어지는 숫자로 채널을 바꾼다.
        tv.setChannel(ch)

    if selOpt.startswith('set vol'): #set vol라는 문자열이 입력되면
        vol = int(selOpt[7:]) #문자열에 이어지는 숫자로 볼륨을 바꾼다.
        tv.setVolume(vol)