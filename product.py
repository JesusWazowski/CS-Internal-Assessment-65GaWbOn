import tkinter as tk
from tkinter import ttk
import uuid
import json 

###PLACEHOLDER FOR WRITING TO JSON
global recipe_list
recipe_list     = [] # This will be a list of dictionaries, each dictionary representing a recipe
placeholder = "0" ### REPLACE ALL INSTANCES OF THIS WITH JSON BULLSHIT TO MAKE IT WORK
root = tk.Tk()

root.title("Dinner Machine v0.1")
root.geometry("1024x768")

mainScreen = ttk.Frame(root, padding=(40,20,40,20))
mainScreen.grid(row=1, column=1)

### Display the name of the application above other sections
title = ttk.Label(mainScreen, text="Dinner Machine", font=("Arial", 40))
title.grid(row=1, column=1, columnspan=3, pady=(0,10))

divider = ttk.Separator(mainScreen, orient="vertical") # vertical line for visual clarity between sections
divider.grid(row=2, column=2, sticky="ns")

### Section of the menu that should contain all widgets for data entry
recipeInput = ttk.Frame(mainScreen)
recipeInput.grid(row=2, column=1, sticky="nsew")

title = ttk.Label(recipeInput, text="Add New Recipe", font=("Arial", 15), anchor="center")
title.grid(row=1, column=1, columnspan=1, pady=10, padx=20)

r1 = ttk.Frame(recipeInput) # Frame top row of inputs seperately, for clarity
r1.grid(row=2, column=1, columnspan=1, pady=10)

nf = ttk.LabelFrame(r1, text="Name", relief="ridge") # Widgets like these specify the data in each field and create the field for the user
name = ttk.Entry(nf)
nf.grid(row=1, column=1, padx=5, pady=5)
name.grid(row=1, column=1, padx=5, pady=5)

pf = ttk.LabelFrame(r1, text="Protein", relief="ridge", padx=5, pady=5) # Frame for protein input
protein = ttk.Combobox(pf, values=["placeholder"], width=12)
proteinAdd = ttk.Button(pf, text="+", width=1, command=lambda: protein['values'].append(name.get())) # Add button to add new protein to the list
pf.grid(row=1, column=2, padx=5, pady=5)
protein.grid(row=1, column=1, padx=5, pady=5)
proteinAdd.grid(row=1, column=2, padx=5, pady=5)

bottomRow = ttk.Frame(recipeInput)
bottomRow.grid(row=3, column=1, columnspan=1, pady=10)

### Section of the menu that should contain widgets for filtering search and choosing a recipe
recipeFilter = ttk.Frame(mainScreen)
recipeFilter.grid(row=2, column=3, sticky="nsew")

title = ttk.Label(recipeFilter, text="Search Recipe", font=("Arial", 15), anchor="center")
title.grid(row=1, column=1, columnspan=1, pady=10, padx=20)



### Section of the menu that should contain widgets for displaying list of recipes, and sorting that list
recipeView = ttk.Frame(mainScreen, borderwidth=5, relief="ridge")
recipeView.grid(row=3, column=1, columnspan=3, sticky="nsew")


root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

### Prevent resizing of the window beyond minimum size of each combined widget
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()