import tkinter
import random

words=('ホワイトタイガー','リス','キリン','カピバラ','シカ','馬','レッサーパンダ','ビーバー','アルパカ','アルマジロ','カワウソ','ペンギン','フクロウ','カメ','ヘビ','ヒツジ','ウサギ','カンガルー'
       ,'ヤギ','サル','ゾウ','ワニ','コウモリ','ラクダ','サイ','シマウマ')

root=tkinter.Tk()
cvs = tkinter.Canvas(width=506,height=506)
cvs.pack()
cvs.create_line(5,5,5,505,fill="black",width=5)
cvs.create_line(105,5,105,505,fill="black",width=5)
cvs.create_line(205,5,205,505,fill="black",width=5)
cvs.create_line(305,5,305,505,fill="black",width=5)
cvs.create_line(405,5,405,505,fill="black",width=5)
cvs.create_line(505,5,505,505,fill="black",width=5)

cvs.create_line(5,5,505,5,fill="black",width=5)
cvs.create_line(5,105,505,105,fill="black",width=5)
cvs.create_line(5,205,505,205,fill="black",width=5)
cvs.create_line(5,305,505,305,fill="black",width=5)
cvs.create_line(5,405,505,405,fill="black",width=5)
cvs.create_line(5,505,505,505,fill="black",width=5)


x=55
y=55
count=0
count2=0

for count in range(5): 
    for count in range(5): 
        word=random.choice(words)  
        cvs.create_text(x,y,text=word,fill="black",font=("System",10))
        x=x+100
    x=55
    y=y+100



root.mainloop()