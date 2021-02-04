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

if "puzzle_logic_3.mzn" in filename:
    arguments = {"monitor":["13'", "15'", "15'6", "21'5", "27'"],"cpu":["2.0MHz", "2.3MHz", "2.5MHz", "2.7MHz", "3.1MHz"],"hdd":["250Gb", "320Gb", "500Gb", "750Gb", "1024Gb"],"price":["699$", "999$", "1149$", "1349$", "1649$"]}
    current = {"cpu":[0,0,0,0,0],"hdd":[0,0,0,0,0],"price":[0,0,0,0,0]}
    currentVert = {"cpu":[0,0,0,0,0],"hdd":[0,0,0,0,0],"price":[0,0,0,0,0]}
    result = { "cpu":[2, 1, 4, 3, 5], "hdd":[1, 2, 5, 3, 4], "price":[1, 2, 3, 4, 5]}
    text = "1. Andrew bought the computer which was three hundred Euros less than the PC\n which has a processor that is 0.4 MHz more powerful than the one which has a 21.5' screen.\n2. The five computers arent the one chosen by Andrew (which doesn't have the 27' screen), the one which has\nthe 2.0-MHz processor, the computer that has a 250 GB HD, the one which has a price of 1,149 Euros and\nthe computer (which doesn't have the 15' screen) that\nhas the HD bigger than the one chosen by Andrew but\nsmaller than that the one which has the 2.7 MHz processor.\n3. The computer with the 320 Gb HD has either the 2.0 or the 2.3 MHz processor.The processor of the\ncomputer which has the 15' screen is more powerful than the one in the computer that costs 999 euros but\nless powerful than the processor that is included in the 1,349 Euros computer.\n4. The computer that has the 27' screen doesn't have the 320 Gb hard drive. The 500 GB HD is included in\nthe computer that has a more powerful professor and a \nlarger size screen than the one which costs 699 euros (which doesn't include the 320 Gb HD).\n\n"
else:
    arguments = {"name":["Jessica","Laurie","Mark","Mary","Sally"],"film":["Minutes","Donnie","Scarecrow","Scarface","Recruit"],"day":["Monday","Tuesday","Wednesday","Thursday","Friday"],"time":["t735","t740","t820","t830","t845"]}
    current = {"film":[0,0,0,0,0],"day":[0,0,0,0,0],"time":[0,0,0,0,0]}
    currentVert = {"film":[0,0,0,0,0],"day":[0,0,0,0,0],"time":[0,0,0,0,0]}
    text = "1. Of the 20-hundreds releases, neither of which was Jessica s choice, one opened the week and one closed the week.\n2. The latest of the 19-hundreds releases was shown at 30 minutes past the hour.\n3. The releases shown before 8:00 pm were on consecutive days, as were the releases shown after 8:00 pm.\n4. One of the men and one of the women had a showing before 8:00 pm, but neither was mid-week.\n5. Mark, whose choice was Scarecrow, had a showing at a time of one hour and five minutes after that of Scarface.\n6. Neither Miss Farmer nor Miss Peters had a showing on an even-numbered day\n7. 88 Minutes showed at a time both 40 minutes to the hour and 40 minutes after the Thursday showing.\n\n"


print(result)

grid = gridperso.Gridperso(arguments,result,current,currentVert,text)

grid.makeGrid()

