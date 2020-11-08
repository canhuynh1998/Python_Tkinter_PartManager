from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


"""
THESE FUNCTIONS SHOULD BE IN A SEPERATED CLASS
"""
def populate_list():
    # print('Populated')
    # db.fetch() return a row
    part_list.delete(0, END)    # make sure not duplicated
    for row in db.fetch():
        part_list.insert(END, row)  # insert at the END of each row, insert() is a method of Listbox

def add_item():
    if part_text.get() == '' or customer.get() == '' or retailer.get() == '' or price.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_text.get(), customer.get(), retailer.get(), price.get()) #this is inserting into the DB
    part_list.delete(0, END)
    part_list.insert(END, (part_text.get(), customer.get(), retailer.get(), price.get()))
    populate_list()

def select_item(event):
    global selected_item 
    index = part_list.curselection()[0]
    selected_item = part_list.get(index)
    print(selected_item)

    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, selected_item[2])
    retailer_entry.delete(0, END)
    retailer_entry.insert(END, selected_item[3])
    price_entry.delete(0, END)
    price_entry.insert(END, selected_item[4])


def remove_item():
    print('Remove')
    db.remove(selected_item[0])
    populate_list()
    
def update_item():
    print('Updated')

def clear_item():
    print('Cleared')








app = Tk() # this line will create a window object

#Part element
part_text = StringVar()
part_label = Label(app, text="Part Name", font=('bold', 14), pady=20)
part_label.grid(row= 0, column= 0, sticky = W)
part_entry = Entry(app, textvariable =part_text)
part_entry.grid(row= 0, column = 1)

#Customer element
customer = StringVar()
customer_label = Label(app, text="Customer Name", font=('bold', 14))
customer_label.grid(row= 0, column= 2, sticky = W)
customer_entry = Entry(app, textvariable = customer)
customer_entry.grid(row= 0, column = 3)

#Retailer element
retailer = StringVar()
retailer_label = Label(app, text="Retailer Name", font=('bold', 14))
retailer_label.grid(row= 1, column= 0, sticky = W)
retailer_entry = Entry(app, textvariable = retailer)
retailer_entry.grid(row= 1, column = 1)

#Price element
price = StringVar()
price_label = Label(app, text="Price", font=('bold', 14))
price_label.grid(row= 1, column= 2, sticky = W)
price_entry = Entry(app, textvariable =price)
price_entry.grid(row= 1, column = 3)


#Part List( list box)
part_list = Listbox(app, height = 10, width = 50, border = 0)
part_list.grid(row=3, column =0, columnspan= 3, rowspan=6, pady=20, padx= 20)

#Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)

# Blind select
part_list.bind('<<ListboxSelect>>', select_item)



#Add Button
add_button = Button(app, text='Add Part', width = 12, command = add_item )
add_button.grid(row=2, column=0, pady =20)

#Remove Button
remove_button = Button(app, text='Remove', width = 12, command = remove_item )
remove_button.grid(row=2, column=1)

#update Button
update_button = Button(app, text='Update', width = 12, command = update_item )
update_button.grid(row=2, column=2)

#Add Button
clear_button = Button(app, text='Clear', width = 12, command = clear_item )
clear_button.grid(row=2, column=3)



app.title('Part Manager')
app.geometry('800x350') # resize the windown


# Populated data
populate_list()
populate_list()
app.mainloop()  # this line will start the program

