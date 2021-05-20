import time
#나의 시간감각을 알아보는 예제
input("엔터를 누르고 마음 속으로 10를 셉니다.")
start=time.time()

input("10초 후에 다시 엔터를 눌러주세요.")
end=time.time()

diff=end-start
print("실제 시간:",diff,"초")
print("차이:",abs(diff-10),"초")