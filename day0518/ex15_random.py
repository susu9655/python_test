import turtle as t
import random
t.shape("turtle")
t.speed(0)
t.color("magenta")
for x in range(500):
    a=random.randint(1,360) #1~360에서 난수를 발생하여 a에 저장
    t.setheading(a) #거북이 머리 방향을 랜덤 숫자 a 각도로 튼다
    b=random.randint(1,50)
    t.forward(b) #b픽셀만큼 진격
t.exitonclick()