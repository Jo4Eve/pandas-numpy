#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import*  
#from tkinter import ttk

window = Tk()
window.title('Main Frame')

window.geometry("500x800")

left = Frame(borderwidth = 5)
left.pack(side = 'right')


listbox = Listbox(window, bg = 'pink')
listbox.pack(anchor = "nw")
listbox.insert(1, 'Year 3')
listbox.insert(2, 'Year 4')
listbox.insert(3, 'Year 5')
listbox.insert(4, 'Year 6')

spin = Spinbox(window, values = ('Josh',"Eve",'Craig','Demi','Lily') )
spin.pack()

text = Label(window,text = 'Student Details')
text.pack(anchor = "w")

cButton = ['Name', 'ID','Grades']
y = IntVar()
for i in range (len(cButton)):
    checkButton = Checkbutton(window, text = cButton[i],
                    variable = y,
                     onvalue = 1,
                     offvalue = 0,
                     height = 2,
                     width = 10,)
    checkButton.pack(anchor = "w")

subjects = ['Maths', 'English', 'Geograpghy', 'Physics']
x = IntVar()
for i in range(len(subjects)):
    radioButton = Radiobutton(window, text = subjects[i], variable = x, value = i, padx = 25)
    radioButton.pack(anchor = "w")
    
msg = Message(left, text = 'How has your day been?')
msg.config(bg = 'violet')
msg.pack()

scale = Scale(left,from_= 40, to = 0 , orient = HORIZONTAL)
scale.pack()

text1 = Text(left, bg = 'green', width = 20, height = 10)
text1.pack()

button = Button(left, text = "Exit")
button.pack()



window.mainloop()


# In[ ]:


import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Main Frame')

window.geometry("500x400")


window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

cButton = ['Name', 'ID','Grades']
y = tk.IntVar()
for i in range (len(cButton)):
    text = ttk.Label(window,text = 'Student Details')
    text.grid(row = 0, column  = 0, sticky = 'nw')
    checkButton = ttk.Checkbutton(window,text = cButton[i],
                    variable = y,
                     onvalue = 1,
                     offvalue = 0,
                     width = 10)
    checkButton.grid(column = 0, row = 1+(i), sticky = tk.NW)
    
subjects = ['Maths', 'English', 'Geograpghy', 'Physics']
x = tk.IntVar()
for i in range(len(subjects)):
    radioButton = ttk.Radiobutton(window,text = subjects[i], variable = x, value = i)
    radioButton.grid(row = 1+(i), column = 0, sticky = tk.N)
    
msg = tk.Message(window, text = 'How has your day been?').grid(row = 2, column = 0, sticky = 'nw')


listItems = ('Year 3', 'Year 4','Year 5','Year 6')
items = tk.StringVar(value = listItems)
listbox = tk.Listbox(window, height = 4, listvariable = items, selectmode = 'extended')
listbox.grid(columns = 1, row = 1, sticky = 'nesw')

spin = tk.Spinbox(window, values = ('Josh',"Eve",'Craig','Demi','Lily') )
spin.grid(columns = 1, row = 0, sticky = 'n')

scale = tk.Scale(window,from_= 40, to = 0 ).grid(row = 0, column = 1, sticky = 'nw')


window.mainloop()


# In[ ]:


from tkinter import *

window = Tk()
window.title("Canvas Example")
c = Canvas(window,width=350,height=400)
c.pack()
c.create_rectangle(40, 40, 110, 110, fill="#FD6707", outline='#C5D906',)

window.mainloop()


# In[ ]:





# In[ ]:




