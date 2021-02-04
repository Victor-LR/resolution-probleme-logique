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

print(result)

if "puzzle_logic_3.mzn" in filename:
    arguments = {"monitor":["13'", "15'", "15'6", "21'5", "27'"],"cpu":["2.0MHz", "2.3MHz", "2.5MHz", "2.7MHz", "3.1MHz"],"hdd":["250Gb", "320Gb", "500Gb", "750Gb", "1024Gb"],"price":["699$", "999$", "1149$", "1349$", "1649$"]}
    current = {"cpu":[0,0,0,0,0],"hdd":[0,0,0,0,0],"price":[0,0,0,0,0]}
    currentVert = {"cpu":[0,0,0,0,0],"hdd":[0,0,0,0,0],"price":[0,0,0,0,0]}
    result = { "cpu":[2, 1, 4, 3, 5], "hdd":[1, 2, 5, 3, 4], "price":[1, 2, 3, 4, 5]}
else:
    arguments = {"name":["Jessica","Laurie","Mark","Mary","Sally"],"film":["Minutes","Donnie","Scarecrow","Scarface","Recruit"],"day":["Monday","Tuesday","Wednesday","Thursday","Friday"],"time":["t735","t740","t820","t830","t845"]}
    current = {"film":[0,0,0,0,0],"day":[0,0,0,0,0],"time":[0,0,0,0,0]}
    currentVert = {"film":[0,0,0,0,0],"day":[0,0,0,0,0],"time":[0,0,0,0,0]}

print(result)

grid = gridperso.Gridperso(arguments,result,current,currentVert)

grid.makeGrid()

