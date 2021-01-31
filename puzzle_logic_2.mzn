include "globals.mzn";

set of int: NAME = 1..5;
set of int: FILM = 1..5;
set of int: DAY = 1..5;
set of int: TIME = 1..5;

int: Jessica = 1;
int: Laurie = 2;
int: Mark = 3;
int: Mary = 4;
int: Sally = 5;
array [NAME] of string: nomN = ["Jesssica","Laurie","Mark","Mary","Sally"];

int: Minutes = 1;
int: Donnie = 2;
int: Scarecrow = 3;
int: Scarface = 4;
int: Recruit = 5;
array [FILM] of string: nomF = ["Minutes","Donnie","Scarecrow","Scarface","Recruit"];

int: Moday = 1;
int: Tuesday = 2;
int: Wednesday = 3;
int: Thursday = 4;
int: Friday = 5;
array [DAY] of string: nomD = ["Moday","Tuesday","Wednesday","Thursday","Friday"];

int: t735 = 1;
int: t740 = 2;
int: t820 = 3;
int: t830 = 4;
int: t845 = 5;
array [TIME] of string: nomT = ["t735","t740","t820","t830","t845"];

array [NAME] of var FILM : film;
array [NAME] of var DAY : day;
array [NAME] of var TIME : time;

constraint all_different(film);
constraint all_different(day);
constraint all_different(time);


% indice 1
% Of the 20-hundreds releases, neither of which was Jessica's choice, one opened the week and one closed the week
constraint film[Jessica] != Minutes /\ film[Jessica] != Recruit;
constraint exists(n in NAME)((film[n] == Minutes /\ day[n] == Moday ) \/ (film[n] == Recruit /\ day[n] == Moday ));
constraint exists(n in NAME)((film[n] == Minutes /\ day[n] == Friday ) \/ (film[n] == Recruit /\ day[n] == Friday ));


% indice 2
%The latest of the 19-hundreds releases was shown at 30 minutes past the hour.
constraint exists(n in NAME)(film[n] == Donnie /\ time[n] == t830);

% indice 3
% The releases shown before 8:00 pm were on consecutive days, as were the releases shown after 8:00 pm.
constraint exists(n,m in NAME)(time[n] == t735 /\ time[m] == t740 /\ abs(day[n]-day[m])==1);
constraint exists(n,m,a in NAME)(time[n] == t820 /\ time[m] == t830 /\ time[a] == t845 
/\ ( (abs(day[n]-day[m])==1 /\ abs(day[n]-day[a])==1) 
  \/ (abs(day[m]-day[n])==1 /\ abs(day[m]-day[a])==1) 
  \/ (abs(day[a]-day[n])==1 /\ abs(day[a]-day[m])==1)) );

% indice 4
% One of the men and one of the women had a showing before 8:00pm, but neither was mid-week
constraint exists(m,w in NAME)((m==Mark \/ m==Laurie) /\ (w==Jessica \/ w==Mary \/ w==Sally)
           /\ (time[m]==t735 \/ time[m]==t740) /\ (time[w]==t735 \/ time[w]==t740) 
           /\ (day[m] != Wednesday /\ day[w] != Wednesday));

% indice 5 
% Mark, whose choice was Scarecrow, had a showing at a time of one hour and five minutes after that of Scarface.
constraint(film[Mark]==Scarecrow /\ time[Mark] == t845);
constraint exists(n in NAME)(n != Mark /\ film[n]==Scarface /\ time[n]==t740);

% indice 6 
% Neither Miss Farmer nor Miss Peters had a showing on an even-numbered day
constraint day[Jessica] mod 2 != 0 /\ day[Mary] mod 2 != 0;

solve satisfy;

output
[nomN[a]
++ "\t" ++ show(NAME[a])
++ "\t" ++ nomF[fix(film[a])] ++" = "++ show(film[a]) 
++ "\t" ++ nomD[fix(day[a])] ++" = "++ show(day[a])
++ "\t" ++ nomT[fix(time[a])] ++" = "++ show(time[a])
++ "\n" 
| a in NAME];