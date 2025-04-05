import tkinter as tk
from tkinter import BooleanVar, StringVar, ttk
import uuid
import json 
import os

root = tk.Tk()
root.title("Dinner Machine v0.8")
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

def addProtein(protein): # Function to add a new protein to the list of options
    print("THIS IS A DEBUG MESSAGE")
    if protein not in proteinValues: # Check if the protein is already in the list
        proteinValues.append(protein) # Add the new protein to the list
        with open(proteins_file_path, "a") as f: # Append the new protein to the file
            f.write(f"\n{protein}") # Add a newline character before adding the new protein
    else:
        print(f"{protein} is already in the list of proteins.")

# Define the absolute path for proteins.txt
proteins_file_path = os.path.join(os.path.dirname(__file__), "proteins.txt")

proteinValues = []  # Initialize list of proteins saved by the user
if not os.path.exists(proteins_file_path):  # Check if the file doesn't exist, and create it if it doesn't
    with open(proteins_file_path, "w") as f:
        f.write("Ground beef\nChicken Breast\nChicken Thigh")  # Add a few default proteins
        print(f"No proteins.txt file found. Creating a new one at {proteins_file_path}")  # Alert the user
with open(proteins_file_path, "r") as f:  # Read the protein list from the file
    proteinValues.clear()  # Clear the list to avoid duplicates
    for line in f:
        proteinValues.append(line.strip())  # Add each line to the list, removing the newline character

pf = ttk.LabelFrame(r1, text="Protein", relief="ridge") # Frame for protein input
crm_protein = ttk.Combobox(pf, values=proteinValues, width=16)
crm_proteinAdd = ttk.Button(pf, text="+", width=1, command=lambda: addProtein(crm_protein.get())) # Corrected command to defer execution
pf.grid(row=1, column=2, padx=5, pady=5)
crm_protein.grid(row=1, column=1, padx=(5, 2), pady=5)
crm_proteinAdd.grid(row=1, column=2, padx=(0, 5), pady=5)

lf = ttk.LabelFrame(r1, text="Recipe Link", relief="ridge") # Frame for link input
crm_link = ttk.Entry(lf)
lf.grid(row=1, column=3, padx=5, pady=5)
crm_link.grid(row=1, column=1, padx=5, pady=5)



nf = ttk.LabelFrame(r1, text="Notes", relief="ridge") # Frame for notes input
crm_notes = ttk.Entry(nf, width=30)
nf.grid(row=1, column=5, padx=5, pady=5)
crm_notes.grid(row=1, column=1, padx=5, pady=5)

r2 = ttk.Frame(recipeInput, width=r1.winfo_width()) # Frame for the bottom row of buttons, for clarity
r2.grid(row=3, column=1, columnspan=1, pady=3)

sf = ttk.LabelFrame(r2, text="Servings", relief="ridge") # Frame for servings input
crm_servings = ttk.Spinbox(sf, from_=1, to=100, increment=1, width=5) # Spinbox for selecting number of servings
sf.grid(row=1, column=1, padx=5, pady=5)
crm_servings.grid(row=1, column=1, padx=5, pady=5)

cf = ttk.LabelFrame(r2, text="Cost", relief="ridge") # Frame for cost input
crm_cost = ttk.Spinbox(cf, from_=0.00, to=1000.00, increment=5.00, width=8) # Spinbox for selecting cost of recipe
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

### Initializing checkbox values to "No" (default)
W = StringVar(value="No")
X = StringVar(value="No")
Y = StringVar(value="No")
Z = StringVar(value="No")
of = ttk.LabelFrame(r2, text="Liked?", relief="ridge") # Frame for family opinions per recipe
crm_opinionW = ttk.Checkbutton(of, text="W", onvalue="Yes", offvalue="No", variable=W) # Checkbutton for family opinions
crm_opinionX = ttk.Checkbutton(of, text="X", onvalue="Yes", offvalue="No", variable=X) # Letters refer to initials, anonymized here
crm_opinionY = ttk.Checkbutton(of, text="Y", onvalue="Yes", offvalue="No", variable=Y)
crm_opinionZ = ttk.Checkbutton(of, text="Z", onvalue="Yes", offvalue="No", variable=Z)
of.grid(row=1, column=5, padx=5, pady=5)
crm_opinionW.grid(row=1, column=1)
crm_opinionX.grid(row=1, column=2)
crm_opinionY.grid(row=2, column=1)
crm_opinionZ.grid(row=2, column=2)

### Initializing checkbox value to False
lowfat = StringVar(value="No") # default to unfilled value
hf = ttk.LabelFrame(r2, text="Low-fat?", relief="ridge") # Frame for user defined health input
crm_health = ttk.Checkbutton(hf, text="Yes", onvalue="Yes", offvalue="No", variable=lowfat) # Checkbutton for low-fat option
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

trv = ttk.Treeview(recipeView, columns=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,), show="headings", height=21, displaycolumns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14)) # Treeview for displaying recipes
trv.grid(row=1, column=1, columnspan=3, sticky="nsew")
scrollbar = ttk.Scrollbar(trv, orient=tk.VERTICAL)
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
trv.heading(10, text="W" , anchor="center")
trv.heading(11, text="X" , anchor="center")
trv.heading(12, text="Y" , anchor="center")
trv.heading(13, text="Z" , anchor="center")
trv.heading(14, text="Last made" , anchor="center")

trv.column(0) # ID column for internal use, not displayed to user
trv.column(1, width=90, anchor="center", stretch=True) # Name
trv.column(2, width=100, anchor="center") # Protein
trv.column(3, width=70, anchor="center") # Servings
trv.column(4, width=70, anchor="center") # Cost/Serv
trv.column(5, width=70, anchor="center") # Prep Time
trv.column(6, width=70, anchor="center") # Cleanup Time
trv.column(7, width=50, anchor="center") # Low-fat
trv.column(8, width=75, anchor="center") # Recipe Link
trv.column(9, width=150, anchor="center") # Notes
trv.column(10, width=25, anchor="center") # Family Opinion W
trv.column(11, width=25, anchor="center") # Family Opinion X
trv.column(12, width=25, anchor="center") # Family Opinion Y
trv.column(13, width=25, anchor="center") # Family Opinion Z
trv.column(14, width=90, anchor="center") # Edit

### End GUI code            ###
### Data functions below    ###

file_path = os.path.join(os.path.dirname(__file__), "recipes.json") # Location of JSON file, global variable for easy editing

def load_json_from_file():
    global recipe_list
    if os.path.exists(file_path):
        with open(file_path, "r") as file_handler:
            recipe_list = json.load(file_handler)
    else: # If the file doesn't exist, create it
        with open(file_path, "w") as file_handler:
            json.dump([], file_handler)  # Create an empty JSON array
        print(f"File created: {file_path}")
    print('file has been read and closed')


def save_json_to_file():
    global recipe_list
    if os.path.exists(file_path):
        with open(file_path, "w") as file_handler:
            json.dump(recipe_list, file_handler, indent=4)
    else: # If the file doesn't exist, create it, same as above
        with open(file_path, "w") as file_handler:
            json.dump([], file_handler)
        print(f"File created: {file_path}")
        save_json_to_file() # Call the function again to save the data
    print('file has been written to and closed')



def remove_all_data_from_trv(): # Used to clear the treeview, which prevents duplicate data entries
    for item in trv.get_children():
        trv.delete(item)
    

def load_trv_with_json():
    global recipe_list

    remove_all_data_from_trv()

    rowIndex = 1

    for key in recipe_list:
        guid_value = key["id"]
        name = key["name"]
        protein = key["protein"]
        servings = key["servings"]
        cost = key["cost"]
        cost_per_serving = round(float(cost) / float(servings), 2) if float(servings) > 0 else 0  # Calculate cost per serving
        prep = key["prep"]
        cleanup = key["cleanup"]
        lowfat = key["lowfat"]
        link = key["link"]
        notes = key["notes"]
        opinionW = key["W"]
        opinionX = key["X"]
        opinionY = key["Y"]
        opinionZ = key["Z"]

        trv.insert('', index='end', iid=rowIndex, text="",
                   values=(guid_value, name, protein, servings, f"{cost_per_serving:.2f}", prep, cleanup, lowfat, link, notes, opinionW, opinionX, opinionY, opinionZ))
        rowIndex = rowIndex + 1

def clear_all_fields():
    # Clear Entries
    crm_name.delete(0,'end')
    crm_protein.delete(0,'end')
    crm_notes.delete(0,'end')
    crm_link.delete(0,'end')
    # Clear spinboxes
    crm_servings.delete(0,'end')
    crm_cost.delete(0,'end')
    crm_prep.delete(0,'end')
    crm_cleanup.delete(0,'end')
    # Clear checkboxes
    W.set("No")
    X.set("No")
    Y.set("No")
    Z.set("No")
    lowfat.set("No")

    crm_name.focus_set()
    id_value.set(uuid.uuid4())

### Simple search function for IDs
def find_row_in_recipe_list(guid_value):
    global recipe_list
    row     = 0
    found   = False

    for rec in recipe_list:
        if rec["id"] == guid_value:
            found = True
            break
        row = row+1

    if(found==True):
        return(row)

    return(-1)

### Regulate functions of buttons that control data based on if data is selected or not ###
def change_enabled_state(state):

    if state == 'Edit':
        btnUpdate["state"]="normal"
        btnDelete["state"]="normal"
        btnAdd["state"]="disabled"
    elif state=='Cancel':
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
        btnAdd["state"]="disabled"
    else:
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
        btnAdd["state"]="normal"

# --review=Y
def load_edit_field_with_row_data(_tuple):
    if len(_tuple) == 0:
        return
    print(_tuple)
    clear_all_fields()

    # Update id_value with the GUID of the selected row
    id_value.set(_tuple[0])  # GUID

    crm_name.insert(0, _tuple[1])  # Name
    crm_protein.insert(0, _tuple[2])  # Protein
    crm_servings.insert(0, _tuple[3])  # Servings
    crm_cost.insert(0, round((float(_tuple[4]) * float(_tuple[3])), 2))  # Total cost
    crm_prep.insert(0, _tuple[5])  # Prep time
    crm_cleanup.insert(0, _tuple[6])  # Cleanup time
    crm_link.insert(0, _tuple[8])  # Recipe link
    crm_notes.insert(0, _tuple[9])  # Notes

    # Set the lowfat checkbox based on the value
    lowfat.set("Yes" if _tuple[7] == "Yes" else "No")

    # Set the opinion checkboxes based on the values
    W.set("Yes" if _tuple[10] == "Yes" else "No")
    X.set("Yes" if _tuple[11] == "Yes" else "No")
    Y.set("Yes" if _tuple[12] == "Yes" else "No")
    Z.set("Yes" if _tuple[13] == "Yes" else "No")


# --review=Y
def cancel():
    clear_all_fields()
    change_enabled_state('New')

# --review=Y
def add_entry():
    guid_value = id_value.get()
    name = crm_name.get()
    protein = crm_protein.get()
    servings = crm_servings.get()
    cost = crm_cost.get()
    prep = crm_prep.get()
    cleanup = crm_cleanup.get()
    global lowfat # Used existing variable for lowfat checkbox
    link = crm_link.get()
    notes = crm_notes.get()
    global W # Used existing variable for checkboxes here
    global X
    global Y
    global Z

    process_request('_INSERT_',guid_value,name,protein,servings,cost,prep,cleanup,lowfat,link,notes,W,X,Y,Z)


# --review=Y
def update_entry():
    guid_value = id_value.get()
    name = crm_name.get()
    protein = crm_protein.get()
    servings = crm_servings.get()
    cost = crm_cost.get()
    prep = crm_prep.get()
    cleanup = crm_cleanup.get()
    global lowfat # Once again used existing variable for lowfat checkbox
    link = crm_link.get()
    notes = crm_notes.get()
    global W # Used existing variable for checkboxes here
    global X
    global Y
    global Z

    process_request('_UPDATE_',guid_value,name,protein,servings,cost,prep,cleanup,lowfat,link,notes,W,X,Y,Z)   



# --review=Y
def delete_entry():
    guid_value = id_value.get()
    process_request('_DELETE_',guid_value,None,None,None,None,None,None,None,None,None,None,None,None,None)
 


# --review=Y
def process_request(command_type, guid_value, name, protein, servings, cost, prep, cleanup, lowfat, link, notes, W, X, Y, Z):
    global recipe_list

    if command_type == "_UPDATE_":
        row = find_row_in_recipe_list(guid_value)
        if row >= 0:
            dict = {
                "id": guid_value,
                "name": name,
                "protein": protein,
                "servings": servings,
                "cost": cost,
                "prep": prep,
                "cleanup": cleanup,
                "lowfat": lowfat.get(),  # Retrieve the value of crm_health
                "link": link,
                "notes": notes,
                "W": W.get(),
                "X": X.get(),
                "Y": Y.get(),
                "Z": Z.get()
            }
            recipe_list[row] = dict

            # Update the Treeview directly
            trv.item(row + 1, values=(
                guid_value, name, protein, servings, 
                f"{round(float(cost) / float(servings), 2) if float(servings) > 0 else 0:.2f}", 
                prep, cleanup, lowfat.get(), link, notes, 
                W.get(), X.get(), Y.get(), Z.get()
            ))

    elif command_type == "_INSERT_":
        dict = {
            "id": guid_value,
            "name": name,
            "protein": protein,
            "servings": servings,
            "cost": cost,
            "prep": prep,
            "cleanup": cleanup,
            "lowfat": lowfat.get(),  # Retrieve the value of crm_health
            "link": link,
            "notes": notes,
            "W": W.get(),
            "X": X.get(),
            "Y": Y.get(),
            "Z": Z.get()
        }
        recipe_list.append(dict)

    elif command_type == "_DELETE_":
        row = find_row_in_recipe_list(guid_value)
        if row >= 0:
            del recipe_list[row]

    save_json_to_file()
    if command_type != "_UPDATE_":  # Reload Treeview only for insert or delete
        load_trv_with_json()
    clear_all_fields()


# --review=Y
def MouseButtonUpCallBack(event):
    currentRowIndex = trv.selection()[0]
    lastTuple = (trv.item(currentRowIndex,'values'))
    load_edit_field_with_row_data(lastTuple)

    change_enabled_state('Edit')


# --review=Y
trv.bind("<ButtonRelease>",MouseButtonUpCallBack)

ButtonFrame = ttk.Frame(r2) # Frame for buttons
ButtonFrame.grid(row=1,column=99,columnspan=1, sticky="sew")

##save=Button(root,text="Save",padx=20,pady=10,command=Save)

btnAdd=ttk.Button(ButtonFrame, text="Add", command=add_entry)
btnAdd.grid(row=1, column=1, padx=1, pady=1)

btnUpdate=ttk.Button(ButtonFrame, text="Update", command=update_entry)
btnUpdate.grid(row=1, column=2, padx=1, pady=1)

btnDelete=ttk.Button(ButtonFrame, text="Delete", command=delete_entry)
btnDelete.grid(row=2, column=1, padx=1, pady=1)

btnClear=ttk.Button(ButtonFrame, text="Cancel", command=cancel)
btnClear.grid(row=2, column=2, padx=1, pady=1)

##### Move this button to Search Frame probably
#btnMake=ttk.Button(ButtonFrame, text="Make Recipe",) # Add date reset command here
#btnMake.grid(row=1, column=3, padx=1, pady=1, rowspan=2)

#btnExit=ttk.Button(ButtonFrame, text="Exit", command=root.quit)
#btnExit.grid(row=1, column=5, padx=1, pady=1)

# Automatically load storage, if there is one
load_json_from_file()
load_trv_with_json()

crm_name.focus_set()
root.mainloop()