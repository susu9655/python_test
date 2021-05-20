#파이썬의 GUI프로그래밍 하는 방법
import tkinter #window생성에 필요한 라이브러리
t=tkinter.Tk() #TK는 window생성을 하기 위한 함수
t.geometry('300x200') #가로X세로
t.resizable(0,0) #크기 고정

#3개의 라벨을 만든 후 윈도우 프레임에 배치
l1=tkinter.Label(t,text="박스 #1",bg="red",fg="white")
l1.place(x=0,y=0)

l2=tkinter.Label(t,text="박스 #2",bg="green",fg="white")
l2.place(x=20,y=20)

l3=tkinter.Label(t,text="박스 #3",bg="yellow",fg="white")
l3.place(x=40,y=40)

#라벨에 이미지 넣기
img=tkinter.PhotoImage(file='15.png') #png나 gif만 가능함
imgLabel=tkinter.Label(t,image=img)
imgLabel.pack()
t.mainloop() #모든 이벤트나 시스템 이벤트 처리하기 위한 코드