import turtle as t
wn=t.Screen() #스크린생성
wn.setup(600,600,0,0) #w,h,x,y
wn.addshape("s1.JPG") #shape 모양 추가
t.shape("s1.JPG") #shape 변견
t.width(3)
#t.color("red") #직접 색상으로 지정하는 경우

#256 색상으로 직접 주려면
wn.colormode(255)
t.color(0,255,120)
t.write("Have a Good Day!!",align="center",
       font=("Comic Sans MS",30,"bold"))

t.exitonclick()
