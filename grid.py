from tkinter import*

master = Tk()
master.geometry("500x500")

text1 = Label(master, text="Premier type",wraplength=1,background="black",foreground="white")
text1.grid(row=2, column=0, rowspan=3)

text1 = Label(master, text="truc")
text1.grid(row=2, column=1 )

text1 = Label(master, text="machin")
text1.grid(row=3, column=1 )

text1 = Label(master, text="bordel")
text1.grid(row=4, column=1 )

argsSize = 3
argsCount = 2

class SpecialButton(Button):
    def __init__(self, master=None, **kw):
        self.state = 0
        self.baseColor = kw.pop('notclickedbg','yellow')
        self.error = kw.pop('clickedonce','red')
        self.verified = kw.pop('clickedtwice','green')
        Button.__init__(self,master,**kw)
        self.bind('<Button-1>',self.clicked)

    def clicked(self,*args):
        if self.state == 0:
            self['bg'] = self.error
            self.state = 1
        elif self.state == 1:
            self['bg'] = self.verified
            self.state = 2
        elif self.state == 2:
            self['bg'] = self.baseColor
            self.state = 0

def somethingElse():
    print("Doing something else")

    
frameSpace = Frame(master, width=20, height=300, background="Black")
frameSpace.grid(row=0, column=2, rowspan=5)

for l in range(3,11,4):
    text2 = Label(master, text="Autre type",width=20, height=2,background="black",foreground="white")
    text2.grid(row=0, column=l, columnspan=3)

    text1 = Label(master, text="truc",wraplength=1)
    text1.grid(row=1, column=l )

    text1 = Label(master, text="machin",wraplength=1)
    text1.grid(row=1, column=l+1 )

    text1 = Label(master, text="bordel",wraplength=1)
    text1.grid(row=1, column=l+2 )

    for i in range(2, 5):
      for j in range(l, l+3):
            if (i % 2) == 0 and (j % 2) == 0:
                frame1 = SpecialButton(master, width=4, height=2, background="Yellow",command = somethingElse)
                frame1.grid(row=i, column=j)
            if (i % 2) == 0 and (j % 2) != 0:
                frame1 = SpecialButton(master, width=4, height=2, background="Yellow",command = somethingElse)
                frame1.grid(row=i, column=j)
            if (i % 2) != 0 and (j % 2) == 0:
                frame1 = SpecialButton(master, width=4, height=2, background="Yellow",command = somethingElse)
                frame1.grid(row=i, column=j)
            if (i % 2) != 0 and (j % 2) != 0:
               frame1 = SpecialButton(master, width=4, height=2, background="Yellow",command = somethingElse)
               frame1.grid(row=i, column=j)

    frameSpace = Frame(master, width=20, height=300, background="Black")
    frameSpace.grid(row=0, column=l+3, rowspan=5)


master.mainloop()
