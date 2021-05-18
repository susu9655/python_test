import turtle
t=turtle.Turtle() #거북이 모양 생성
t.shape("turtle") #모양을 거북이로
#arrow, turtle, circle, square, triangle, classic

t.color("green")
t.forward(100) #앞으로 진격
t.right(90) #90도 돌기
t.forward(100)
t.right(90)
t.forward(100)

turtle.exitonclick() #그래픽창 안 닫히게 하기 위해서 마지막에 추가(클릭시 창 닫힘)