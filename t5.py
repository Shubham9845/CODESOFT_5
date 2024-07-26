import tkinter as tk
from tkinter import messagebox, simpledialog

# Data storage (for demo purposes; in real applications, use a database)
contacts = []

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter the contact's name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter the contact's phone number:")
    email = simpledialog.askstring("Input", "Enter the contact's email:")
    address = simpledialog.askstring("Input", "Enter the contact's address:")
    
    if name and phone:
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and phone number are required.")

# Function to view the contact list
def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if not search_term:
        return
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to update a contact
def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Update", "Select a contact to update.")
        return
    index = selected[0]
    contact = contacts[index]
    
    new_name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact['name'])
    if new_name is not None:
        contact['name'] = new_name
    
    new_phone = simpledialog.askstring("Update", "Enter new phone number:", initialvalue=contact['phone'])
    if new_phone is not None:
        contact['phone'] = new_phone
    
    new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact['email'])
    if new_email is not None:
        contact['email'] = new_email
    
    new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact['address'])
    if new_address is not None:
        contact['address'] = new_address
    
    view_contacts()

# Function to delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Delete", "Select a contact to delete.")
        return
    index = selected[0]
    contact = contacts[index]
    
    confirm = messagebox.askyesno("Delete", f"Are you sure you want to delete {contact['name']}?")
    if confirm:
        del contacts[index]
        view_contacts()

# Create main window
root = tk.Tk()
root.title("Contact Management System")

# Create and place widgets
tk.Button(root, text="Add Contact", command=add_contact).grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=0, column=3, padx=10, pady=10)

contact_list = tk.Listbox(root, width=50, height=15)
contact_list.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Initialize the contact list view
view_contacts()

# Run the application
root.mainloop()
