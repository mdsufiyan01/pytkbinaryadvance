
from tkinter import *
from tkinter import messagebox as letter
from tkinter import filedialog

#opening file "history" it will open history file if exists and if its didn'ty it will create one
fileh=open("historydoc.txt",'w')
fileh.close()

def showdata():
    fileh=open("historydoc.txt",'a+') #openining "history" file 
    txttext = fill.get()  #getting entries from entry field
    txt=txttext.upper()
    output=' '.join(format(ord(x), 'b') for x in txttext) # converting to binary
    if (txttext == ""):
        letter.showerror("Empty Entry Box","Please Write Something in Entry Box !!")
    else:
        data.insert(0.0,txt+" = "+output +"."+'\n') # printing value to databox  
        fill.delete(0, END)  # clearing entry
        zz=txt+" = "+output +"."+'\n'
        fileh.write(zz+'\n') # printing conversion history to "history" file
        fileh.close() #Closiing it 
def popup():
    r2=letter.askquestion("Exit","Do You Really Want To Exit? ")
    if r2 == 'yes' :
        root.destroy()     
    else:
        data.insert(0.0,"")        
def about():
    def forwin2():
        po2.destroy()
    po2=Tk()
    po2.title("About Binary Converter")
    abel2=Label(po2,text="""               WELCOME To String to Binary Converter
    ***** HOW TO USE  *****
1)Use entry field to insert data like alphabet,word and small sentences.
2)Use button given below to convert them into binary.
3)Refresh your GUI using refresh option from menubar.
4)Many more feature available in menubar.
5)Clear entry with just one click.


 Thanks for using my GUI
 
 DESCLIMER: Try to use only strings Decimals may show
     incorrect  value""")
    abel2.pack()
    bu1=Button(po2,text="  OK  ",font=('Helvetica 14 bold italic'),command=forwin2)
    bu1.pack()
    
def history():
    def clearhis():
            jh2=data2.get("1.0","end-1c")
            if jh2=="":
                letter.showinfo("Clear  HISTORY...","There is nothing in History..")
            else:
                r=letter.askquestion("Clear  HISTORY...","Do You Really Want To Clear All History....?")
                if (r == 'yes') :
                    data2.delete(1.0,END)
                    fileh=open("historydoc.txt",'w')
                    fileh.close()
                else:
                    data2.insert(0.0,"")
    def exithis():
        loot.destroy()
    loot=Tk() # creating history window in tkinter
    loot.title("History")
    fileh=open("historydoc.txt",'r+') #opening history
    mno=fileh.read()#exoprting data from file to tkinter window
    label9=Label(loot,text="    Conversion History    ",bg="cyan",font=('Time 15 bold'))
    label9.pack()
    scroll2 = Scrollbar(loot)
    scroll2.pack(side=RIGHT, fill=Y)
    data2 =  Text(loot, width=50, height=20, yscrollcommand = scroll2.set)
    scroll2.config(command=data2.yview)
    data2.insert(0.0,mno)
    data2.pack()
    button12=Button(loot,text="  Exit history  ",bg="powder blue",font=('Helvetica 12 bold italic'),command=exithis)
    button12.pack(side=LEFT)
    button22=Button(loot,text="Clear history",bg="powder blue",font=('Times 12 bold'),command=clearhis)
    button22.pack(side=RIGHT)
 
    fileh.close()# closing history

    
def b():
    jh=data.get("1.0","end-1c")
    if jh=="":
        letter.showerror("Empty data box","Data box is Already Empty")
    else:
        r=letter.askquestion("Clear All Stored Data...","Do You Really Want To Clear All Data....?")
        if (r == 'yes') :
            data.delete(1.0,END)     
        else:
            data.insert(0.0,"")
      
def value():
    def fowin():
        win.destroy()
    win=Tk()
    win.title("Alphabet value in Binary ")
    abel=Label(win,text="""Spacebar = 100000.
            A = 1000001.
            B = 1000010.
            C = 1000011.
            D = 1000100.
            E = 1000101.
            F = 1000110.
            G = 1000111.
            H = 1001000.
            I = 1001001.
            J = 1001010.
            K = 1001011.
            L = 1001100.
            M = 1001101.
            N = 1001110.
            O = 1001111.
            P = 1010000.
            Q = 1010001.
            R = 1010010.
            S = 1010011.
            T = 1010100.
            U = 1010101.
            W = 1010111.
            X = 1011000.
            Y = 1011001.
            Z = 1011010.""",font=(' 14 '))
    abel.pack()
    bu6=Button(win,text="  OK  ",font=('Helvetica 12 bold italic'),command=fowin)
    bu6.pack()
    

def refresh ():
    fill.delete(0, END)
    data.delete(1.0,END)
    

def remove():
    ab=fill.get()
    if ab=="" :
        letter.showerror(" Empty Entry box","Entrybox is Already Blank !! ")
    else:
        fill.delete(0, END)
def chose():
    def can():
        fi.destroy()
    file5=filedialog.askopenfile(mode='r')
    def back():
        file5=filedialog.askopenfile(mode='r')
        can()
    def done():
         jh2=data5.get("1.0","end-1c")
         outpu2t=' '.join(format(ord(x), 'b') for x in jh2)
         data.insert(0.0,"Chosen File"+" = "+outpu2t +"."+'\n') 
         can()
        
    if file5 is not None:
        fi=Tk()
        fi.title("Preview Choosed")
        lalal=Label(fi,text="Please Dont Choose big file \n It may Cause Freeze While Processing",fg="green",font=('Times 12 bold'))
        lalal.pack()
        values4=file5.read()
        scroll5 = Scrollbar(fi)
        scroll5.pack(side=RIGHT, fill=Y)
        data5 =  Text(fi, width=50, height=20, yscrollcommand = scroll5.set)
        scroll5.config(command=data5.yview)
        data5.pack()
        data5.insert(0.0,values4)
        bat=Button(fi,text="  Cancel  ",bg="red",fg="white",font=('Helvetica 12 bold italic'),command=can)
        bat.pack(side=LEFT)
        but2=Button(fi,text="Back",bg="white",fg="blue",font=('Times 12 bold'),command=back)
        but2.pack()
        but2=Button(fi,text="OK",bg="red",fg="white",font=('Times 12 bold'),command=done)
        but2.pack(side=RIGHT)
        

    else:
       data.insert(0.0," please choose")        

root = Tk()
root.title("String  To BINARY  Converter ")
mla=Label(root,text="WELCOME ",font=("Algerian",15))#welcome txt using label widget
mla.pack()
mla4=Label(root,text="<= Enter String Below =>")
mla4.pack()
mla2=Label(root,text="---------------------------------------------------------------------------------------------------------------------------------------",font=("Algerian",7))
mla2.pack()
root.iconbitmap("logo.ico")
enterybox = Frame(root)
fill = Entry(enterybox,width=45,font=' 13',bg="powder blue")# creating entry field
fill.pack(side=LEFT)

butt = Button(enterybox, text=" Clear",bg="white",fg="red",font=('Time 10 bold'),command=remove)
butt.pack(side=RIGHT)#clear entry button
enterybox.pack(side = TOP)
buttonbox = Frame(root)
mla22=Label(buttonbox,text="---------------------------------------------------------------------------------------------------------------------------------------",font=("Algerian",7))
mla22.pack(side=TOP)
butt2 = Button(buttonbox, text="Chose from Saved ",bg="white",fg="red",font=("Algerian",14),command=chose)
butt2.pack(side=LEFT)


button = Button(buttonbox, text="    Convert To Binary ",bg="white",fg="blue",font=("Algerian",14),command=showdata)
button.pack()# conversion button

buttonbox.pack(side = TOP)

databox = Frame(root)#frame for databox

scroll = Scrollbar(databox)#scroolbar to frame 
scroll.pack(side=RIGHT, fill=Y)
data =  Text(databox, width=50, height=20, yscrollcommand = scroll.set)
scroll.config(command=data.yview)


data.pack()




databox.pack()
w =Label(root, text=" NOTE: 100000 Refers To Spacebar Input",font="helvetica 8 bold")
w.pack()




button1=Button(root,text="  Exit  ",bg="red",fg="white",font=('Helvetica 12 bold italic'),command=popup)
button1.pack(side=LEFT)#exit button
button2=Button(root,text="Clear Data",bg="red",fg="white",font=('Times 12 bold'),command=b)
button2.pack(side=RIGHT)#clear data button



menubar=Menu(root)#creating menu bar

em=Menu(menubar,tearoff=0)
em.add_command(label="Refresh GUI",command=refresh)
em.add_separator()
em.add_command(label="Exit",command=popup)



menubar.add_cascade(label="Edit",menu=em)

fm=Menu(menubar,tearoff=0)
fm.add_command(label="View Alphabet Value",command=value)
fm.add_command(label="Clear Data",command=b)


menubar.add_cascade(label="Option",menu=fm)

rm=Menu(menubar,tearoff=0)
rm.add_command(label="Convert To Binary",command=showdata)
rm.add_command(label="Clear Entry",command=remove)


menubar.add_cascade(label="Run",menu=rm)
hm=Menu(menubar,tearoff=0)
hm.add_command(label="About",command=about)
hm.add_command(label="conversion(History).",command=history)
menubar.add_cascade(label="Help",menu=hm)


root.config(menu=menubar)
coder=Label(root,text="CREATED:16/12/20020 (mdsufiyan) ",font="times 10 bold")
coder.pack()



root.mainloop()#putting every thing to mainloop


