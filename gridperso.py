from tkinter import*
import tkinter.messagebox

class Gridperso:

    # bouton custom
    class SpecialButton(Button):

        def __init__(self, gridRow, gridCol, outer, currentVar , master=None, **kwargs):
             Button.__init__(self, master, **kwargs)
             self.outer = outer
             self.state = 0
             self.gridRow = gridRow
             self.gridCol = gridCol
             self.currentVar = currentVar
             self.bind('<Button-1>', self.clicked)
    
        def clicked(self, *args):
            argu = self.outer.arguments
            print(argu[self.outer.keys[0]][self.gridRow])
            print(argu[self.currentVar][self.gridCol])
            print(self.gridCol)
            if self.state == 0:
                self['bg'] = 'red'
                self.state = 1
                self.outer.current[self.currentVar][self.gridRow] = 0
            elif self.state == 1:
                self['bg'] = 'green'
                self.state = 2
                self.outer.current[self.currentVar][self.gridRow] = self.gridCol+2
            elif self.state == 2:
                self['bg'] = 'white'
                self.state = 0
                self.outer.current[self.currentVar][self.gridRow] = 0

            
    def __init__(self, arguments,solution):
        self.arguments = arguments
        self.keys = list(arguments.keys())
        self.solution = solution
        self.current = {"film":[0,0,0,0,0],"day":[0,0,0,0,0],"time":[0,0,0,0,0]}

    def checkSolution(self):
        valide = True
        for k in range(1,len(self.keys)):
            for idx, item in enumerate(self.solution[self.keys[k]]):
                if item != self.current[self.keys[k]][idx]:
                    valide=False
                # print(str(idx) + " " + str(item) + "   " + str(self.current[self.keys[k]][idx]))
        if valide :
            tkinter.messagebox.showinfo(title="résultat", message="gagner")
        else :
            tkinter.messagebox.showinfo(title="résultat", message="perdu")

    def makeGrid(self):
        arguments = len(next(iter(self.arguments.values())))
        variables = len(self.arguments.keys())-1
        
        # grid
        master = Tk()
        
        length = arguments * variables * 60
        height = arguments * 120
        master.geometry(str(length) + "x" + str(height))
        
        
        # barre horizontale gauche
        labelHorizontalGauche = Label(master, text=self.keys[0], wraplength=1,height=arguments * 4, background="black", foreground="white")
        labelHorizontalGauche.grid(row=2, column=0, rowspan=arguments)
        
        # arguments de gauche
        for k in range(2, 2+arguments):
            labelGauche = Label(master, text=self.arguments[self.keys[0]][k-2])
            labelGauche.grid(row=k, column=1)
        
        # barre de séparation verticale de gauche
        frameSpace = Frame(master, width=20, height=arguments * 90, background="Black")
        frameSpace.grid(row=0, column=2, rowspan=2+arguments)
        
        start = 3
        step = arguments+1
        
        
        # parcours des différents grid
        for l in range(start, start+step*variables, step):
            # premiere barre horizontale en haut
            varIndex = int(l/step) +1
            labelHorizontal = Label(master, text=self.keys[varIndex], width=arguments*7,
                          height=2, background="black", foreground="white")
            labelHorizontal.grid(row=0, column=l, columnspan=arguments)
        
            # arguments du haut
            for p in range(l, l+arguments):
                labelHaut = Label(master, text=self.arguments[self.keys[varIndex]][p-l-1], wraplength=1)
                labelHaut.grid(row=1, column=p)
        
            # grid des boutons
            for i in range(2, 2+arguments):
                for j in range(l, l+arguments):
                    button = self.SpecialButton(gridRow=i-2,gridCol=j-l-1,outer=self,currentVar=self.keys[varIndex], width=4, height=2, background="White")
                    button.grid(row=i, column=j)

        
            # séparation entre les grids
            frameSpace = Frame(master, width=20, height=arguments *
                               90, background="Black")
            frameSpace.grid(row=0, column=l+arguments, rowspan=2+arguments)


        buttonCheck = Button(master,text="Check",command=self.checkSolution)
        buttonCheck.grid(row=arguments+4, column=2, rowspan=2+arguments)
        master.mainloop()

