from tkinter import*
from tkinter import filedialog, messagebox
#from turtle import bgcolor
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import jieba
import numpy as np
from PIL import Image, ImageTk

jieba.set_dictionary('./dict/dict.txt')
jieba.initialize()

win = Tk()
win.title("Text Word Cloud Notepad")
frame_left = Frame(win, relief ="raised",borderwidth=2, bg="white", width=80, height=90)
frame_left.pack(side="left", fill="both",  expand=1)
frame_right= Frame(win, relief="raised", borderwidth=2, bg="white", width=50, height=90)
frame_right.pack(side="bottom",fill="both", expand=1 )

scrollbar1 = Scrollbar(frame_left, orient="horizontal")
scrollbar1.pack(side="bottom", fill="x")
scrollbar2 = Scrollbar(frame_left)
scrollbar2.pack(side="right", fill="y")

textBookLabel = Label(frame_left, width=80, height=1, text='文本编辑区',bg='pink', font=40)
textBookLabel.pack(side="top", fill='both')
textbook = Text(frame_left, width=80, height=80, undo=True, xscrollcommand=scrollbar1.set(0, 0.1), yscrollbar=scrollbar2.set(0, 0.3))
textbook.pack(side="bottom", fill="both")

scrollbar1.config(command=textbook.xview)
scrollbar2.config(command=textbook.yview)

textBookLabelRight = Label(frame_right, width=50, height=1, text='词频统计结果展示区',bg='pink', font=40)
textBookLabelRight.pack(side="top", fill='both')
listbox = Text(frame_right, width=50, height=80)
listbox.pack(side="bottom",  fill="both")
txt = textbook.get(1.0, "end")

def openfile():
    global txt
    textbook.delete(1.0, "end")
    filename = filedialog.askopenfilename()
    if filename != None:
        f = open(filename, "r")
        txt = f.read()
        f.close()
        textbook.insert("insert", txt)
    else:
        messagebox.showinfo("提示", "文件名错误")
        
def saveasfile():
    save()
    filename_save = filedialog.asksaveasfilename()
    if filename_save != None:
        with open(filename_save, "w") as f_save:
            f_save.write(textbook.get(1.0, "end"))
        f_save.close()
        messagebox.showinfo("提示", "另存完成！")
    else:
        messagebox.showinfo("提示", "文件名错误！")

def window_quit():
    if textbook.get(1.0, "end") != txt and txt!='':
        handleprotocol()
    else:
        win.destroy()
        
def handleprotocol():
    if messagebox.askokcancel("提示", "需要保存修改吗？") == True:
        save()
        win.destroy()
    else:
        win.destroy()
        
def wordsnumber():
    dct = {}
    txt_count = textbook.get(1.0, "end")
    word_count = jieba.lcut(txt_count)
    for word in word_count:
        if len(word) == 1:
            continue
        dct[word] = dct.get(word, 0) + 1
    items = list(dct.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for w in range(len(items)):
        listbox.insert("end", "{0} : {1}\n".format(items[w][0], items[w][1]))
        if w > 100:
            break
        
def generate_wordcloud():
    txt_cloud = textbook.get(1.0, "end")
    words = jieba.lcut(txt_cloud)
    newtext = "".join(words)
    if messagebox.askokcancel("提示", "是否生成自定义样式的词云？") == False:
        wordcloud = WordCloud(background_color="white", font_path="./SIMKAI.TTF",max_font_size=20, width=600, height=400, scale=5).generate(newtext)
    else:
        bg_pic_path = filedialog.askopenfilename()
        if bg_pic_path != None:
            mask = np.array(Image.open(bg_pic_path))
            wordcloud = WordCloud(background_color="white", font_path="./SIMKAI.TTF",max_font_size=20, width=600, height=400, scale=5, mask=mask).generate(newtext)
        else:
            messagebox.showinfo("提示", "未选择图片，请重试！")
            return
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    if messagebox.askokcancel("提示", "是否将词云图片导出？") == False:
        return
    filename_save = filedialog.asksaveasfilename()
    if filename_save != None:
        wordcloud.to_file(filename_save+'.png')
        messagebox.showinfo("提示", "词云图片已经保存到目录: "+filename_save+"！")
    else:
            messagebox.showinfo("提示", "文件名错误")
    
    
    
def showpopmenu(event):
    popmenu.post(event.x_root, event.y_root)

def cut():
    global content
    content = textbook.get(SEL_FIRST, SEL_LAST)
    if content == None:
        return
    else:
        textbook.delete(SEL_FIRST, SEL_LAST)
        return content
    
def copy():
    global content
    content = textbook.get(SEL_FIRST, SEL_LAST)
    return content

def paste():
    global content
    textbook.insert("insert", content)
    
def save():
    textbook.tag_add(textbook.get(1.0, "end"), 1.0, "end")

def redo():
    textbook.edit_redo()
    
def undo():
    textbook.edit_undo()
    
def select_all():
    textbook.tag_add("sel", 1.0, "end")

def about():
    if messagebox.showinfo("about", "copyright by keviness") == True:
        pass
    

topmenu = Menu(win)
filemenu = Menu(topmenu, tearoff=False)
filemenu.add_command(label="打开", command=openfile)
filemenu.add_command(label="另存为", command=saveasfile)
topmenu.add_cascade(label="文件",menu=filemenu)

editmenu = Menu(topmenu, tearoff=False)
editmenu.add_command(label="剪切", command=cut)
editmenu.add_command(label="复制",  command = copy)
editmenu.add_command(label="粘贴", command = paste)
editmenu.add_command(label="保存", command=save)
editmenu.add_separator()
editmenu.add_command(label="撤销", command=undo)
editmenu.add_command(label="恢复", command=redo)
editmenu.add_command(label="全选", command=select_all)
topmenu.add_cascade(label="编辑", menu=editmenu)


functionmenu = Menu(topmenu, tearoff=False)
functionmenu.add_command(label="统计词频", command=wordsnumber)
functionmenu.add_command(label="生成词云", command=generate_wordcloud)
#functionmenu.add_command(label="展示图片", command=showpicture)
topmenu.add_cascade(label="功能", menu=functionmenu)

aboutusmenu = Menu(topmenu, tearoff=False)
aboutusmenu.add_command(label="关于", command=about)
topmenu.add_cascade(label="关于", menu=aboutusmenu)
win.config(menu=topmenu)

popmenu = Menu(win, tearoff=False)
popmenu.add_command(label="打开", command=openfile)
#popmenu.add_command(label="展示图片", command=showpicture)
popmenu.add_command(label="统计词频", command=wordsnumber)
popmenu.add_command(label="生成词云", command=generate_wordcloud)
popmenu.add_separator()
popmenu.add_command(label="剪切", command=cut)
popmenu.add_command(label="复制", command=copy)
popmenu.add_command(label="粘贴", command=paste)
popmenu.add_command(label="保存", command=save)
popmenu.add_separator()
popmenu.add_command(label="撤销", command=undo)
popmenu.add_command(label="恢复", command=redo)
popmenu.add_command(label="全选", command=select_all)
textbook.bind("<Button-3>", showpopmenu)

win.protocol("WM_DELETE_WINDOW", window_quit)

win.mainloop()
print("hello")
#time.sleep(200)