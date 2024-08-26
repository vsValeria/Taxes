import tkinter as tk
from tkinter import ttk
from controller import Controller

class TaxesApp:
    def __init__(self, root):
        self.controller=Controller()
        self.root=root
        self.root.title('Taxes')

#Entry and Label for Min tax-id abd Max tax_id
        self.min_tax_id=tk.Label(root, text='Min tax_id')
        self.min_tax_id.grid(row=0,column=0, sticky='s')
        self.min_tax_id_entry=tk.Entry(root)
        self.min_tax_id_entry.grid(row=0, column=1, padx=0, pady=0, sticky='s')

        self.max_tax_id=tk.Label(root, text='Max tax_id')
        self.max_tax_id.grid(row=1, column=0)
        self.max_tax_entry=tk.Entry(root)
        self.max_tax_entry.grid(row=1, column=1)

#Creating Button
        self.filter_button=tk.Button(root, text='Apply Filter', command=self.app_filter)
        self.filter_button.grid(row=2, column=0, columnspan=2, sticky='s')

#Creating style for Table
        style=ttk.Style()
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        fieldbackground="D3D3D3")
        style.configure("Treeview.Heading",
                        background="#4CAF50",
                        foreground="black")

#Creating Table
        self.tree=ttk.Treeview(root, columns=('Tax Description', 'Period Type', 'Taxpayer Number', 'Taxpayer Address', 'Total Due'), show='headings')
        self.tree.heading('Tax Description', text='Tax Description')
        self.tree.heading('Period Type', text='Period Type')
        self.tree.heading('Taxpayer Number', text='Taxpayer Number')
        self.tree.heading('Taxpayer Address', text='Taxpayer Address')
        self.tree.heading('Total Due', text='Total Due')
        self.tree.grid(row=3, column=0, columnspan=2, sticky='e')

        root.grid_rowconfigure(0,weight=1)
        root.grid_columnconfigure(0, weight=1)

#Filling the Table
    def app_filter(self):
        try:
            min_tax=int(self.min_tax_id_entry.get())
            max_tax=int(self.max_tax_entry.get())
            taxes = self.controller.filter_taxes(min_tax, max_tax)
            self.min_tax_id.config(text='Min tax_id')
            self.max_tax_id.config(text='Max tax_id')
            for row in self.tree.get_children():
                self.tree.delete(row)
            for tax in taxes:
                self.tree.insert(parent="", index="end", values=tax)
        except ValueError as e:
            self.min_tax_id.config(text=f"Please, enter a valid integer: {e}")
            self.max_tax_id.config(text=f"Please, enter a valid integer: {e}")


#Creating Scrollbar
        self.vsb=ttk.Scrollbar(root,orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=3, column=3, sticky='ns')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0,weight=1)


if __name__=='__main__':
    root=tk.Tk()
    app=TaxesApp(root)
    root.mainloop()