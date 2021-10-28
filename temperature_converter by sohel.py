
from tkinter import *

window= Tk()
window.title('Temperature Converter created by sohel')
window.minsize(width=600, height=400)

window.config()

label=Label(window,text="convert to fahrenheit",bg="red",fg="white")
label.grid(row=2,column=0)
label.config()

input=Entry()
input.grid(row=2,column=2)

ans=Label(text=' ',font=('Courrier',10,'bold'))
ans.grid(row=3,column=2)

def convert():
    temp = float(input.get())
    temp_F= temp*9/5+32
    ans['text']='Temperature in Fahrenheit is: '+str(temp_F)


button=Button(window,text='Covert',bg="green", command=convert,font=("Arial",15,"bold"))
button.grid(row=2,column=3)

window.mainloop()