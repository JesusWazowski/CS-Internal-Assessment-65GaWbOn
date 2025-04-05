import tkinter as tk
from tkinter import BooleanVar, StringVar, ttk
import uuid
import json 
import os
import datetime
import random
import webbrowser

root = tk.Tk()
root.title("Dinner Machine v1.0")
root.geometry("1024x768")
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
### Prevent resizing of the window beyond minimum size of each combined widget
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

### JSON handling ###
global recipe_list
global filtered_recipe_list
recipe_list = []  # This is a list of dictionaries, each dictionary representing a recipe
filtered_recipe_list = []  # This is a list of dictionaries, based off recipe_list and user filters
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

    if protein not in proteinValues: # Check if the protein is already in the list
        proteinValues.append(protein) # Add the new protein to the list
        with open(proteins_file_path, "a") as f: # Append the new protein to the file
            f.write(f"\n{protein}") # Add a newline character before adding the new protein
    else:
        print(f"{protein} is already in the list of proteins.")

# Ensure proteins.txt is created in the script directory
proteins_file_path = os.path.join(os.path.dirname(__file__), "proteins.txt")

proteinValues = []  # Declare list of proteins saved by the user
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
recipeFilter = ttk.Frame(mainScreen, height=recipeInput.winfo_height())
recipeFilter.grid(row=2, column=3, sticky="nsew")

title = ttk.Label(recipeFilter, text="Search Recipe", font=("Arial", 21), anchor="center")
title.grid(row=1, column=1, columnspan=100, pady=2, padx=20)

ff = ttk.Frame(recipeFilter) # Frame for the filter input
ff.grid(row=2, column=1, columnspan=100, pady=3)

srf = ttk.LabelFrame(ff, text="Servings>=", relief="ridge") # Frame for servings filter input
rf_servings = ttk.Spinbox(srf, from_=1, to=100, increment=1, width=5)
srf.grid(row=1, column=1, padx=3, pady=3)
rf_servings.grid(row=1, column=1, padx=3, pady=3)

crf = ttk.LabelFrame(ff, text="Cost<=", relief="ridge") # Frame for cost filter input
rf_cost = ttk.Spinbox(crf, from_=0.00, to=1000.00, increment=5.00, width=8) # Spinbox for selecting cost of recipe
dollarSign = ttk.Label(crf, text="$") # Label for dollar sign
dollarSign.grid(row=1, column=0, padx=(5, 0), pady=5, sticky="e") # Position dollar sign to the left of the cost input
crf.grid(row=1, column=2, padx=3, pady=3)
rf_cost.grid(row=1, column=1, padx=(0, 5), pady=5)

trf = ttk.LabelFrame(ff, text="Prep and Cleanup<=", relief="ridge") # Frame for prep and cleanup time filter input
rf_prep = ttk.Spinbox(trf, from_=0, to=300, increment=5, width=8) # Spinbox for selecting prep and cleanup time
rf_cleanup = ttk.Spinbox(trf, from_=0, to=300, increment=5, width=8) # Spinbox for selecting prep and cleanup time
trf.grid(row=2, column=1, columnspan=2, padx=3, pady=3)
rf_prep.grid(row=1, column=1, padx=3, pady=3)
rf_cleanup.grid(row=1, column=2, padx=3, pady=3)

orf = ttk.LabelFrame(ff, text="Likes?", relief="ridge") # Frame for family opinions filter input
rf_opinionW = ttk.Checkbutton(orf, text="W", onvalue="Yes", offvalue="No")
rf_opinionX = ttk.Checkbutton(orf, text="X", onvalue="Yes", offvalue="No")
rf_opinionY = ttk.Checkbutton(orf, text="Y", onvalue="Yes", offvalue="No")
rf_opinionZ = ttk.Checkbutton(orf, text="Z", onvalue="Yes", offvalue="No")
orf.grid(row=1, column=3, padx=3, pady=3)
rf_opinionW.grid(row=1, column=1, padx=3, pady=3)
rf_opinionX.grid(row=1, column=2, padx=3, pady=3)
rf_opinionY.grid(row=2, column=1, padx=3, pady=3)
rf_opinionZ.grid(row=2, column=2, padx=3, pady=3)

hrf = ttk.LabelFrame(ff, text="Low-fat?", relief="ridge") # Frame for health filter input
rf_lowfat = ttk.Checkbutton(hrf, text="Yes", onvalue="Yes", offvalue="No")
hrf.grid(row=2, column=3, padx=3, pady=3)
rf_lowfat.grid(row=1, column=1, padx=3, pady=3)


### Section of the menu that should contain widgets for displaying list of recipes, and sorting that list ###
recipeView = ttk.Frame(mainScreen, borderwidth=5, relief="ridge")
recipeView.grid(row=3, column=1, columnspan=3, sticky="nsew")

trv = ttk.Treeview(recipeView, columns=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,), show="headings", height=18, displaycolumns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14)) # Treeview for displaying recipes
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

def sort_treeview_column(treeview, col, reverse):
    """Sort the Treeview column when a header is clicked."""
    data = [(treeview.set(child, col), child) for child in treeview.get_children('')]
    try:
        # Attempt to sort numerically
        data.sort(key=lambda t: float(t[0]) if t[0].replace('.', '', 1).isdigit() else t[0], reverse=reverse)
    except ValueError:
        # Fallback to string sorting
        data.sort(key=lambda t: t[0], reverse=reverse)

    # Rearrange items in sorted order
    for index, (val, child) in enumerate(data):
        treeview.move(child, '', index)

    # Reverse the sort order for the next click
    treeview.heading(col, command=lambda: sort_treeview_column(treeview, col, not reverse))

# Bind sorting to Treeview headers
for col in range(1, 15):  # Columns 1 to 14 (excluding the hidden ID column)
    trv.heading(col, command=lambda _col=col: sort_treeview_column(trv, _col, False))

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
    

def open_url(url):
    """Open the given URL in the default web browser."""
    if url:
        webbrowser.open(url)

def load_trv_with_json():
    global recipe_list

    remove_all_data_from_trv()

    rowIndex = 1

    for key in recipe_list:
        guid_value = key["id"]
        name = key["name"]
        protein = key["protein"]
        servings = key["servings"] if key["servings"] != "" else 0 # Check if servings is empty, set to 0 if so
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
        last_made = key.get("last_made", "Never")

        # Insert data into Treeview
        trv.insert('', index='end', iid=rowIndex, text="",
                   values=(guid_value, name, protein, servings, f"{cost_per_serving:.2f}", prep, cleanup, lowfat, link, notes, opinionW, opinionX, opinionY, opinionZ, last_made))
        rowIndex = rowIndex + 1

    # Add a button-like behavior to the "Recipe Link" column
    trv.bind("<Button-1>", on_treeview_click)

def on_treeview_click(event):
    """Handle clicks on the Treeview."""
    region = trv.identify("region", event.x, event.y)
    if region == "cell":
        column = trv.identify_column(event.x)
        row_id = trv.identify_row(event.y)
        if column == "#8":  # "Recipe Link" column
            item = trv.item(row_id)
            link = recipe_list[int(row_id) - 1]["link"]
            open_url(link)  # Open the link in the browser

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

    # Disable buttons when no recipe is selected to avoid misleading the user
    btnUpdate["state"]="disabled"
    btnDelete["state"]="disabled"
    btnMake["state"]="disabled"

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
    elif state=='Cancel':
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
    else:
        btnUpdate["state"]="disabled"
        btnDelete["state"]="disabled"
        btnAdd["state"]="normal"


def load_edit_field_with_row_data(_tuple):
    if len(_tuple) == 0:
        return

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



def cancel():
    clear_all_fields()
    change_enabled_state('New')


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

    if name != "":
        process_request('_INSERT_',guid_value,name,protein,servings,cost,prep,cleanup,lowfat,link,notes,W,X,Y,Z)



def update_entry():
    selected_item = trv.selection()  # Get the selected item in the treeview
    if selected_item:  # Ensure an item is selected
        guid_value = trv.item(selected_item, 'values')[0]  # Get the GUID of the selected item
        name = crm_name.get()
        protein = crm_protein.get()
        servings = crm_servings.get()
        cost = crm_cost.get()
        prep = crm_prep.get()
        cleanup = crm_cleanup.get()
        global lowfat
        link = crm_link.get()
        notes = crm_notes.get()
        global W, X, Y, Z

        process_request('_UPDATE_', guid_value, name, protein, servings, cost, prep, cleanup, lowfat, link, notes, W, X, Y, Z)   




def delete_entry():
    selected_item = trv.selection()  # Get the selected item in the treeview
    if selected_item:  # Ensure an item is selected
        guid_value = trv.item(selected_item, 'values')[0]  # Get the GUID of the selected item
        process_request('_DELETE_', guid_value, None, None, None, None, None, None, None, None, None, None, None, None, None)
 



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

def MouseButtonUpCallBack(event):
    currentRowIndex = trv.selection()[0]
    lastTuple = (trv.item(currentRowIndex, 'values'))
    load_edit_field_with_row_data(lastTuple)

    # Enable buttons when a recipe is selected
    btnUpdate["state"] = "normal"
    btnDelete["state"] = "normal"
    btnMake["state"] = "normal"

trv.bind("<ButtonRelease>", MouseButtonUpCallBack)

def choose_recipe():
    global recipe_list
    if not recipe_list:
        print("No recipes available")
        return

    # Calculate weights based on the time since last made
    weights = []
    now = datetime.datetime.now()
    for recipe in recipe_list:
        last_made = recipe.get("last_made", "Never")
        if last_made == "Never":
            # Assign a high weight for recipes never made
            weights.append(1000)
        else:
            # Calculate days since last made
            last_made_date = datetime.datetime.strptime(last_made, "%Y-%m-%d %H:%M:%S")
            days_since_last_made = (now - last_made_date).days
            # Weight is proportional to days since last made
            weights.append(max(days_since_last_made, 1))  # Ensure minimum weight of 1

    # Choose a recipe based on weights
    chosen_recipe = random.choices(filtered_recipe_list, weights=weights, k=1)[0]
    print(f"Chosen Recipe: {chosen_recipe['name']} (Last made: {chosen_recipe.get('last_made', 'Never')})")

    # Highlight the chosen recipe in the Treeview
    for item in trv.get_children():
        if trv.item(item, "values")[0] == chosen_recipe["id"]:
            trv.selection_set(item)
            trv.see(item)
            break

def make_recipe():
    selected_item = trv.selection()  # Get the selected item in the Treeview
    if selected_item:  # Ensure an item is selected
        guid_value = trv.item(selected_item, 'values')[0]  # Get the GUID of the selected item
        row = find_row_in_recipe_list(guid_value)  # Find the row in the recipe list
        if row >= 0:
            # Update the 'last_made' field with the current timestamp
            recipe_list[row]["last_made"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_json_to_file()  # Save the updated data to the JSON file
            load_trv_with_json()  # Reload the Treeview to reflect the changes
            print(f"Recipe '{recipe_list[row]['name']}' marked as made on {recipe_list[row]['last_made']}")

def filter_recipes():
    global recipe_list
    global filtered_recipe_list

    # Get filter values
    servings_filter = rf_servings.get() if rf_servings.get() != "" else 0 # Account for empty boxes by exceeding reasonable value, which nullifies filter logic
    cost_filter = rf_cost.get() if rf_cost.get() != "" else 9999999
    prep_filter = rf_prep.get() if rf_prep.get() != "" else 9999999
    cleanup_filter = rf_cleanup.get() if rf_cleanup.get() != "" else 9999999
    opinionW_filter = rf_opinionW.instate(['selected'])
    opinionX_filter = rf_opinionX.instate(['selected'])
    opinionY_filter = rf_opinionY.instate(['selected'])
    opinionZ_filter = rf_opinionZ.instate(['selected'])
    lowfat_filter = rf_lowfat.instate(['selected'])



    # Filter recipes based on user input
    filtered_recipe_list.clear()
    for recipe in recipe_list:
        if (int(recipe["servings"]) >= int(servings_filter) and
            float(recipe["cost"]) <= float(cost_filter) and
            int(recipe["prep"]) <= int(prep_filter) and
            int(recipe["cleanup"]) <= int(cleanup_filter) and
            (recipe["W"] == "Yes" if opinionW_filter else True) and
            (recipe["X"] == "Yes" if opinionX_filter else True) and
            (recipe["Y"] == "Yes" if opinionY_filter else True) and
            (recipe["Z"] == "Yes" if opinionZ_filter else True) and
            (recipe["lowfat"] == "Yes" if lowfat_filter else True)):
            filtered_recipe_list.append(recipe)

    # Clear the Treeview and load filtered recipes
    remove_all_data_from_trv()
    for recipe in filtered_recipe_list:
        trv.insert('', index='end', iid=recipe["id"], text="", values=(recipe["id"], recipe["name"], recipe["protein"], recipe["servings"], f"{round(float(recipe['cost']) / float(recipe['servings']), 2):.2f}", recipe["prep"], recipe["cleanup"], recipe["lowfat"], recipe["link"], recipe["notes"], recipe["W"], recipe["X"], recipe["Y"], recipe["Z"]))

ButtonFrame = ttk.Frame(r2) # Frame for buttons
ButtonFrame.grid(row=1,column=99,columnspan=1, sticky="sew")

##save=Button(root,text="Save",padx=20,pady=10,command=Save)

btnAdd=ttk.Button(ButtonFrame, text="Add", command=add_entry)
btnAdd.grid(row=1, column=1, padx=1, pady=1)

btnUpdate=ttk.Button(ButtonFrame, text="Update", command=update_entry, state="disabled") # Disabled by default until entry selected
btnUpdate.grid(row=1, column=2, padx=1, pady=1)

btnDelete=ttk.Button(ButtonFrame, text="Delete", command=delete_entry, state="disabled") # Disabled by default until entry selected
btnDelete.grid(row=2, column=1, padx=1, pady=1)

btnClear=ttk.Button(ButtonFrame, text="Cancel", command=cancel)
btnClear.grid(row=2, column=2, padx=1, pady=1)

style = ttk.Style()
style.configure("Blue.TButton", foreground="blue", font=("Arial", 18), relief="raised")

btnChoose = ttk.Button(recipeFilter, text="Choose Recipe", style="Blue.TButton", command=choose_recipe)
btnChoose.grid(row=4, column=1, padx=1, pady=1, columnspan=2, sticky="esw")

btnMake = ttk.Button(recipeFilter, text="Make Recipe", command=make_recipe, state="disabled") # Disabled by default until entry selected
btnMake.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")
recipeFilter.columnconfigure(1, weight=1)
recipeFilter.columnconfigure(2, weight=1)

btnFilter = ttk.Button(recipeFilter, text="Filter", command=filter_recipes)
btnFilter.grid(row=3, column=2, padx=1, pady=1, sticky="nesw")

#btnExit=ttk.Button(ButtonFrame, text="Exit", command=root.quit)
#btnExit.grid(row=1, column=5, padx=1, pady=1)

# Automatically load storage, if there is one
load_json_from_file()
load_trv_with_json()

crm_name.focus_set()
root.mainloop()