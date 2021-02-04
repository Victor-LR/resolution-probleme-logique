import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as message_box




class Zebra_GUI:

    def __init__(self, solution):
        self.solution = solution
        self.shirt_values = ["blue", "green", "red", "white", "yellow"]
        self.name_values = ["Andrea", "Holly", "Julie", "Leslie", "Victoria"]
        self.surname_values = ["Brown", "Davis", "Lopes", "Miller", "Wilson"]
        self.pasta_values = ["farfalle", "lasagne", "penne", "spaghetti", "ravioli"]
        self.wine_values = ["Australian", "Argentine", "Chilean", "French", "Italian"]
        self.age_values = ["30", "35", "40", "45", "50"]
        self.combo_boxes = {}
        self.frames = []

    def create_gui(self):
        window = tk.Tk()
        window.title("Zebra puzzles")

        tk.Label(window, text="").grid(column=0, row=0)
        tk.Label(window, text="").grid(column=0, row=1)

        #création d'un label pour les frames
        labels_frame = tk.Frame(window, padx = 5)
        tk.Label(labels_frame, text="Shirt").grid(column=0, row=2)
        tk.Label(labels_frame, text="Name").grid(column=0, row=3)
        tk.Label(labels_frame, text="Surname").grid(column=0, row=4)
        tk.Label(labels_frame, text="Pasta").grid(column=0, row=5)
        tk.Label(labels_frame, text="Wine").grid(column=0, row=6)
        tk.Label(labels_frame, text="Age").grid(column=0, row=7)

        labels_frame.grid(row=2, column=0)

        self.create_combo_boxes(window)

        tk.Button(window, text="SUBMIT", command=self.submit, padx=5, pady=3).grid(column=5, row=8, pady=10)
        tk.Button(window, text="SOLUTION", command=self.resolve, padx=5, pady=3).grid(column=6, row=8, pady=10, padx=10)

        window.mainloop()

    def create_combo_boxes(self, window):
        for i in range(1, 6):
            tk.Label(window, text="Woman #" + str(i)).grid(column=i, row=1)
            frame = tk.Frame(window, relief="solid", bd=1, bg="white", padx = 5, pady = 5)
            combo_shirt = ttk.Combobox(frame, state="readonly", values=self.shirt_values)
            combo_shirt.grid(column=i, row=2)
            combo_shirt.bind('<<ComboboxSelected>>', self.color_change)
            self.combo_boxes['cases' + str(i) + str(2)] = combo_shirt
            combo_name = ttk.Combobox(frame, state="readonly", values=self.name_values)
            combo_name.grid(column=i, row=3)
            combo_name.bind('<<ComboboxSelected>>', self.disable_values)
            self.combo_boxes['cases' + str(i) + str(3)] = combo_name
            combo_surname = ttk.Combobox(frame, state="readonly", values=self.surname_values)
            combo_surname.grid(column=i, row=4)
            combo_surname.bind('<<ComboboxSelected>>', self.disable_values)
            self.combo_boxes['cases' + str(i) + str(4)] = combo_surname
            combo_pasta = ttk.Combobox(frame, state="readonly", values=self.pasta_values)
            combo_pasta.grid(column=i, row=5)
            combo_pasta.bind('<<ComboboxSelected>>', self.disable_values)
            self.combo_boxes['cases' + str(i) + str(5)] = combo_pasta
            combo_wine = ttk.Combobox(frame, state="readonly", values=self.wine_values)
            combo_wine.grid(column=i, row=6)
            combo_wine.bind('<<ComboboxSelected>>', self.disable_values)
            self.combo_boxes['cases' + str(i) + str(6)] = combo_wine
            combo_age = ttk.Combobox(frame, state="readonly", values=self.age_values)
            combo_age.grid(column=i, row=7)
            combo_age.bind('<<ComboboxSelected>>', self.disable_values)
            self.combo_boxes['cases' + str(i) + str(7)] = combo_age
            frame.grid(row=2, column=i, sticky="nesw")
            self.frames.append(frame)

    def submit(self):
        valid = True
        for i in range(1, 6):
            valid = valid and \
                    (self.shirt_values.index(self.combo_boxes['cases' + str(i) + str(2)].get()) == self.solution.shirt[
                        i - 1] - 1) and \
                    (self.name_values.index(self.combo_boxes['cases' + str(i) + str(3)].get()) == self.solution.name[
                        i - 1] - 1) and \
                    (self.surname_values.index(self.combo_boxes['cases' + str(i) + str(4)].get()) ==
                     self.solution.surname[i - 1] - 1) and \
                    (self.pasta_values.index(self.combo_boxes['cases' + str(i) + str(5)].get()) == self.solution.pasta[
                        i - 1] - 1) and \
                    (self.wine_values.index(self.combo_boxes['cases' + str(i) + str(6)].get()) == self.solution.wine[
                        i - 1] - 1) and \
                    (self.age_values.index(self.combo_boxes['cases' + str(i) + str(7)].get()) == self.solution.age[
                        i - 1] - 1)
        if valid:
            message_box.showinfo(title="Result", message="GAGNER ! ")
        else:
            message_box.showinfo(title="Result", message="Perdu ! ")

    def resolve(self):
        for i in range(1, 6):
            self.combo_boxes['cases' + str(i) + str(2)].set(self.shirt_values[self.solution.shirt[i - 1] - 1])
            self.frames[i - 1].config(bg=self.shirt_values[self.solution.shirt[i - 1] - 1])
            self.combo_boxes['cases' + str(i) + str(3)].set(self.name_values[self.solution.name[i - 1] - 1])
            self.combo_boxes['cases' + str(i) + str(4)].set(self.surname_values[self.solution.surname[i - 1] - 1])
            self.combo_boxes['cases' + str(i) + str(5)].set(self.pasta_values[self.solution.pasta[i - 1] - 1])
            self.combo_boxes['cases' + str(i) + str(6)].set(self.wine_values[self.solution.wine[i - 1] - 1])
            self.combo_boxes['cases' + str(i) + str(7)].set(self.age_values[self.solution.age[i - 1] - 1])

    # fonction qui permet de changer la couleur du widget
    def color_change(self, event):
        color = event.widget.get()
        column = event.widget.grid_info()['column']
        self.frames[column-1].config(bg=color)
        self.disable_values(event)

    def get_row_values(self, index):
        switcher = {
            2: self.shirt_values,
            3: self.name_values,
            4: self.surname_values,
            5: self.pasta_values,
            6: self.wine_values,
            7: self.age_values
        }
        return switcher.get(index)

    def used_values(self, index):
        used_values = []
        for i in range(1, 6):
            used_values.append(self.combo_boxes['cases' + str(i) + str(index)].get())

        return used_values

    def disable_values(self, event):
        value = event.widget.get()
        row = event.widget.grid_info()['row']
        values = self.get_row_values(row)
        used_values = self.used_values(row)
        available_values = [v for v in values if v not in used_values]

        for i in range(1,6):
            self.combo_boxes['cases' + str(i) + str(row)]['values'] = available_values + [self.combo_boxes['cases' + str(i) + str(row)].get()]
