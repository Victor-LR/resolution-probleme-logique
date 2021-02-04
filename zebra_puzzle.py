import minizinc
import zebra_gui as zgui

# Create a MiniZinc model
model = minizinc.Model()
with open('problem_zebre.mzn', 'r') as file:
    data = file.read()
model.add_string(data)

# Transform Model into an instance
gecode = minizinc.Solver.lookup("gecode")
instance = minizinc.Instance(gecode, model)

# Solve the instance
result = instance.solve(all_solutions=True)
print(result)

zebre = zgui.Zebra_GUI(result[0])
zebre.create_gui()
