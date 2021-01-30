include "globals.mzn";
set of int: PLACEMENT = 1..5;
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

array[PLACEMENT] of var SHIRT: shirt;
array[PLACEMENT] of var SURNAME: surname;
array[PLACEMENT] of var PASTA: pasta;
array[PLACEMENT] of var WINE: wine;
array[PLACEMENT] of var AGE: age;
array[PLACEMENT] of var NAME: name;


constraint
all_different(shirt)
    /\ all_different(surname)
    /\ all_different(pasta)
    /\ all_different(wine)
    /\ all_different(age)
    /\ all_different(name)
    
    % The woman wearing the White shirt is next to the woman who likes Lombardian wines
    /\ exists(a,b in PLACEMENT) ((shirt[a] == white) /\ (wine[b] == Italian) /\ abs(a-b)==1) 
    
    % Ms Miller is somewhere between Ms Davis and Ms Brown, in that order
    /\ exists(a,b,c in PLACEMENT) ( (surname[a] == Miller) /\ (surname[b] == Davis) /\ (surname[c] == Brown) /\ (a > b) /\ ( a < c))
    
    % The youngest woman is at the third position
    /\ age[3] == year30
    
    % The 45 years old woman is somewhere to the right of the woman wearing the Red shirt.
    /\ exists(a,b in PLACEMENT) ((age[a] == year45) /\ (shirt[b] == red) /\ (a > b))
    
    % The woman who likes Chilean wines also likes Farfalle
    /\ exists(a in PLACEMENT) (wine[a] == Chilean /\ pasta[a] == farfalle)
    
    % At the first position is the woman that likes Argentine wines.
    /\ wine[1] == Argentine
    
    % Andrea is exactly to the right of the 35 years old woman.
    /\ exists(a,b in PLACEMENT) ( name[a] == Andrea /\ age[b] == year35  /\ a == b+1)
    
    % The woman wearing the Blue shirt is somewhere between Ms Davis and Holly, in that order
    /\ exists(a,b,c in PLACEMENT) ( (shirt[a] == blue) /\ (surname[b] == Davis) /\ (name[c] == Holly) /\ (a > b) /\ ( a < c))
    
    % Victoria is next to Leslie
    /\ exists(a,b in PLACEMENT) (name[a] == Victoria /\ name[b] == Leslie /\ abs(a-b)==1)
    
    % The woman wearing the Red shirt is somewhere to the left of the woman who likes Australian wines.
    /\ exists(a,b in PLACEMENT) ((shirt[a] == red) /\ (wine[b] == Australian) /\ a < b)
    
    % Ms Wilson is next to the 30 years old woman
    /\ exists(a,b in PLACEMENT) (surname[a] == Wilson /\ age[b] == year30 /\ abs(a-b)==1)
    
    % Leslie is exactly to the left of the 30 years old woman
    /\ exists(a,b in PLACEMENT) (name[a] == Leslie /\ age[b] == year30 /\ a == b-1)
    
    % Holly is somewhere to the right of the woman wearing the Red shirt
    /\ exists(a,b in PLACEMENT) (name[a] == Holly /\ shirt[b] == red /\ a > b)
    
    % Ms Brown is exactly to the left of Julie
    /\ exists(a,b in PLACEMENT) (surname[a] == Brown /\ name[b] == Julie /\ a == b-1)
    
    % The youngest woman likes Penne
    /\ exists(a in PLACEMENT) (age[a] == year30 /\ pasta[a]==penne)
    
    % Ms Wilson is wearing the White shirt
    /\ exists(a in PLACEMENT) (surname[a] == Wilson /\ shirt[a]==white)
    
    % The woman who likes Lasagne is somewhere between the woman who likes Italian wines and the woman who likes Spaghetti, in that order
    /\ exists(a,b,c in PLACEMENT) ( (pasta[a] == lasagne) /\ (wine[b] == Italian) /\ (pasta[c] == spaghetti) /\ (a > b) /\ ( a < c))
    
    % At the second position is the woman wearing the Blue shirt.
    /\ shirt[2] == blue
    
    % The 40 years old woman likes Lasagne
    /\ exists(a in PLACEMENT) (age[a] == year40 /\ pasta[a]==lasagne)
    
    % Ms Lopes is at the fifth position
    /\ surname[5] == Lopes
    
    % The woman that likes Australian wines is somewhere between Victoria and the woman who likes wines from Bordeaux, in that order
    /\ exists(a,b,c in PLACEMENT) ( (wine[a] == Australian) /\ (name[b] == Victoria) /\ (wine[c] == French) /\ (a > b) /\ ( a < c))
    
    %The woman wearing the Yellow shirt is exactly to the left of the 35 years old woman
    /\ exists(a,b in PLACEMENT) (shirt[a] == yellow /\ age[b] == year35 /\ a == b-1)
    
    ;
    
solve satisfy;

    
output
[show(a)
++ "\t" ++ nomSh[fix(shirt[a])] 
++ "\t" ++ nomN[fix(name[a])]
++ "\t" ++ nomSu[fix(surname[a])]
++ "\t" ++ nomP[fix(pasta[a])] 
++ "\t" ++ nomW[fix(wine[a])] 
++ "\t" ++ nomA[fix(age[a])] 
++ "\n"
 | a in PLACEMENT];
