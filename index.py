from tkinter import *


#==================================MAIN FRAME=====================================
root = Tk()
root.title("Read Text File In Python")
width=450
height=350
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2) - (width/2)
y=(screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#=================================VARIABLES=======================================
FILE = StringVar()

#=================================METHODS=========================================
def Read_File():
    if FILE.get() == "":
        lbl_status.config(fg="Orange", text="Please enter something")
        for widget in BottomPane.winfo_children():
            widget.destroy()
    else:
        for widget in BottomPane.winfo_children():
            widget.destroy()
        file = open(FILE.get() + ".txt", "r")
        chars = [line.rstrip('\n') for line in file]
        for i in range(len(chars)):
            exec ('Label%d=Label(BottomPane,text="%s")\nLabel%d.pack(anchor=W)' % (i, chars[i], i))
        file.close()

#=================================FRAMES==========================================
Top = Frame(root, relief=SOLID, bd=1)
Top.pack(fill=X)
Mid = Frame(root)
Mid.pack(pady=20)
Left = Frame(Mid)
Left.pack(side=LEFT)
Right = Frame(Mid)
Right.pack(side=RIGHT)
BelowMid = Frame(root)
BelowMid.pack()
Bottom = Frame(root)
Bottom.pack()
BottomPane = Frame(root)
BottomPane.pack()
#=================================LABEL WIDGETS===================================
lbl_title = Label(Top, text="Read File Text", font=('Courier new', 16))
lbl_title.pack()
lbl_txt = Label(Left, text="Enter a text file", font=('Courier new', 15))
lbl_txt.pack()
lbl_txt2 = Label(Bottom, text="Result", font=('Courier new', 15))
lbl_txt2.pack()
lbl_status = Label(Bottom,font=('Courier new', 12))
lbl_status.pack()


#=================================ENTRY WIDGETS===================================
txt_file = Entry(Right, font=('Courier new', 15),fg='blue', textvariable=FILE)
txt_file.pack()

#=================================BUTTON WIDGETS==================================
btn_check = Button(BelowMid, text="Read File",bg='green', command=Read_File)
btn_check.pack(pady=10)


#=================================INITIALIZATION==================================
if __name__ == '__main__':
    root.mainloop()