import minizinc


# Create a MiniZinc model
model = minizinc.Model()
print(model)
model.add_string("""
include "globals.mzn";

var 1..9:S;
var 0..9:E;
var 0..9:N;
var 0..9:D;
var 1..9:M;
var 0..9:O;
var 0..9:R;
var 0..9:Y;

constraint 1000*S + 100*E + 10*N + D + 1000*M + 100*O + 10*R + E = 10000*M + 1000*O + 100*N + 10*E + Y;
constraint alldifferent([S,E,N,D,M,O,R,Y]);

%

solve satisfy;


""")

# Transform Model into a instance
gecode = minizinc.Solver.lookup("gecode")
inst = minizinc.Instance(gecode, model)
# inst["a"] = 1
# inst["b"] = 4
# inst["c"] = 0

# Solve the instance
result = inst.solve(all_solutions=True)
print(result) 

# for i in range(len(result)):
#     print("x = {}".format(result[i, "x"]))