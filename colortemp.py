
#!/brando/bin/env python3
import sys

print(sys.version)
from tkinter import *
from tkinter import messagebox
import tkinter
import subprocess as sub
root = tkinter.Tk()
root.geometry('300x300')


root.title("Brandon's Redshift UI")


selectedTemp = ""
def emptyTextFieldCallBack():
        messagebox.showinfo("Warning", "Missing a value between 5000 and 25000")

def changeScreenColorTemp():
        if entry.get() == "":
                messagebox.showinfo("Error", "Field cannot be empty")
        elif not entry.get().isdigit():
                messagebox.showinfo("Error", "Can only contain numerical values")
        elif int(entry.get()) > 20000 or int(entry.get()) < 1000:
                messagebox.showinfo("Error", "Can only contain values between 1000 and 20000.")
        else:
                selectedTemp = entry.get()
                #sub.call('redshift -O %s' % selectedTemp ,shell=True)
                safeScreenChange(selectedTemp)

def safeScreenChange(safeTemp):
	sub.call('redshift -O %s' % safeTemp ,shell=True)
	scale.pack()
	tmp = safeTemp
	scale.set(tmp)

scale = tkinter.Scale(orient='horizontal', from_=1000, to=20000, length=400, width=50, command=safeScreenChange)
	
close_button = tkinter.Button(root, text = "Quit", command=quit)

entry = tkinter.Entry(root)
entry.insert(0, '')
entry.config(width=25, justify=CENTER, bd=4)
entry.pack()

change_screen_button = tkinter.Button(root, text = "Change Screen Temp", command=changeScreenColorTemp)
change_screen_button.pack()
change_screen_button.config(height = 3, width = 25)

"""
min_button  = tkinter.Button(root, text="1000(minimum)", command= lambda: safeScreenChange(1000))
min_button.pack()
min_button.config(height=2, width=10)
"""


scale.pack()
scale.set(5000)

close_button.pack()
close_button.config(height=4, width=10)

root.mainloop()

