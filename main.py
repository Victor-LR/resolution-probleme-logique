import minizinc
import gridperso
import tkinter.filedialog 
import os

# choisir le bon fichier
cwd = os.getcwd()
filename = tkinter.filedialog.askopenfilename(initialdir=cwd, filetypes=(('Minizinc code files','*.mzn'),))

# Create a MiniZinc model
model = minizinc.Model()

print(filename)
with open(filename, 'r') as file:
    data = file.read()
model.add_string(data)

# Transform Model into a instance
gecode = minizinc.Solver.lookup("gecode")
inst = minizinc.Instance(gecode, model)

# Solve the instance
result = inst.solve()

if "puzzle_logic_2.mzn" in filename:
    arguments = {"Taille":["13'", "15'", "15'6", "21'5", "27'"],"Processeur":["2.0MHz", "2.3MHz", "2.5MHz", "2.7MHz", "3.1MHz"],"Disque":["250Gb", "320Gb", "500Gb", "750Gb", "1024Gb"],"Prix":["699$", "999$", "1149$", "1349$", "1649$"]}
    current = {"Processeur":[0,0,0,0,0],"Disque":[0,0,0,0,0],"Prix":[0,0,0,0,0]}
else:
    arguments = {"name":["Jesssica","Laurie","Mark","Mary","Sally"],"film":["Minutes","Donnie","Scarecrow","Scarface","Recruit"],"day":["Monday","Tuesday","Wednesday","Thursday","Friday"],"time":["t735","t740","t820","t830","t845"]}
    current = {"film":[0,0,0,0,0],"day":[0,0,0,0,0],"time":[0,0,0,0,0]}


grid = gridperso.Gridperso(arguments,result,current)

grid.makeGrid()

