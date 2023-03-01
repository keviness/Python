from tkinter import *
window = Tk()
window.title("四五棋")
#画棋盘
canvas = Canvas(window, bg = "SandyBrown", width = 480, height = 480)
canvas.grid(row = 0, column = 0, rowspan = 10)

#画线条
for i in range(15):
    canvas.create_line(30, (30 * i + 30), 450, (30 * i + 30))
    canvas.create_line((30* i + 30), 30, (30 * i + 30), 450)

#画初始的五个星
point_x = [3, 3, 11, 11, 7]
point_y = [3, 11, 3, 11, 7]
for i in range(5):
    canvas.create_oval(30 * point_x[i] + 27, 30 * point_y[i] + 27, 
                       30 * point_x[i] + 33, 30 * point_y[i] + 33, fill = "black")

#设置必要参数
r = 10
click_x=0                 #定义x轴坐标
click_y=0                 #定义y轴坐标
piece_color = "black"     #当前棋子颜色
person_flag = 1           #棋子标志，1为白子，-1为黑子
a_flag = 1                #当一方获胜后，无法在棋盘上点击
mouse_black = []          #黑子坐标存储列表
mouse_white = []          #白子坐标存储列表
mouse = []                #所有棋子坐标存储列表
totala=0
totalb=0
ret=1
#返回鼠标位置
def mouseBack(event):     
    global click_x, click_y
    click_x = event.x
    click_y = event.y
    mouseJudge()
    
#单击左键，返回当前位置    
canvas.bind("<Button-1>",mouseBack) 

#使落点在交叉点处
def mouseJudge():
    global click_x, click_y, person_flag, mouse
    mouse = mouse_black + mouse_white   #将棋子（黑白）坐标全部存进去
    i=0
    j=0
    while click_x > (30+15*i):     #确定鼠标点击位置所在的格子
        i+=1
    while click_y > (30+15*j):
        j+=1
    if ((i%2)==1 and (j%2)==1):      #将一个格子分成四个区域，根据鼠标点击位置所在区域分得格子的顶点
        click_x=30+15*(i-1)                      
        click_y=30+15*(j-1)
    if ((i%2)==1 and (j%2)==0):
        click_x=30+15*(i-1)
        click_y=30+15*j
    if ((i%2)==0 and (j%2)==1):
        click_x=30+15*i
        click_y=30+15*(j-1)
    if ((i%2)==0 and (j%2)==0):
        click_x=30+15*i
        click_y=30+15*j
    if person_flag ==1:
        putPiece("black")
    elif person_flag ==-1:
        putPiece("white")
    
#落子        
def putPiece(piece_color):
    global mouse_black, mouse_white, person_flag, mouse,ret
    ret=1
    if (click_x>=30)and(click_x<=450)and(click_y>=30)and(click_y<=450): #只能在棋谱内产生棋子
        if (click_x, click_y) not in mouse:   #一个点只能产生一个棋子
            if a_flag == 0:
                canvas.create_oval(click_x - r, click_y - r,
                                   click_x + r, click_y + r, 
                                   fill = piece_color, tags = ("piece"))
                person_flag *= -1
                if piece_color == "white":
                    Show(mouse)
                    mouse_white.append( (click_x, click_y) )   #将白子坐标放进白子列表中
                    Judge1(mouse_white) 
                    Tips(mouse)
                elif piece_color == "black":
                    Show(mouse)
                    mouse_black.append( (click_x, click_y) )   #将黑子坐标放进黑子列表中
                    Judge1(mouse_black)
                    Tips(mouse)
            else:
                return 0

#根据连子数判断输赢
def pieceCount(mouse,pieces_count,p,q):
    global piece_count
    if person_flag==-1:   #判断黑子
        for i in range(1,5):
            (x, y) = (click_x + p * 30 * i, click_y + q * 30 * i)
            if (x, y) in mouse_black:
                piece_count+=1
            else:
                break
        return piece_count
    if person_flag==1:   #判断白子
        for i in range(1,5):
            (x, y) = (click_x + p * 30 * i, click_y + q * 30 * i)
            if (x, y) in mouse_white:
                piece_count+=1
            else:
                break
        return piece_count

#从横竖斜三个方向判断输赢
def Judge1(mouse):
    global piece_count, piece_color
    piece_count = 0
    piece_count = pieceCount(mouse,piece_count,-1,0)              #从该落点坐标往左判断
    piece_count = pieceCount(mouse,piece_count,1,0)               #从该落点坐标往右判断
    #除了刚落下的棋子，还连接了三个，则连成了四子
    if  piece_count == 3:
        return 1
    elif  piece_count > 3:
        return 5
    else:
        piece_count = 0
        piece_count = pieceCount(mouse,piece_count,0,-1)          #从该落点坐标往上判断
        piece_count = pieceCount(mouse,piece_count,0,1)           #从该落点坐标往下判断
        if piece_count== 3:
            return 1
        elif  piece_count > 3:
            return 5
        else:
            piece_count = 0
            piece_count = pieceCount(mouse,piece_count,-1,-1)     #从该落点坐标往左上角判断
            piece_count = pieceCount(mouse,piece_count,1,1)       #从该落点坐标往右下角判断
            if piece_count == 3:
                return 1
            elif  piece_count > 3:
                return 5
            else:
                piece_count = 0
                piece_count = pieceCount(mouse,piece_count,1,-1)  #从该落点坐标往右上角判断
                piece_count = pieceCount(mouse,piece_count,-1,1)  #从该落点坐标往左下角判断
                if piece_count ==3:
                    return 1
                elif  piece_count > 3:
                    return 5
                else:
                    return 0

#走棋提示
def Show(mouse):
    var1 = StringVar()
    if person_flag==1:
        piece_canvas = Canvas(window, width = 200, height = 50)
        piece_canvas.grid(row = 0, column = 1)
        piece_canvas.create_oval(100 - r, 30 - r,
                                100 + r, 30 + r,
                                fill = 'black')
        var1.set("执黑轮次")
        label = Label(window, textvariable=var1, font=("宋体",16))
        label.grid(row = 1,column = 1) 
    if person_flag==-1:
        piece_canvas = Canvas(window, width = 200, height = 50)
        piece_canvas.grid(row = 0, column = 1)
        piece_canvas.create_oval(100 - r, 30 - r,
                                100 + r, 30 + r,
                                fill = 'white')
        var1.set("执白轮次")
        label = Label(window, textvariable=var1, font=("宋体",16))
        label.grid(row = 1,column = 1)

#胜方提示
def Tips(mouse):
    var2 = StringVar()
    global a_flag,totala,totalb
    if len(mouse)==224:  #如果棋盘铺满
        if totala>totalb:
            var2.set("黑方%s:%s白方，黑方胜"%(totala,totalb))
            label = Label(window, textvariable=var2, font=("宋体",16))
            label.grid(row = 2,column = 1) 
            a_flag = 1
            return a_flag
        elif totala<totalb:
            var2.set("黑方%s:%s白方，白方胜"%(totala,totalb))
            label = Label(window, textvariable=var2, font=("宋体",16))
            label.grid(row = 2,column = 1) 
            a_flag = 1  
            return a_flag
        else:
            var2.set("黑方%s:%s白方，和棋"%(totala,totalb))
            label = Label(window, textvariable=var2, font=("宋体",16))
            label.grid(row = 2,column = 1)   
            a_flag = 1
            return a_flag
    if  person_flag==-1:
        totala+=Judge1(mouse)
        var2.set("黑方%s:%s白方"%(totala,totalb))
        label = Label(window, textvariable=var2, font=("宋体",16))
        label.grid(row = 2,column = 1) 
        #a_flag = 1
        return a_flag
    if  person_flag==1:
        totalb+=Judge1(mouse)
        var2.set("黑方%s:%s白方"%(totala,totalb))
        label = Label(window, textvariable=var2, font=("宋体",16))
        label.grid(row = 2,column = 1) 
        #a_flag = 1
        return a_flag

#重新开始后，输方先下
def click_reset():
    var3 = StringVar()
    global a_flag, mouse_black, mouse_white, mouse,totala,totalb
    canvas.delete("piece")
    mouse_black = []
    mouse_white = []
    mouse = []
    a_flag=0
    totala,totalb=0,0
    var3.set("          ")
    label = Label(window, textvariable=var3, font=("宋体",16))
    label.grid(row = 2,column = 1) 

#悔棋
def click_return():
    global mouse_black, mouse_white, mouse,person_flag,totala,totalb,ret
    if ret==0:
        return
    canvas.delete("piece")
    ret=0
    var2 = StringVar()
    if person_flag==-1:
        mouse_black.pop()
        mouse=mouse_black+mouse_white
        totala-=Judge1(mouse)
        var2.set("黑方%s:%s白方"%(totala,totalb))
        label = Label(window, textvariable=var2, font=("宋体",16))
        label.grid(row = 2,column = 1)
        
        for i in range(len(mouse_black)):
            canvas.create_oval(mouse_black[i][0]-r,mouse_black[i][1]-r
                              ,mouse_black[i][0]+r,mouse_black[i][1]+r,fill="black",tags="piece")
        for i in range(len(mouse_white)):
            canvas.create_oval(mouse_white[i][0]-r,mouse_white[i][1]-r
                              ,mouse_white[i][0]+r,mouse_white[i][1]+r,fill="white",tags="piece")
        
    if person_flag==1:      
        for i in range(len(mouse_black)):
            canvas.create_oval(mouse_black[i][0]-r,mouse_black[i][1]-r
                              ,mouse_black[i][0]+r,mouse_black[i][1]+r,fill="black",tags="piece")
        mouse_white.pop()
        mouse=mouse_black+mouse_white
        totalb-=Judge1(mouse)
        var2.set("黑方%s:%s白方"%(totala,totalb))
        label = Label(window, textvariable=var2, font=("宋体",16))
        label.grid(row = 2,column = 1)
        
        for i in range(len(mouse_white)):
            canvas.create_oval(mouse_white[i][0]-r,mouse_white[i][1]-r
                              ,mouse_white[i][0]+r,mouse_white[i][1]+r,fill="white",tags="piece")
    person_flag *= -1
    Show(mouse)
    

button1 = Button(window,text="开始/重来",font=('黑体', 10),fg='blue',width=10,height=2,command = click_reset)
button1.grid(row = 4,column = 1)
button2 = Button(window,text="悔 棋",font=('黑体', 10),fg='red',width=10,height=2,command = click_return)
button2.grid(row = 6,column = 1)
var = StringVar()
piece_canvas = Canvas(window, width = 200, height = 50)
piece_canvas.grid(row = 0, column = 1)
piece_canvas.create_oval(100 - r, 30 - r,100 + r, 30 + r,fill = 'black')
var.set("黑棋轮次")
label = Label(window, textvariable=var, font=("宋体",16))
label.grid(row = 1,column = 1) 
window.mainloop()