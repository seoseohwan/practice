gun = 10

def checkpoint(soldiers): #경계근무
    #gun = 20 지역변수
    global gun #전역변수 : 위에있는10을 가져옴
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun  

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계근무 나감 
print("남은 총 :{0}".format(gun))   