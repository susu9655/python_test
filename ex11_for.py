import turtle as t
t.color("red")
t.width(3)

for x in range(3):
    t.fd(100)
    t.lt(120)

t.color("green")
for x in range(4):
    t.fd(100)
    t.lt(90)
t.circle(30) #for문 빠져나와서 원

t.penup()
t.goto(-200,200)
t.color("orange")
n=6
t.begin_fill() #채우기
for x in range(n): #0~5까지 6번이 반복됨
    t.fd(50)
    t.lt(360/n)
t.end_fill()
t.exitonclick()
