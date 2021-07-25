from tkinter import *
from tkinter.messagebox import *
import math as m
import operator
import speech_recognition as sr
from audio_helper import playaudio
import threading

#code for audio input
r=sr.Recognizer()
my_mic_device=sr.Microphone(device_index=1)

check=True
def awd():
    with my_mic_device as source:
        print("Say what want to you calculate")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    my_string = r.recognize_google(audio)
    print(my_string)

    def get_operator(op):
        return {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            'divided': operator.__truediv__,
            'Mod': operator.mod,
            'mod': operator.mod,
            'power': operator.pow,
        }[op]

    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator(oper)(op1, op2)

    filled=eval_binary_expr(*(my_string.split()))
    textfield.insert(END,filled)

def tick():
    global check
    if check:
        awd()
        tick()
        check=False
    else:
        check=True




#some useful variables
font=('Lucida',20,'bold')
ob=playaudio()

#some imp functions


def all_clear():
    textfield.delete(0,END)

def clear():
    ex=textfield.get()
    ex=ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)

def click_btn_fun(event):
    global p
    print("button clicked")
    b=event.widget
    text=b['text']
    print(text)
    t = threading.Thread(target=ob.speak, args=(text,))
    t.start()
    #ob.speak(text)

    if text=='=':
        try:
            ex = textfield.get()
            ans = eval(ex)
            textfield.delete(0, END)
            textfield.insert(0, ans)

        except Exception as e:
            print("Error..",e)
            showerror("Error",e)

        return 0
    if text=='x':
        textfield.insert(END,"*")
        return


    textfield.insert(END,text)




#createing a window
window=Tk()
window.title("My Calculator")
window.geometry("500x555")
#picture label
pic=PhotoImage(file='img/calculator1.png')
headingLabel=Label(window,image=pic)
headingLabel.pack(side=TOP,pady=10)
#heading label
heading=Label(window,text="My Calculator",font=font)
heading.pack(side=TOP)

#textfield
textfield=Entry(window,font=font,justify=CENTER)
textfield.pack(side=TOP,pady=10,fill=X,padx=10)

#frame creation

butttonFrame=Frame(window)
butttonFrame.pack(side=TOP,padx=10)

#Adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(butttonFrame,text=str(temp),font=font,width=5,relief=SUNKEN,activebackground="orange",
                   activeforeground="white")
        btn.grid(row=i,column=j,padx=5,pady=5)
        temp+=1
        btn.bind("<Button-1>",click_btn_fun)


dotbtn=Button(butttonFrame,text=".",font=font,width=5,relief=SUNKEN,activebackground="red",activeforeground="white")
dotbtn.grid(row=3,column=0,padx=5,pady=5)

zerobtn=Button(butttonFrame,text="0",font=font,width=5,relief=SUNKEN,activebackground="orange",activeforeground="white")
zerobtn.grid(row=3,column=1,padx=5,pady=5)

equalbtn=Button(butttonFrame,text="=",font=font,width=5,relief=SUNKEN,activebackground="red",activeforeground="white")
equalbtn.grid(row=3,column=2,padx=5,pady=5)

plusbtn=Button(butttonFrame,text="+",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
plusbtn.grid(row=0,column=3,padx=5,pady=5)

minusbtn=Button(butttonFrame,text="-",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
minusbtn.grid(row=1,column=3,padx=5,pady=5)

mulbtn=Button(butttonFrame,text="x",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
mulbtn.grid(row=2,column=3,padx=5,pady=5)

divbtn=Button(butttonFrame,text="/",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
divbtn.grid(row=3,column=3,padx=5,pady=5)

allclearbtn=Button(butttonFrame,text="AC",font=font,width=5,relief=SUNKEN,activebackground="blue",
                   command=all_clear,activeforeground="white")
allclearbtn.grid(row=4,column=0,padx=5,pady=5)

modbtn=Button(butttonFrame,text="%",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
modbtn.grid(row=4,column=1,padx=5,pady=5)

clearbtn=Button(butttonFrame,text="<--",font=font,width=12,relief=SUNKEN,
                command=clear,activebackground="blue",activeforeground="white")
clearbtn.grid(row=4,column=2,padx=5,pady=5,columnspan=2)




#binding buttons
plusbtn.bind("<Button-1>",click_btn_fun)
minusbtn.bind("<Button-1>",click_btn_fun)
mulbtn.bind("<Button-1>",click_btn_fun)
divbtn.bind("<Button-1>",click_btn_fun)
modbtn.bind("<Button-1>",click_btn_fun)
zerobtn.bind("<Button-1>",click_btn_fun)
dotbtn.bind("<Button-1>",click_btn_fun)
equalbtn.bind("<Button-1>",click_btn_fun)

def enterclick(event):
    print("enter button clicked")
    e=Event()
    e.widget=equalbtn
    click_btn_fun(e)
textfield.bind("<Return>",enterclick)


###########################################################################################################################
#SCIENTIFIC CALCUALTOR

#functions

sc_frame=Frame(window)

sqrtbtn=Button(sc_frame,text="sqrt",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
sqrtbtn.grid(row=0,column=0,padx=5,pady=5)

powbtn=Button(sc_frame,text="^",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
powbtn.grid(row=0,column=1,padx=5,pady=5)

factbtn=Button(sc_frame,text="x!",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
factbtn.grid(row=0,column=2,padx=5,pady=5)

radbtn=Button(sc_frame,text="toRad",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
radbtn.grid(row=0,column=3,padx=5,pady=5)

degbtn=Button(sc_frame,text="toDeg",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
degbtn.grid(row=1,column=0,padx=5,pady=5)

sinbtn=Button(sc_frame,text="sin",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
sinbtn.grid(row=1,column=1,padx=5,pady=5)

cosbtn=Button(sc_frame,text="cos",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
cosbtn.grid(row=1,column=2,padx=5,pady=5)

tanbtn=Button(sc_frame,text="tan",font=font,width=5,relief=SUNKEN,activebackground="blue",activeforeground="white")
tanbtn.grid(row=1,column=3,padx=5,pady=5)

def cal_sc(event):
    print("btn..")
    btn=event.widget
    text=btn["text"]
    ans=""
    ex=textfield.get()
    print(text)
    t = threading.Thread(target=ob.speak, args=(text,))
    t.start()
    if text=='toDeg':
        print("cal degree")
        ans=str(m.degrees(float(ex)))

    elif text=='toRad':
        print("radian")
        ans=str(m.radians((float(ex))))

    elif text=='x!':
        print("cal factorial")
        ans=str(m.factorial(int(ex)))
    elif text=='sin':
        print("cal sin")
        ans=str(m.sin(m.radians(int(ex))))
    elif text=="cos":
        print("cal cos")
        ans=str(m.cos(m.radians(int(ex))))
    elif text=="tan":
        print("cal tan")
        ans=str(m.tan(m.radians(int(ex))))
    elif text=='sqrt':
        print("cal square root")
        ans=(m.sqrt(int(ex)))
    elif text=='^':
        print("cal power")
        base,pow=ex.split(',')
        print(base)
        print(pow)
        ans=m.pow(int(base),int(pow))

    textfield.delete(0,END)
    textfield.insert(0,ans)


normalcalc=True
def sc_click():
    global normalcalc
    if normalcalc:
        #sc..
        butttonFrame.pack_forget()
        sc_frame.pack(side=TOP,pady=20)
        butttonFrame.pack(side=TOP)
        window.geometry("500x700")
        print("show sc")
        normalcalc=False

    else:
        print("show normal calc")
        sc_frame.pack_forget()
        window.geometry("500x600")
        normalcalc=True


#binding sc buttons
sqrtbtn.bind("<Button-1>",cal_sc)
powbtn.bind("<Button-1>",cal_sc)
factbtn.bind("<Button-1>",cal_sc)
radbtn.bind("<Button-1>",cal_sc)
degbtn.bind("<Button-1>",cal_sc)
sinbtn.bind("<Button-1>",cal_sc)
cosbtn.bind("<Button-1>",cal_sc)
tanbtn.bind("<Button-1>",cal_sc)
#CREATING MENU
menubar=Menu(window)


mode=Menu(menubar,tearoff=0,font="15")
mode.add_checkbutton(label="Scientific Calculator",command=sc_click)
#mode.add_checkbutton(label="Ad",command=tick)

menubar.add_cascade(label="Mode",menu=mode)


window.config(menu=menubar)

window.mainloop()