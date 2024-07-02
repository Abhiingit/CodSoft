# to do list application
import tkinter
from tkinter import *


root=Tk()
root.title("To Do List App")
name_var=StringVar()
root.geometry("400x650")
root.resizable(False,False)
task_list=[]

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("taskfile.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task) 


def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))  
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            taskfile.write(task+"\n")
        listbox.delete(ANCHOR)        


def openTaskFile():
    try:
       global task_list
       with open("tasklist.txt","r") as taskfile:
           tasks =taskfile.readlines()
       for task in tasks:
           if task !='\n':
               task_list.append(task)
               listbox.insert(END,task)
    except:
        file=open('task_list','w')
        file.close()        

#icon
input_frame = Frame(root, width=300, height=40, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
input_frame.pack(side=TOP)
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)
task=StringVar()
task_entry=Entry(frame,width=18,font='arial 20',bd=0)
task_entry.place(x=150,y=7)
task_entry.focus()
button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="black",fg="white",bd=0,command=addTask)
button.place(x=300,y=0)

#delete
button=Button(frame,text="DELETE",font="arial 20 bold",width=7,bg="black",fg="white",bd=0,command=deleteTask)
button.place(x=10,y=-5)

#listbox

frame1=Frame(root,bd=3,width=700,height=280,bg="dark blue")
frame1.pack(pady=(220,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="black",fg="white",cursor="hand2")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

root.mainloop()