import turtle as t

#예제1
# n=50
# t.bgcolor("black")
# t.color("green")
# t.speed(0) #0:가장 빠름, 1:가장 느림~10:빠름
# for x in range(n):
#     t.circle(80)
#     t.lt(360/n)

#예제2
# angle=89
# t.bgcolor("black")
# t.color("yellow")
# t.speed(0)
# for x in range(200):
#     t.fd(x)
#     t.lt(angle)

#예제3
t.bgcolor("black")
t.speed(0)
colors=["red","purple","blue","yellow","orange"]
t.width(3)
length=10
while length<500:
    t.fd(length)
    t.pencolor(colors[length%5])
    t.rt(89)
    length+=4


t.exitonclick()