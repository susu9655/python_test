import turtle
t=turtle.Turtle() #거북이 모양 생성
t.shape("turtle") #모양을 거북이로
#right->rt forward->fd left->lt
t.color("red")
t.width(5)
t.fd(100)
t.write("앞으로 이동")
t.rt(90)
t.fd(100)
t.color("green")
t.fd(50)
t.lt(90)
t.fd(100)
t.color("magenta")
t.fd(50)
t.rt(45)
t.fd(100)
t.goto(0,0) #맨 처음 있던 자리(정중앙 좌표)
t.circle(40) #반지름이 40인 원
t.penup() #다른 곳에서 그리고자 펜을 뗌
t.goto(100,0)
t.lt(90)
t.fd(50)
t.pendown() #다시 팬 붙임
t.circle(50)
turtle.exitonclick() #그래픽창 안 닫히게 하기 위해서 마지막에 추가(클릭시 창 닫힘)