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

### Display the name of the application above other sections ### 
title = ttk.Label(mainScreen, text="Dinner Machine", font=("Arial", 40))
title.grid(row=1, column=1, columnspan=3, pady=(0,10))

divider = ttk.Separator(mainScreen, orient="vertical") # vertical line for visual clarity between sections
divider.grid(row=2, column=2, sticky="ns")

### Section of the menu that should contain all widgets for data entry ###
recipeInput = ttk.Frame(mainScreen)
recipeInput.grid(row=2, column=1, sticky="nsew")

title = ttk.Label(recipeInput, text="Add New Recipe", font=("Arial", 15), anchor="center")
title.grid(row=1, column=1, columnspan=1, pady=2, padx=20)

r1 = ttk.Frame(recipeInput) # Frame top row of inputs seperately, for clarity
r1.grid(row=2, column=1, columnspan=1, pady=10)

nf = ttk.LabelFrame(r1, text="Name", relief="ridge") # Widgets like these specify the data in each field and create the field for the user
name = ttk.Entry(nf)
nf.grid(row=1, column=1, padx=5, pady=5)
name.grid(row=1, column=1, padx=5, pady=5)

pf = ttk.LabelFrame(r1, text="Protein", relief="ridge") # Frame for protein input
protein = ttk.Combobox(pf, values=["placeholder"], width=12)
proteinAdd = ttk.Button(pf, text="+", width=1,) # Button to add new proteins to the list of options
pf.grid(row=1, column=2, padx=5, pady=5)
protein.grid(row=1, column=1, padx=(5, 2), pady=5)
proteinAdd.grid(row=1, column=2, padx=(0, 5), pady=5)

lf = ttk.LabelFrame(r1, text="Recipe Link", relief="ridge") # Frame for link input
link = ttk.Entry(lf)
lf.grid(row=1, column=3, padx=5, pady=5)
link.grid(row=1, column=1, padx=5, pady=5)

of = ttk.LabelFrame(r1, text="Liked?", relief="ridge") # Frame for family opinions per recipe
opinion1 = ttk.Checkbutton(of, text="W")
opinion2 = ttk.Checkbutton(of, text="X")
opinion3 = ttk.Checkbutton(of, text="Y")
opinion4 = ttk.Checkbutton(of, text="Z")
of.grid(row=1, column=4, padx=5, pady=5)
opinion1.grid(row=1, column=1)
opinion2.grid(row=1, column=2)
opinion3.grid(row=2, column=1)
opinion4.grid(row=2, column=2)

nf = ttk.LabelFrame(r1, text="Notes", relief="ridge") # Frame for notes input
notes = ttk.Entry(nf, width=30)
nf.grid(row=1, column=5, padx=5, pady=5)
notes.grid(row=1, column=1, padx=5, pady=5)

r2 = ttk.Frame(recipeInput) # Frame for the bottom row of buttons, for clarity
r2.grid(row=3, column=1, columnspan=1, pady=10)

sf = ttk.LabelFrame(r2, text="Servings", relief="ridge") # Frame for servings input
servings = ttk.Spinbox(sf, from_=1, increment=1, width=5) # Spinbox for selecting number of servings
sf.grid(row=1, column=1, padx=5, pady=5)
servings.grid(row=1, column=1, padx=5, pady=5)

cf = ttk.LabelFrame(r2, text="Cost", relief="ridge") # Frame for cost input
cost = ttk.Spinbox(cf, from_=0, increment=0.01, width=5) # Spinbox for selecting cost of recipe
cf.grid(row=1, column=2, padx=5, pady=5)
cost.grid(row=1, column=1, padx=5, pady=5)

tf = ttk.LabelFrame(r2, text="Prep and Cleanup time", relief="ridge") # Frame for time input
prep = 





### Section of the menu that should contain widgets for filtering search and choosing a recipe ###
recipeFilter = ttk.Frame(mainScreen)
recipeFilter.grid(row=2, column=3, sticky="nsew")

title = ttk.Label(recipeFilter, text="Search Recipe", font=("Arial", 15), anchor="center")
title.grid(row=1, column=1, columnspan=1, pady=2, padx=20)



### Section of the menu that should contain widgets for displaying list of recipes, and sorting that list ###
recipeView = ttk.Frame(mainScreen, borderwidth=5, relief="ridge")
recipeView.grid(row=3, column=1, columnspan=3, sticky="nsew")


root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

### Prevent resizing of the window beyond minimum size of each combined widget
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()