from Apriori import *
from FPGrowth import *
import tkinter as tk
from tkinter import *


OptionList = ["Apriori","FP-Growth"]
root= tk.Tk()


canvas1 = tk.Canvas(root, width = 800, height = 700,  relief = 'raised')
canvas1.pack()
canvas1.configure(background='white')
label1 = tk.Label(root, text='Market Basket Analysis')
label1.config(font=('helvetica', 14),bg="white")
canvas1.create_window(400, 25, window=label1)


label2 = tk.Label(root, text='File Location')
label2.config(font=('helvetica', 10),bg='white')
canvas1.create_window(120, 70, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(280, 70, window=entry1)

label3 = tk.Label(root, text='Algorithm')
label3.config(font=('helvetica', 10),bg='white')
canvas1.create_window(500, 70, window=label3)

variable = tk.StringVar(root)
variable.set(OptionList[0])

opt = tk.OptionMenu(root, variable, *OptionList)
opt.config(width=12 ,font=('Helvetica', 10))
canvas1.create_window(660, 75, window=opt)

label4 = tk.Label(root, text='Support')
label4.config(font=('helvetica', 10),bg='white')
canvas1.create_window(120, 110, window=label4)

entry2 = tk.Entry (root) 
canvas1.create_window(280, 110, window=entry2)


label5 = tk.Label(root, text='Confidence')
label5.config(font=('helvetica', 10),bg='white')
canvas1.create_window(500, 110, window=label5)

entry3 = tk.Entry (root) 
canvas1.create_window(660, 110, window=entry3)


def analysis ():
    xaxis = 230
    yaxis = 250
    FileLocation = entry1.get()
    Algo = variable.get()
    support = float(entry2.get())
    confidence = float(entry3.get())
    if Algo == 'Apriori':
        result = Apmain(support,confidence,FileLocation)
    elif Algo == 'FP-Growth':
        result = fpmain(support,confidence,FileLocation)
    else:
        print("invalid Algorithm ")
    for data in result:
        if type(data[0]) == tuple:
            quote = ','.join(data[0])
            outText = quote+ "-->" + data[1]
            outConf = "confidence:" + str(data[2])
        else:
            outText = data[0]+ "-->" + data[1]
            outConf = "confidence:" + str(data[2])
        label8 = tk.Label(root,text = "Association Rules")
        label8.config(font=('helvetica', 14),bg='white')
        canvas1.create_window(390, 200 , window=label8)
        
        label6 = tk.Label(root,text = outText)
        label6.config(font=('helvetica', 10),bg='white')
        canvas1.create_window(xaxis, yaxis , window=label6)
        
        label7 = tk.Label(root,text = outConf)
        label7.config(font=('helvetica', 10),bg='white')
        canvas1.create_window(xaxis + 300, yaxis , window=label7)
        yaxis += 25 
        
    root.mainloop()
    
button1 = tk.Button(text='Analyze', command=analysis, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(390, 150, window=button1)







