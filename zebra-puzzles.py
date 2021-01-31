import tkinter  as tk
from tkinter import ttk

def submit():
    print(combo_shirt_woman_I.get())


window = tk.Tk()
window.title("Zebra puzzles")

tk.Label(window, text = "").grid(column=0, row=0)

tk.Label(window, text = "").grid(column=0, row=1)

tk.Label(window, text = "Shirt").grid(column=0, row=2)
tk.Label(window, text = "Name").grid(column=0, row=3)
tk.Label(window, text = "Surname").grid(column=0, row=4)
tk.Label(window, text = "Pasta").grid(column=0, row=5)
tk.Label(window, text = "Wine").grid(column=0, row=6)
tk.Label(window, text = "Age").grid(column=0, row=7)

tk.Label(window, text = "Woman #1").grid(column=1, row=1)
combo_shirt_woman_I = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_shirt_woman_I.grid(column=1, row=2)
combo_name_woman_I = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_name_woman_I.grid(column=1, row=3)
combo_surname_woman_I = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_surname_woman_I.grid(column=1, row=4)
combo_pasta_woman_I = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_pasta_woman_I.grid(column=1, row=5)
combo_wine_woman_I = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_wine_woman_I.grid(column=1, row=6)
combo_age_woman_I = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_age_woman_I.grid(column=1, row=7)

tk.Label(window, text = "Woman #2").grid(column=2, row=1)

combo_shirt_woman_II = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_shirt_woman_II.grid(column=2, row=2)
combo_name_woman_II = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_name_woman_II.grid(column=2, row=3)
combo_surname_woman_II = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_surname_woman_II.grid(column=2, row=4)
combo_pasta_woman_II = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_pasta_woman_II.grid(column=2, row=5)
combo_wine_woman_II = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_wine_woman_II.grid(column=2, row=6)
combo_age_woman_II = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_age_woman_II.grid(column=2, row=7)

tk.Label(window, text = "Woman #3").grid(column=3, row=1)
combo_shirt_woman_III = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_shirt_woman_III.grid(column=3, row=2)
combo_name_woman_III = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_name_woman_III.grid(column=3, row=3)
combo_surname_woman_III = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_surname_woman_III.grid(column=3, row=4)
combo_pasta_woman_III = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_pasta_woman_III.grid(column=3, row=5)
combo_wine_woman_III = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_wine_woman_III.grid(column=3, row=6)
combo_age_woman_III = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_age_woman_III.grid(column=3, row=7)

tk.Label(window, text = "Woman #4").grid(column=4, row=1)
combo_shirt_woman_VI = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_shirt_woman_VI.grid(column=4, row=2)
combo_name_woman_VI = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_name_woman_VI.grid(column=4, row=3)
combo_surname_woman_VI = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_surname_woman_VI.grid(column=4, row=4)
combo_pasta_woman_VI = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_pasta_woman_VI.grid(column=4, row=5)
combo_wine_woman_VI = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_wine_woman_VI.grid(column=4, row=6)
combo_age_woman_VI = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_age_woman_VI.grid(column=4, row=7)

tk.Label(window, text = "Woman #5").grid(column=5, row=1)
combo_shirt_woman_V = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_shirt_woman_V.grid(column=5, row=2)
combo_name_woman_V = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_name_woman_V.grid(column=5, row=3)
combo_surname_woman_V = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_surname_woman_V.grid(column=5, row=4)
combo_pasta_woman_V = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_pasta_woman_V.grid(column=5, row=5)
combo_wine_woman_V = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_wine_woman_V.grid(column=5, row=6)
combo_age_woman_V = ttk.Combobox(window, values=["blue","green","red","white","yellow"])
combo_age_woman_V.grid(column=5, row=7)

combo_shirt_woman_I.current(1)

tk.Button(window, text="SUBMIT", command=submit).grid(column=5, row=8)
window.mainloop()

# root = Tk()
# root.title("Tk dropdown example")
#
# # Add a grid
# mainframe = Frame(root)
# mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
# mainframe.columnconfigure(0, weight = 1)
# mainframe.rowconfigure(0, weight = 1)
# mainframe.pack(pady = 100, padx = 100)
#
# # Create a Tkinter variable
# tkvar = StringVar(root)
#
# # Dictionary with options
# choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
# tkvar.set('Pizza') # set the default option
#
# popupMenu = OptionMenu(mainframe, tkvar, *choices)
# Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
# popupMenu.grid(row = 2, column =1)
#
# # on change dropdown value
# def change_dropdown(*args):
#     print( tkvar.get() )
#
# # link function to change dropdown
# tkvar.trace('w', change_dropdown)
#
# root.mainloop()


