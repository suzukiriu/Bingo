import tkinter
import random

words=('ホワイトタイガー','リス','キリン','カピバラ','シカ','馬','レッサーパンダ','ビーバー','アルパカ','アルマジロ','カワウソ','ペンギン','フクロウ','カメ','ヘビ','ヒツジ','ウサギ','カンガルー'
       ,'ヤギ','サル','ゾウ','ワニ','コウモリ','ラクダ','サイ','シマウマ','トラ')

root=tkinter.Tk()
cvs = tkinter.Canvas(width=506,height=506)
cvs.pack()

x1=5
x2=5
y1=5
y2=5
count=0
for count in range(6):
    cvs.create_line(x1,5,x2,505,fill="black",width=5)
    x1=x1+100
    x2=x2+100

for count in range(6):
    cvs.create_line(5,y1,505,y2,fill="black",width=5)
    y1=y1+100
    y2=y2+100

x=55
y=55
count=0
count2=0

for count in range(5): 
    for count in range(5): 
        word=random.choice(words) 
        num=len(word) 
        print(num)
        if num >= 5:
            cvs.create_text(x,y,text=word,fill="red")
        else:    
             cvs.create_text(x,y,text=word,fill="black",font=("System",1))
        x=x+100
    x=55
    y=y+100



root.mainloop()