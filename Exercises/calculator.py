from tkinter import*
root=Tk()
root.geometry("600x700")
root.title("Calculator By Manish singh")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,ipady=10,padx=10)

f1= Frame(root)
root.mainloop()