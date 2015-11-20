# Convert temperatures from Fahrenheit to Celsius and vice versa

import tkinter as tk

# Previous temperature strings are kept in global variables

oldf = ""
oldc = ""

# Callback function called when the 'convert' button is clicked;
# determine which string changed, convert that temperature, and 
# save the new strings

def convert():
    global oldf, oldc
    ftext = fahr.get()
    ctext = cels.get()
    if (ftext != oldf):
        f2c(ftext)
        oldf = ftext
    elif (ctext != oldc):
        c2f(ctext)
        oldc = ctext

def f2c(temp):
    t = (float(temp) - 32) * 5 / 9
    cels.delete(0, tk.END)
    cels.insert(0, "{:.1f}".format(t))
    
def c2f(temp):
    t = (9 * float(temp) / 5 + 32)
    fahr.delete(0, tk.END)
    fahr.insert(0, "{:.1f}".format(t))
    
# The main window just has two entry boxes (with their labels)
# and a button
    
root = tk.Tk()

flabel = tk.Label(root, text="Fahrenheit")
flabel.grid(row=0, column=0, sticky=tk.W, padx = 20, pady = 30)

clabel = tk.Label(root, text="Celsius")
clabel.grid(row=1, column=0, sticky=tk.W, padx = 20, pady = 10)

fahr = tk.Entry(root)
fahr.grid(row=0, column=1, padx = 20)

cels = tk.Entry(root)
cels.grid(row=1, column=1, padx = 20)

button = tk.Button(root, text='Convert', command=convert) 
button.grid(row=2, column=0, columnspan=2, pady = 30)

if __name__ == "__main__":
    root.mainloop()

