from tkinter import *
from tkinter import messagebox as tsmg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile(event=None):
    global file
    root.title("Untitiled-Notepad")
    file=None
    textarea.delete(1.0,END)
def openfile(event=None):
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
def savefile(event=None):
    global file
    if file==None:
        file=asksaveasfilename(defaultextension=".txt",
                         filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"-Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def copyfile(event=None):
    textarea.event_generate(("<<Copy>>"))
def cutfile(event=None):
    textarea.event_generate(("<<Cut>>"))
def pastefile(event=None):
    textarea.event_generate(("<<Paste>>"))
def helps():
    tsmg.showinfo("help","this notepad is created by avi and can be used to edit files")
if __name__ == '__main__':
    root=Tk()
    root.title("Untitled-Notepad")
    root.geometry("500x500")
    root.wm_iconbitmap("icon.ico")

    textarea=Text(root,font="Alias 13")
    file = None
    textarea.pack(fill=BOTH,expand=True)


    mainmenu=Menu(root)
    m1=Menu(mainmenu,tearoff=0)

    m1.add_command(label="New (Ctrl+N)",command=newfile)
    m1.add_command(label="Open (Ctrl+O)",command=openfile)
    m1.add_command(label="Save (Ctrl+S)",command=savefile)
    mainmenu.add_cascade(label="File",menu=m1)

    m2=Menu(mainmenu,tearoff=0)
    m2.add_command(label="Copy (Ctrl+C)",command=copyfile)
    m2.add_command(label="Cut (Ctrl+X)",command=cutfile)
    m2.add_command(label="Paste (Ctrl+V)",command=pastefile)
    mainmenu.add_cascade(label="Edit",menu=m2)

    m3 = Menu(mainmenu, tearoff=0)
    m3.add_command(label="Help", command=helps)
    mainmenu.add_cascade(label="About",menu=m3)
    root.config(menu=mainmenu)

    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

    root.bind("<Control-c>",copyfile)
    root.bind("<Control-x>",cutfile)
    root.bind("<Control-v>",pastefile)
    root.bind("<Control-n>",newfile)
    root.bind("<Control-s>",savefile)
    root.bind("<Control-o>",openfile)

    root.mainloop()