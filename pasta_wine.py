import minizinc

# Create a MiniZinc model
model = minizinc.Model()
print(model)
model.add_string("""
include "globals.mzn"
set of int: SHIRT = 1..5;
set of int: NAME = 1..5;
set of int: SURNAME = 1..5;
set of int: PASTA = 1..5;
set of int: WINE = 1..5;
set of int: AGE = 1..5;

int: blue = 1;
int: green = 2;
int: red = 3;
int: white = 4;
int: yellow = 5;
array [SHIRT] of string: nomSh = ["blue", "green", "red", "white", "yellow"];

int: Andrea = 1;
int: Holly = 2;
int: Julie = 3;
int: Leslie = 4;
int: Victoria = 5;
array [NAME] of string: nomN = ["Andrea", "Holly", "Julie", "Leslie", "Victoria"];

int: Brown = 1;
int: Davis = 2;
int: Lopes = 3;
int: Miller = 4;
int: Wilson = 5;
array [SURNAME] of string: nomSu = ["Brown", "Davis", "Lopes", "Miller", "Wilson"];

int: farfalle = 1;
int: lasagne = 2;
int: penne = 3;
int: spaghetti = 4;
int: ravioli = 5;
array [PASTA] of string: nomP = ["farfalle", "lasagne", "penne", "spaghetti", "ravioli"];

int: Australian = 1;
int: Argentine = 2;
int: Chilean = 3;
int: French = 4;
int: Italian = 5;
array [WINE] of string: nomW = ["Australian", "Argentine", "Chilean", "French", "Italian"];

int: year30 = 1;
int: year35 = 2;
int: year40 = 3;
int: year45 = 4;
int: year50 = 5;
array [AGE] of string: nomA = ["year30", "year35", "year40", "year45", "year50"];

array[NAME] of var SHIRT: shirt;
array[NAME] of var SURNAME: surname;
array[NAME] of var PASTA: pasta;
array[NAME] of var WINE: wine;
array[NAME] of var AGE: age;

constraint
all_different(shirt)
    /\ all_different(surname)
    /\ alldifferent(pasta)
    /\ alldifferent(wine)
    /\ alldifferent(age)
    %Contrainte
    /\
""")