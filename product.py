import tkinter as tk
from tkinter import StringVar, ttk
import uuid
import json 

root = tk.Tk()
root.title("Dinner Machine v0.1")
root.geometry("1024x768")
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
### Prevent resizing of the window beyond minimum size of each combined widget
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

### JSON handling ###
global recipe_list
recipe_list     = [] # This is a list of dictionaries, each dictionary representing a recipe
id_value = StringVar()
id_value.set(uuid.uuid4()) 

mainScreen = ttk.Frame(root, padding=10)
mainScreen.grid(row=1, column=1)

### Display the name of the application above other sections ### 
title = ttk.Label(mainScreen, text="Dinner Machine", font=("Arial", 40))
title.grid(row=1, column=1, columnspan=3, pady=(0,10))

divider = ttk.Separator(mainScreen, orient="vertical") # vertical line for visual clarity between sections
divider.grid(row=2, column=2, sticky="ns")

### Section of the menu that should contain all widgets for data entry ###
recipeInput = ttk.Frame(mainScreen)
recipeInput.grid(row=2, column=1, sticky="nsew")

title = ttk.Label(recipeInput, text="Add New Recipe", font=("Arial", 21), anchor="center")
title.grid(row=1, column=1, columnspan=1, pady=2, padx=20)

r1 = ttk.Frame(recipeInput) # Frame top row of inputs seperately, for clarity
r1.grid(row=2, column=1, columnspan=1, pady=3)

nf = ttk.LabelFrame(r1, text="Name", relief="ridge") # Widgets like these specify the data in each field and create the field for the user
crm_name = ttk.Entry(nf)
nf.grid(row=1, column=1, padx=5, pady=5)
crm_name.grid(row=1, column=1, padx=5, pady=5)

pf = ttk.LabelFrame(r1, text="Protein", relief="ridge") # Frame for protein input
crm_protein = ttk.Combobox(pf, values=["placeholder"], width=12)
crm_proteinAdd = ttk.Button(pf, text="+", width=1,) # Button to add new proteins to the list of options
pf.grid(row=1, column=2, padx=5, pady=5)
crm_protein.grid(row=1, column=1, padx=(5, 2), pady=5)
crm_proteinAdd.grid(row=1, column=2, padx=(0, 5), pady=5)

lf = ttk.LabelFrame(r1, text="Recipe Link", relief="ridge") # Frame for link input
crm_link = ttk.Entry(lf)
lf.grid(row=1, column=3, padx=5, pady=5)
crm_link.grid(row=1, column=1, padx=5, pady=5)

of = ttk.LabelFrame(r1, text="Liked?", relief="ridge") # Frame for family opinions per recipe
crm_opinion1 = ttk.Checkbutton(of, text="W")
crm_opinion2 = ttk.Checkbutton(of, text="X")
crm_opinion3 = ttk.Checkbutton(of, text="Y")
crm_opinion4 = ttk.Checkbutton(of, text="Z")
of.grid(row=1, column=4, padx=5, pady=5)
crm_opinion1.grid(row=1, column=1)
crm_opinion2.grid(row=1, column=2)
crm_opinion3.grid(row=2, column=1)
crm_opinion4.grid(row=2, column=2)

nf = ttk.LabelFrame(r1, text="Notes", relief="ridge") # Frame for notes input
crm_notes = ttk.Entry(nf, width=30)
nf.grid(row=1, column=5, padx=5, pady=5)
crm_notes.grid(row=1, column=1, padx=5, pady=5)

r2 = ttk.Frame(recipeInput) # Frame for the bottom row of buttons, for clarity
r2.grid(row=3, column=1, columnspan=1, pady=3)

sf = ttk.LabelFrame(r2, text="Servings", relief="ridge") # Frame for servings input
crm_servings = ttk.Spinbox(sf, from_=1, to=100, increment=1, width=5) # Spinbox for selecting number of servings
sf.grid(row=1, column=1, padx=5, pady=5)
crm_servings.grid(row=1, column=1, padx=5, pady=5)

cf = ttk.LabelFrame(r2, text="Cost", relief="ridge") # Frame for cost input
crm_cost = ttk.Spinbox(cf, from_=0.00, to=1000, increment=0.50, width=8) # Spinbox for selecting cost of recipe
dollarSign = ttk.Label(cf, text="$") # Label for dollar sign
dollarSign.grid(row=1, column=0, padx=(5, 0), pady=5, sticky="e") # Position dollar sign to the left of the cost input
cf.grid(row=1, column=2, padx=5, pady=5)
crm_cost.grid(row=1, column=1, padx=(0, 5), pady=5)

tf = ttk.LabelFrame(r2, text="Prep and Cleanup time", relief="ridge") # Frame for time input
crm_prep = ttk.Spinbox(tf, from_=0, to=60*5, increment=5, width=8) # Spinbox for selecting prep time
crm_cleanup = ttk.Spinbox(tf, from_=0, to=60*5, increment=5, width=8) # Spinbox for selecting cleanup time
tf.grid(row=1, column=3, padx=5, pady=5)
crm_prep.grid(row=1, column=1, padx=(5, 4), pady=5, sticky="ew")
crm_cleanup.grid(row=1, column=2, padx=(0, 5), pady=5, sticky="ew")

hf = ttk.LabelFrame(r2, text="Low-fat?", relief="ridge") # Frame for user defined health input
crm_health = ttk.Checkbutton(hf, text="Yes") # Checkbutton for low-fat option
hf.grid(row=1, column=4, padx=5, pady=5)
crm_health.grid(row=1, column=1, padx=5, pady=5)

### Section of the menu that should contain widgets for filtering search and choosing a recipe ###
recipeFilter = ttk.Frame(mainScreen)
recipeFilter.grid(row=2, column=3, sticky="nsew")

title = ttk.Label(recipeFilter, text="Search Recipe", font=("Arial", 21), anchor="center")
title.grid(row=1, column=1, columnspan=1, pady=2, padx=20)

### Section of the menu that should contain widgets for displaying list of recipes, and sorting that list ###
recipeView = ttk.Frame(mainScreen, borderwidth=5, relief="ridge")
recipeView.grid(row=3, column=1, columnspan=3, sticky="nsew")

trv = ttk.Treeview(recipeView, columns=(1,2,3,4,5,6,7,8,9,10,11), show="headings", height=10) # Treeview for displaying recipes
trv.grid(row=1, column=1, columnspan=3, sticky="nsew")
recipeView.grid_rowconfigure(1, weight=1)
recipeView.grid_columnconfigure(1, weight=1)

trv.heading(1, text="Name" , anchor="center")
trv.heading(2, text="Protein" , anchor="center")
trv.heading(3, text="Servings" , anchor="center")
trv.heading(4, text="Cost/Serv" , anchor="center")
trv.heading(5, text="Prep" , anchor="center")
trv.heading(6, text="Cleanup" , anchor="center")
trv.heading(7, text="Low-fat" , anchor="center")
trv.heading(8, text="Recipe Link" , anchor="center")
trv.heading(9, text="Notes" , anchor="center")
trv.heading(10, text="Family Opinions" , anchor="center")
trv.heading(11, text="Edit" , anchor="center")

trv.column(1, width=175, anchor="center", stretch=True) # Name
trv.column(2, width=100, anchor="center") # Protein
trv.column(3, width=70, anchor="center") # Servings
trv.column(4, width=70, anchor="center") # Cost/Serv
trv.column(5, width=70, anchor="center") # Prep Time
trv.column(6, width=70, anchor="center") # Cleanup Time
trv.column(7, width=50, anchor="center") # Low-fat
trv.column(8, width=75, anchor="center") # Recipe Link
trv.column(9, width=150, anchor="center") # Notes
trv.column(10, width=100, anchor="center") # Family Opinions
trv.column(11, width=50, anchor="center") # Edit

### End GUI code            ###
### Data functions below    ###

def load_json_from_file():
    global recipe_list
    with open("c:\\tmp\\recipes.json", "r") as file_handler:
        recipe_list = json.load(file_handler)
    print('file has been read and closed')


def save_json_to_file():
    global recipe_list
    with open("c:\\tmp\\recipes.json", "w") as file_handler:
        json.dump(recipe_list, file_handler, indent=4)
    print('file has been written to and closed')



def remove_all_data_from_trv():
    for item in trv.get_children():
        trv.delete(item)
    

def load_trv_with_json():
    global recipe_list

    remove_all_data_from_trv()

    rowIndex=1

    for key in recipe_list:
        guid_value = key["id"]
        name_ = key["name"]

        trv.insert('', index='end', iid=rowIndex, text="",
                   values=(guid_value, first_name, last_name, cell_phone))
        rowIndex = rowIndex + 1

root.mainloop()