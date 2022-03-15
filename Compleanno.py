from tkinter import *
from tkinter import messagebox
import json
import re
import os
filePath=os.path.abspath(os.path.dirname(__file__)) + "\\"
fileName="birthday.txt"
newWin=False;
def findBirthday():
    global newWin
    global cont
    global ID
    name=e_root1.get().upper();
    surname=e_root2.get().upper();
    ID=name + "." + surname;
    try:
        if os.stat(filePath + fileName).st_size == 0:
            file = open(filePath + fileName,"w");
            file.write("{}")
            file.close()
    except FileNotFoundError:
        file =open(filePath + fileName,"x");
        file.close()
        if os.stat(filePath + fileName).st_size == 0:
            file = open(filePath + fileName,"w");
            file.write("{}")
            file.close()
    file = open(filePath + fileName);
    cont = file.read();
    file.close();
    cont = json.loads(cont);
    if ID in cont.keys():
        messagebox.showinfo(title="Found!", message= name.upper() + " " + surname.upper() + "'s birthday is on: " + str(cont.get(ID,0)))
    else:
        msgBox=messagebox.askquestion(title="NOT Found!", message= name.upper() + " " + surname.upper() + "'s birthday is not stored. Would you like to save it?", icon="warning")
        if msgBox == "yes":
            newWin=True;
            root.destroy()
        else:
            return None
    print(cont)
#called from save button in second window
def saveBirthday():
    dateReg=re.compile(r'^\d{4}$')
    year=e1_win2.get()
    if dateReg.search(year) == None:
        messagebox.showerror(title="Error!", message="date not valid")
    else:
        day=clicked1.get()
        month=clicked2.get()
        date=str(day) + "/" + str(month) + "/" + str(year);
        cont[ID]=date;
        file=open(filePath + fileName, "w");
        file.write(str(cont).replace("'",'"'));
        file.close();
        messagebox.showinfo(title="Saved!", message=ID.split(".")[0] + " " + ID.split(".")[1] + "'s birthday '" + str(date) +"' was saved!" )
        win2.destroy()

#main window:
root = Tk()
root.title("Compleanno.exe")
lbl_root0=Label(root, text="Welcome to compleanno!").grid(row=0, column=0)
lbl_root1=Label(root, text="Name:").grid(row=1, column=0)
lbl_root2=Label(root, text="Surname:").grid(row=2, column=0)
e_root1=Entry(root, width=20)
e_root2=Entry(root, width=20)
e_root1.grid(row=1, column=1)
e_root2.grid(row=2, column=1)
btn_root0=Button(root, text="Search",  command=lambda:findBirthday(), width=20)
btn_root0.grid(row=3, column=1)
root.mainloop()
#second window to save new birthday:
if newWin==True:
    win2 = Tk();
    win2.title("Save new birthday!");
    lbl1_win2=Label(win2, text="Insert date:");
    lbl1_win2.grid(row=0, column=0);
    e1_win2=Entry(win2, width=10);
    clicked1 = IntVar()
    clicked1.set(1)
    drop1 = OptionMenu(win2, clicked1, 1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31);
    drop1.grid(row=0,column=1);
    clicked2 = IntVar()
    clicked2.set(1)
    drop2 = OptionMenu(win2, clicked2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12);
    drop2.grid(row=0, column=2);
    e1_win2.insert(END, "yyyy");
    e1_win2.grid(row=0, column=3);
    bt1_win2=Button(win2, text="Save", command=lambda:saveBirthday(),width=10)
    bt1_win2.grid(row=0, column=4)
    win2.mainloop()