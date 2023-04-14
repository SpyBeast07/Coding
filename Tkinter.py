from PIL import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import csv
import webbrowser

Bg = "beige"
app = tk.Tk()
app.geometry('750x750')
app.title('Postal Management System')
app.configure(bg=Bg)

main_frame = tk.Frame(app)

#page1
page1=tk.Frame(main_frame)

page_1_lb = tk.Label(page1, text='Hello welcome to the Postal System', font=('Bold', 20))
page_1_lb.pack()



def click():
    page1.pack_forget()
    page3.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page6.pack_forget()

    page2.pack()

enter1 = tk.Button(page1, text="ENTER",bg=Bg,  width=20, command=click)
enter1.pack(pady=(40, 0))

page1.pack(pady=100)


#page2
page2 = tk.Frame(main_frame)

page2_lb = tk.Label(page2, text='Select the option ', font=('Bold', 20))
page2_lb.pack()

def click1(event):
    if event == "enter2":
        page1.pack_forget()
        page2.pack_forget()
        page5.pack_forget()
        page6.pack_forget()
        page4.pack_forget()
        page3.pack()
    elif event == "enter3":
        page1.pack_forget()
        page2.pack_forget()
        page5.pack_forget()
        page6.pack_forget()
        page3.pack_forget()
        page2.pack_forget()
        page4.pack()
    elif event == "enter4":
        page1.pack_forget()
        page6.pack_forget()
        page3.pack_forget()
        page2.pack_forget()
        page4.pack_forget()
        page5.pack()
    elif event == "enter5":
        page1.pack_forget()
        page3.pack_forget()
        page4.pack_forget()
        page5.pack_forget()
        page2.pack_forget()
        page6.pack()
enter2 = tk.Button(page2, text="Pincode",  font=('Bold', 20) , command=lambda:click1("enter2"))
enter2.pack(pady=(40, 0))

enter3 = tk.Button(page2, text="District Name",  font=('Bold', 20) , command=lambda:click1("enter3"))
enter3.pack(pady=(40, 0))

enter4 = tk.Button(page2, text="City Name",  font=('Bold', 20) , command=lambda:click1("enter4"))
enter4.pack(pady=(40, 0))

enter5 = tk.Button(page2, text="Search on Web",  font=('Bold', 20) , command=lambda:click1("enter5"))
enter5.pack(pady=(40, 0))

def back6():
    page4.pack_forget()
    page3.pack_forget()
    page2.pack_forget()
    page6.pack_forget()
    page5.pack_forget()
    page1.pack()
back6_btn= tk.Button(page2, text="Back"  , bg=Bg , command=back6) 
back6_btn.pack(side=tk.LEFT , pady=(40 , 0)  )

page2.pack(pady=100)

#page3

page3=tk.Frame(main_frame)



def search():
    search_term = entry.get()

    # Check if pincode is 6 digit or not
    if len(search_term) < 6 or len(search_term) > 6:
        results_label.config(text="Invalid Pincode.")
        return
    

    # Read csv file for the searching pincode
    with open('Pincode.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Printing first row in display from the csv file
        column_names = next(csv_reader)

        # Empty list to store results
        results = []

        # Searching for pincode in all the rows of csv file and appending it in the result list
        for row in csv_reader:
            for cell in row:
                if search_term in cell:
                    results.append(row)

    # for displaying results in tabular form
    if len(results) > 0:
        tree = ttk.Treeview(page3)
        tree["columns"] = column_names
        for column in column_names:
            tree.heading(column, text=column)
            tree.column(column, anchor='center')
        for i, row in enumerate(results):
            tree.insert("", i, values=row)
        tree.pack()
    else:
        results_label.config(text="No results found.")







# Label for the search entry
search_label = tk.Label(page3, text="Enter you pincode : ", font=('montessrat', 10))
search_label.pack()

# Box for search_label
entry = tk.Entry(page3)
entry.pack()

# Start search button
search_button = tk.Button(page3, text="Search", command=search, font=('montessrat', 10))
search_button.pack()


# Displaying search results
results_label = tk.Label(page3)
results_label.pack()



def back1():
    page3.pack_forget()
    page4.pack_forget()
    page6.pack_forget()
    page5.pack_forget()
    page2.pack()
back1_btn= tk.Button(page3, text="Back"  , command=back1) 
back1_btn.pack(side=tk.BOTTOM , pady=(40 , 0) )

page3.pack(pady=100)

#page4

page4 = tk.Frame(main_frame)

def search1():
    search_term1 = entry1.get()

    # Read csv file for the searching pincode
    with open('Pincode.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Printing first row in display from the csv file
        column_names = next(csv_reader)

        # Empty list to store results
        results1 = []

        # Searching for pincode in all the rows of csv file and appending it in the result list
        for row in csv_reader:
            for cell in row:
                if search_term1 in cell:
                    results1.append(row)

    # for displaying results in tabular form
    if len(results1) > 0:
        tree = ttk.Treeview(page4)
        tree["columns"] = column_names
        for column in column_names:
            tree.heading(column, text=column)
            tree.column(column, anchor='center')
        for i, row in enumerate(results1):
            tree.insert("", i, values=row)
        tree.pack()
    else:
        results_label1.config(text="No results found.")


# Label for the search entry
search_label1 = tk.Label(page4, text="Enter your District name: ", font=('montessrat', 10))
search_label1.pack()

# Box for search_label
entry1 = tk.Entry(page4)
entry1.pack()

# Start search button
search_button1 = tk.Button(page4, text="Search", command=search1, font=('montessrat', 10))
search_button1.pack()

# Displaying search results
results_label1 = tk.Label(page4)
results_label1.pack()


def back1():
    page3.pack_forget()
    page4.pack_forget()
    page6.pack_forget()
    page5.pack_forget()
    page2.pack()

back1_btn = tk.Button(page4, text="Back", command=back1)
back1_btn.pack(side=tk.BOTTOM, pady=(40, 0))

page4.pack(pady=100)

#page5

page5=tk.Frame(main_frame)

def search2():
    search_term2 = entry2.get()
        # Read csv file for the searching pincode
    with open('Pincode.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Printing first row in display from the csv file
        column_names = next(csv_reader)

        # Empty list to store results
        results2 = []

        # Searching for pincode in all the rows of csv file and appending it in the result list
        for row in csv_reader:
            for cell in row:
                if search_term2 in cell:
                    results2.append(row)

    # for displaying results in tabular form
    if len(results2) > 0:
        tree = ttk.Treeview(page5)
        tree["columns"] = column_names
        for column in column_names:
            tree.heading(column, text=column)
            tree.column(column, anchor='center')
        for i, row in enumerate(results2):
            tree.insert("", i, values=row)
        tree.pack()
    else:
        results_label2.config(text="No results found.")

search_label2 = tk.Label(page5, text="Enter your City name: ", font=('montessrat', 10))
search_label2.pack()
entry2 = tk.Entry(page5)
entry2.pack()
search_button2 = tk.Button(page5, text="Search", command=search2, font=('montessrat', 10))
search_button2.pack()
results_label2 = tk.Label(page5)
results_label2.pack()

def back2():
    page3.pack_forget()
    page4.pack_forget()
    page6.pack_forget()
    page5.pack_forget()
    page2.pack()

back2_btn = tk.Button(page5, text="Back", command=back2)
back2_btn.pack(side=tk.BOTTOM, pady=(40, 0))

page5.pack(pady=100)




#page6
page6=tk.Frame(main_frame)
def find_pincode_location():
    pincode = pincode_entry.get()
    url = "https://www.google.com/maps/search/?api=1&query=" + pincode
    webbrowser.open_new(url)

pincode_label = tk.Label(page6, text="Enter pincode which to find on web :", font=('montessrat', 10))
pincode_label.pack()
pincode_entry = tk.Entry(page6)
pincode_entry.pack()
search_button = tk.Button(page6, text="Search", command=find_pincode_location, font=('montessrat', 10))
search_button.pack()

def back2():
    page3.pack_forget()
    page4.pack_forget()
    page5.pack_forget()
    page6.pack_forget()
    page2.pack()

back_button = tk.Button(page6, text="Back", command=back2)
back_button.pack(side=tk.BOTTOM, pady=(40, 0))

page6.pack()
main_frame.pack(fill=tk.BOTH , expand=True)

app.mainloop()