from tkinter import*

# button custom
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

# size venant de minizinc apres
arguments = 5
variables = 4

# grid
master = Tk()

length = arguments * variables * 60
height = arguments * 100
master.geometry(str(length) + "x" + str(height))



# barre horizontale gauche
text1 = Label(master, text="Premier type",wraplength=1,height = arguments * 4,background="black",foreground="white")
text1.grid(row=2, column=0, rowspan=arguments)

# arguments de gauche
for k in range(2,2+arguments):
    text1 = Label(master, text="machin")
    text1.grid(row=k, column=1 )

# barre de séparation verticale de gauche
frameSpace = Frame(master, width=20, height=arguments * 80, background="Black")
frameSpace.grid(row=0, column=2, rowspan=2+arguments)

start = 3
step = arguments+1



# parcours des différents grid
for l in range(start,start+step*variables,step):
    # premiere barre horizontale en haut
    text2 = Label(master, text="Autre type",width=arguments*7, height=2,background="black",foreground="white")
    text2.grid(row=0, column=l, columnspan=arguments)

    # arguments du haut
    for p in range(l,l+arguments):
        text1 = Label(master, text="truc",wraplength=1)
        text1.grid(row=1, column=p )

    # grid des boutons
    for i in range(2, 2+arguments):
      for j in range(l, l+arguments):
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

    # séparation entre les grids
    frameSpace = Frame(master, width=20, height=arguments * 80, background="Black")
    frameSpace.grid(row=0, column=l+arguments, rowspan=2+arguments)


master.mainloop()
