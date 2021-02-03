include "globals.mzn";

set of int: MONITOR = 1..5;
set of int: PROCESSOR = {20, 23, 25, 27, 31};
set of int: HARDDISK = 1..5;
set of int: PRICE = {699, 999, 1149, 1349, 1649};


int: monit13 = 1;
int: monit15 = 2;
int: monit15_6 = 3;
int: monit21_5 = 4;
int: monit27 = 5;
array [MONITOR] of string: nomM = ["13'", "15'", "15'6", "21'5", "27'"];

int: cpu2 = 20;
int: cpu2_3 = 23;
int: cpu2_5 = 25;
int: cpu2_7 = 27;
int: cpu3_1 = 31;
array [MONITOR] of string: nomPro = ["2.0MHz", "2.3MHz", "2.5MHz", "2.7MHz", "3.1MHz"];

int: hdd_250 = 1;
int: hdd_320 = 2;
int: hdd_500 = 3;
int: hdd_750 = 4;
int: hdd_1024 = 5;
array [MONITOR] of string: nomH = ["250Gb", "320Gb", "500Gb", "750Gb", "1024Gb"];

int: price_699 = 699;
int: price_999 = 999;
int: price_1149 = 1149;
int: price_1349 = 1349;
int: price_1649 = 1649;
array [MONITOR] of string: nomPri = ["699$", "999$", "1149$", "1349$", "1649$"];


array[MONITOR] of var MONITOR: monitor;
array[MONITOR] of var PROCESSOR: cpu;
array[MONITOR] of var HARDDISK: hdd;
array[MONITOR] of var PRICE: price;

constraint all_different(monitor);
constraint all_different(cpu);
constraint all_different(hdd);
constraint all_different(price);
constraint increasing (price);
constraint exists(andrew in MONITOR)(

    %Contrainte
    %1) Andrew bought the computer which was three hundred Euros less than the PC which has a processor that is 0.4 MHz more powerful than the one which has a 21.5' screen.
    
    exists(b, c in MONITOR)((price[andrew] == price[b]-300) /\ (cpu[b] == cpu[c]+4) /\ (monitor[c] == monit21_5) )

    %2) The five computers aren: the one chosen by Andrew (which doesn't have the 27' screen), the one which has the 2.0-MHz processor, the computer that has a 250 GB HD, the one which has a price of 1,149 Euros and the computer (which doesn't have the 15' screen) that has the HD bigger than the one chosen by Andrew but smaller than that the one which has the 2.7 MHz processor
    
     /\ exists(b,c,d,e,f in MONITOR)((monitor[andrew] != monit27) /\ (cpu[b] == 20) /\ ( hdd[c] == hdd_250) /\ (price[d] == 1149)
     /\ ((monitor[e] != monit15) /\ (hdd[e] > hdd[andrew]) /\ ( hdd[e] < hdd[f]) /\ (cpu[f] == 27)) 
     /\ (andrew!=b) /\ (andrew!=c) /\ (andrew!=d) /\ (andrew!=e) /\ (andrew!=f)
     /\ (b!=c) /\ (b!=d) /\ (b!=e)
     /\ (c!=d) /\ (c!=e)
     /\ (d!=e)
     /\ (e!=f))
     );
    
    %3) The computer with the 320 Gb HD has either the 2.0 or the 2.3 MHz processor.The processor of the computer which has the 15' screen is more powerful than the one in the computer that costs 999 euros but less powerful than the processor that is included in the 1,349 Euros computer
    
constraint exists(a in MONITOR) (hdd[a] == hdd_320 /\ (cpu[a] == 20 \/ cpu[a] == 23));
constraint exists(a, b, c in MONITOR) ((monitor[a] == monit15 /\ price[b] == 999 /\ price[c]==1349) /\ (cpu[a] > cpu[b]) /\ (cpu[a] < cpu[c]));

    %4) The computer that has the 27' screen doesn't have the 320 Gb hard drive. The 500 GB HD is included in the computer that has a more powerful professor and a larger size screen than the one which costs 699 euros (which doesn't include the 320 Gb HD)

constraint exists(a in MONITOR) (monitor[a] == monit27 /\ hdd[a] != hdd_320);
constraint exists(a, b in MONITOR) (hdd[a] == hdd_500 /\ price[b] == 699 /\ cpu[a] > cpu[b] /\ monitor[a] > monitor[b] /\ hdd[b] != hdd_320);
    
solve satisfy;

    
output
[show(a)
++ "\t" ++ nomM[fix(monitor[a])] 
++ "\t" ++ show(cpu[a]/10) ++"Mhz"
++ "\t" ++ nomH[fix(hdd[a])]
++ "\t" ++ show(price[a]) ++"$"
++ "\n"
 | a in MONITOR];