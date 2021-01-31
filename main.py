import minizinc
import gridperso

# Create a MiniZinc model
model = minizinc.Model()
with open('puzzle_logic_2.mzn', 'r') as file:
    data = file.read()
model.add_string(data)

# Transform Model into a instance
gecode = minizinc.Solver.lookup("gecode")
inst = minizinc.Instance(gecode, model)

# Solve the instance
result = inst.solve()

arguments = {"name":["Jesssica","Laurie","Mark","Mary","Sally"],"film":["Minutes","Donnie","Scarecrow","Scarface","Recruit"],"day":["Monday","Tuesday","Wednesday","Thursday","Friday"],"time":["t735","t740","t820","t830","t845"]}

grid = gridperso.Gridperso(arguments,result)
grid.makeGrid()
