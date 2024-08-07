
from tkinter import *
import base64
r = Tk()
r.geometry('500x300')
r.resizable(1200,900)
r.title("Message Encode and Decode")


Label(r, text ='ENCODE DECODE', font = 'Helvetica 20 bold').pack()  
Label(r, text ='GROUP 10 ', font = 'Helvetica 15 bold').pack(side =BOTTOM)



store = StringVar()
p_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,msg):
    enc=[]
    for i in range(len(msg)):
        key1 = key[i % len(key)]
        enc.append(chr((ord(msg[i]) + ord(key1)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key,msg):
    dec=[]
    msg = base64.urlsafe_b64decode(msg).decode()
    for i in range(len(msg)):
        key1 = key[i % len(key)]
        dec.append(chr((256 + ord(msg[i])- ord(key1)) % 256))
        
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(p_key.get(), store.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(p_key.get(), store.get()))
    else:
        Result.set('Invalid Mode')
        
def Exit():
    r.destroy()

def Reset():
    store.set("")
    p_key.set("")
    mode.set("")
    Result.set("")


#Message
Label(r, font= 'Helvetica 12 italic', text='MESSAGE').place(x= 60,y=60)
Entry(r, font = 'Helvetica 10', textvariable = store, bg = '#c5c5ff').place(x=290, y = 60)

#key
Label(r, font = 'Helvetica 12 italic', text ='KEY').place(x=60, y = 90)
Entry(r, font = 'Helvetica 10', textvariable = p_key , bg ='#c5c5ff').place(x=290, y = 90)


#mode
Label(r, font = 'Helvetica 12 italic underline', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(r, font = 'Helvetica 10', textvariable = mode , bg= '#c5c5ff').place(x=290, y = 120)



#result
Entry(r, font = 'Helvetica 10 italic', textvariable = Result, bg ='#c5c5ff').place(x=290, y = 150)

#result button
Button(r, font = 'Helvetica 10 italic', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)


#reset button
Button(r, font = 'Helvetica 10 italic' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=180, y = 220)

#exit button
Button(r, font = 'Helvetica 10 italic',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=260, y = 220)
r.mainloop()
