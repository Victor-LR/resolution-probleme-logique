from tkinter import*
import tkinter.messagebox

class Gridperso:

    # bouton custom
    class SpecialButton(Button):

        def __init__(self, gridRow, gridCol, outer, currentVar, currentVarIndex, gridSize, master=None, **kwargs):
             Button.__init__(self, master, **kwargs)
             self.outer = outer
             self.etat = 0
             self.gridRow = gridRow
             self.gridCol = gridCol
             self.gridSize = gridSize
             self.currentVar = currentVar
             self.currentVarIndex = currentVarIndex
             self.bind('<Button-1>', self.clicked)
    
        # gestion du click
        def clicked(self, *args):
            #debug print("x =" + str(self.outer.arguments["name"][self.gridRow]))
            # print("y =" + str(self.outer.arguments[self.currentVar][self.gridCol]))

            # on marque une case en rouge
            if self.etat == 0:
                self.outer.current[self.currentVar][self.gridRow] = 0
                self.outer.currentVert[self.currentVar][self.gridCol] = 0
                self.setRed()
            # on marque une case en vert si elle n'est pas sur une ligne ou une vert ou il y a deja une case verte
            elif self.etat == 1 and self.outer.current[self.currentVar][self.gridRow] == 0 and self.outer.currentVert[self.currentVar][self.gridCol] == 0:
                self['bg'] = 'green'
                self.etat = 2
                self.outer.current[self.currentVar][self.gridRow] = self.gridCol+1
                self.outer.currentVert[self.currentVar][self.gridCol] = self.gridCol+1

                # on marque les cases sur la même ligne et la même verticale en rouge
                for i in range(self.gridSize):
                    if i != self.gridRow:
                        self.outer.grid[self.currentVarIndex][i][self.gridCol].setRed()
                    if i != self.gridCol:
                        self.outer.grid[self.currentVarIndex][self.gridRow][i].setRed()
             #  on remet la case à l'état de base
            elif self.etat == 2:
                self.setDefaut()
                self.outer.current[self.currentVar][self.gridRow] = 0
                self.outer.currentVert[self.currentVar][self.gridCol] = 0
                # on retire les cases marquées
                for i in range(self.gridSize):
                    if i != self.gridRow:
                        self.outer.grid[self.currentVarIndex][i][self.gridCol].setDefaut()
                    if i != self.gridCol:
                        self.outer.grid[self.currentVarIndex][self.gridRow][i].setDefaut()

        def setRed(self):
            self['bg'] = 'red'
            self.etat = 1

        def setDefaut(self):
            self['bg'] = 'white'
            self.etat = 0
        

            
    def __init__(self, arguments,solution,current,currentVert,text):
        self.arguments = arguments
        self.keys = list(arguments.keys())
        self.solution = solution
        self.current = current
        self.currentVert = currentVert
        self.text = text

    def checkSolution(self):
        valide = True
        for k in range(1,len(self.keys)):
            for idx, item in enumerate(self.solution[self.keys[k]]):
                if item != self.current[self.keys[k]][idx]:
                    valide=False
                print(str(idx) + " " + str(item) + "   " + str(self.current[self.keys[k]][idx]))
        if valide :
            tkinter.messagebox.showinfo(title="résultat", message="gagner")
        else :
            tkinter.messagebox.showinfo(title="résultat", message="perdu")

    def makeGrid(self):  
        arguments = len(next(iter(self.arguments.values())))
        variables = len(self.arguments.keys())-1
        
        # grid
        master = Tk()
        
        size = arguments * variables * 80
        master.geometry(str(size) + "x" + str(size))
        
        # ---------- NIVEAU 1 ---------
        # barre verticale gauche
        labelHorizontalGauche = Label(master, text=self.keys[0],height=arguments * 3 ,width=5, background="black", foreground="white")
        labelHorizontalGauche.grid(row=2, column=0, rowspan=arguments)
        
        # arguments de gauche
        for k in range(2, 2+arguments):
            labelGauche = Label(master, text=self.arguments[self.keys[0]][k-2])
            labelGauche.grid(row=k, column=1)
        
        # barre de séparation verticale de gauche
        frameSpace = Frame(master, width=15, height=arguments * 70, background="Black")
        frameSpace.grid(row=0, column=2, rowspan=2+arguments)
        
        start = 3
        step = arguments+1
        
        # on initialize la grid de boutons
        self.grid = [[[0 for f in range(arguments)] for h in range(arguments) ] for g in range(variables+4)]
        
        # parcours des différents grid
        for l in range(start, start+step*variables, step):
            # premiere barre horizontale en haut
            varIndex = int(l/step) +1
            labelHorizontal = Label(master, text=self.keys[varIndex], width=arguments*7,
                          height=2, background="black", foreground="white")
            labelHorizontal.grid(row=0, column=l, columnspan=arguments)
        
            # arguments du haut
            for p in range(l, l+arguments):
                labelHaut = Label(master, text=self.arguments[self.keys[varIndex]][p-l])
                labelHaut.grid(row=1, column=p)
        
            # grid des boutons
            for i in range(2, 2+arguments):
                for j in range(l, l+arguments):
                    gridRow = i-2
                    gridCol = j-l
                    button = self.SpecialButton(master=master,gridRow=gridRow,gridCol=gridCol,outer=self,currentVar=self.keys[varIndex],currentVarIndex = varIndex,gridSize=arguments, width=4, height=2, background="White")
                    button.grid(row=i, column=j)
                    # on rempli la grid de boutons pour la gestion des lignes/verticales 
                    self.grid[varIndex][gridRow][gridCol] = button
        
            # séparation entre les grids
            frameSpace = Frame(master, width=15, height=arguments *
                               70, background="Black")
            frameSpace.grid(row=0, column=l+arguments, rowspan=2+arguments)

        # ---------- NIVEAU 2 ---------
        # barre horizontale gauche
        labelHorizontalGauche = Label(master, text=self.keys[3],height=arguments * 3 ,width=5, background="black", foreground="white")
        labelHorizontalGauche.grid(row=2+arguments, column=0, rowspan=arguments)
        
        # arguments de gauche
        for k in range(2+arguments, 2+arguments*2):
            labelGauche = Label(master, text=self.arguments[self.keys[3]][k-2-arguments])
            labelGauche.grid(row=k, column=1)     

        # barre de séparation verticale de gauche
        frameSpace = Frame(master, width=15, height=arguments * 60, background="Black")
        frameSpace.grid(row=2+arguments, column=2, rowspan=arguments)
        
        variables2 = variables-1
        # parcours des différents grid du milieu
        for l in range(start, start+step*variables2, step):
        
            # grid des boutons
            for i in range(2+arguments, 2+arguments*2):
                for j in range(l, l+arguments):
                    gridRow = i-(2+arguments)
                    gridCol = j-l
                    button = self.SpecialButton(master=master,gridRow=gridRow,gridCol=gridCol,outer=self,currentVar=self.keys[1],currentVarIndex = 4,gridSize=arguments, width=4, height=2, background="White")
                    button.grid(row=i, column=j)
                    # on rempli la grid de boutons pour la gestion des lignes/verticales 
                    self.grid[4][gridRow][gridCol] = button

            # séparation entre les grids
            frameSpace = Frame(master, width=15, height=arguments *
                               60, background="Black")
            frameSpace.grid(row=2+arguments, column=l+arguments, rowspan=arguments)
        
            
        # ---------- NIVEAU 3 ---------

        # barre horizontale gauche
        labelHorizontalGauche = Label(master, text=self.keys[2],height=arguments * 3 ,width=5, background="black", foreground="white")
        labelHorizontalGauche.grid(row=2+arguments*2, column=0, rowspan=arguments)
        
        # arguments de gauche
        for k in range(2+arguments*2, 2+arguments*3):
            labelGauche = Label(master, text=self.arguments[self.keys[2]][k-2-arguments*2])
            labelGauche.grid(row=k, column=1)     

        # barre de séparation verticale de gauche
        frameSpace = Frame(master, width=15, height=arguments * 60, background="Black")
        frameSpace.grid(row=2+arguments*2, column=2, rowspan=arguments)

        # grid des boutons
        for i in range(2+arguments*2, 2+arguments*3):
            for j in range(3,3+arguments):
                gridRow = i-2-arguments*2
                gridCol = j-3
                button = self.SpecialButton(master=master,gridRow=gridRow,gridCol=gridCol,outer=self,currentVar=self.keys[1],currentVarIndex = 5,gridSize=arguments, width=4, height=2, background="White")
                button.grid(row=i, column=j)
                # on rempli la grid de boutons pour la gestion des lignes/verticales 
                self.grid[5][gridRow][gridCol] = button
    
        description = Label(master,text = self.text)
        description.grid(row = 3+arguments*2, column= arguments*2 ,columnspan = 5+arguments *2,rowspan = arguments *2)
        
        buttonCheck = Button(master,text="Check",command=self.checkSolution)
        buttonCheck.grid(row=arguments*3+4, column=2, rowspan=2+arguments)
        master.mainloop()

