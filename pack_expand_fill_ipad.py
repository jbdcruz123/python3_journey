#RSM 7/4/2022 pack sample
#topics ipady ipadx expand fill

import tkinter as tk
from tkinter import messagebox

#https://www.pythontutorial.net/tkinter/tkinter-pack/#:~:text=The%20pack()%20method%20is,ipady%20%2C%20padx%20%2C%20and%20pady%20.
def fInt_chld(p):#1c
      i = 0
      while i< p: #2
            chld.append(None)
            i+=1
      #2
      print(f"L40 all available slots: {chld}\n")
#1c

def fClose_all_chld(p):#1d
      close_all = True      
      i = 0
      while i < p:#2
            if not isinstance( chld[i], type(None)):#3
                  close_all = False
                  break
            #3
            i+=1
      #2
      return close_all
#1d

def fPrnt_close(): #1d
      
      
      if not messagebox.askyesno(title = "text", message = "exit mo na ba y/ n") : #3
            return
      #3
           
      if not fClose_all_chld(10):#2
            messagebox.showinfo(title = "text", message = "mayroon nakabukas sa client") 
            return         
      #2

      prnt.destroy()
       
#1d

def fClose(p):#1b
           
      chld[p].destroy()
      chld[p] = None
      print(f"L30 p {p}, chld[p] {chld[p]} \n")
#1b      

def fSme_clas(p):#1c

      if isinstance(chld[p], tk.Toplevel):#2
            messagebox.showinfo(title = "text", message = f"kaylangan sarado ung unang binuksan ang child {p+1}\n(ito ung chld index {p})\n")

            return True
      #2
      return False
#1c

def fSmpl_1(p):#1a

      print(f"L10 p {p}, chld[p] {chld[p]}\n")

      if fSme_clas(p):#2
            return 
      #2
      
      '''This example uses the ipadx and ipady for internal padding. These options create 
      spaces between the labels and their borders.
      As you can see, the pack geometry manager piles the label widgets on top of each other. '''
      
      chld[p] = tk.Toplevel(prnt)
      chld[p].title(f"sample {p+1}")
      chld[p].geometry("400x300")
      chld[p].resizable(False, False)
      #this will show only in app menu close  
      chld[p].protocol("WM_DELETE_WINDOW", lambda : fClose(p))      
      
      box1 = tk.Label(chld[p], text="Box 1", bg="green", fg="white" )
      '''1) Using the fill option
      The fill option accepts three values 'x', 'y', and 'both'. These options allow the widget to
       fill available space along the x-axis, y-axis, and both.
      If you add the fill='x' to the first widget like this:'''
      
      box1.pack( ipadx=10, ipady=10, fill ="x" )

      # box 2
      box2 = tk.Label(chld[p], text="Box 2", bg="red", fg="white")

      '''However, if you change to fill='y' as follows:
      you’ll see that the first widget doesn’t fill all space vertically:
      When you use the fill option, the area of each widget can fill is constrained by those allocated areas.'''

      box2.pack( ipadx=10, ipady=10, fill ="y")
      
      
#1a

def fSmpl_2(p):#1a

      print(f"L20 p {p}, chld[p] {chld[p]}\n")
      if fSme_clas(p):#2
            return 
      #2

      
      chld[p] = tk.Toplevel(prnt)
      chld[p].title(f"sample {p+1}")
      chld[p] .geometry("400x300")
      chld[p] .resizable(False, False)
      chld[p].protocol("WM_DELETE_WINDOW", lambda: fClose(p))

      box1 = tk.Label(chld[p] , text="Box 1", bg="green", fg="white" )
      
      '''Using the expand option
      The expand option allocates more available space to a widget.
      If you add the expand option to the first widget:
      The first widget takes all available space in the window except for the space 
      allocated to the second widget. Since the first widget doesn’t have the fill option, 
      it floats in the middle of the allocated area. If you set fill to 'both': 
      If you add the expand option to both widgets, the pack manager will allocate the space 
      to them evenly.
      '''
      #fill() pupunoin ung isang side, pero pag both lahat ng side
      box1.pack( ipadx=10, ipady=10, fill = "both", expand = True )

      # box 2
      box2 = tk.Label(chld[p] , text="Box 2", bg="red", fg="white")

      box2.pack( ipadx=10, ipady=10, expand=True)
      
#1a

def fSmpl_3(p):#1a

      '''Using side option
      The side option specifies the alignment of the widget. It can be 'left', 'top', 
      'right', and 'bottom'. The side defaults to 'top'. In other words, widgets are 
      aligned to the top of their container. '''


      print(f"L60 p {p}, chld[p] {chld[p]}\n")

      if fSme_clas(p):#2
            return 
      #2
            
      chld[p] = tk.Toplevel(prnt)
      chld[p].title(f"sample {p+1}")
      chld[p].geometry("400x400")
      chld[p].resizable(False, False)
      #this will show only in app menu close  
      chld[p].protocol("WM_DELETE_WINDOW", lambda : fClose(p))            

      box1 = tk.Label(chld[p], text="Box 1", bg="green", fg="white" )

      box1.pack( ipadx=10, ipady=10, expand=True, fill = "both", side = "left")

      # box 2
      box2 = tk.Label(chld[p], text="Box 2", bg="red", fg="white")

      box2.pack( ipadx=10, ipady=10, expand= True, fill = "both")
      
      '''In this example, the expand option may not work as you expected. The reason is
      that widgets have different sides.
      ' '''         
#1a

def fSmpl_4(p):#1a

      print(f"L70 p {p}, chld[p] {chld[p]}\n")

      if fSme_clas(p):#2
            return 
      #2
            
      chld[p] = tk.Toplevel(prnt)
      chld[p].title(f"sample {p+1}")
      chld[p].geometry("400x300")
      chld[p].resizable(False, False)
      #this will show only in app menu close  
      chld[p].protocol("WM_DELETE_WINDOW", lambda : fClose(p))    
  
      '''To make their space even again, you can set the side of both widgets to 'left'
      or one is 'left' and the other is 'right' '''

      box1 = tk.Label(chld[p], text="Box 1", bg="green", fg="white" )

      box1.pack( ipadx=10, ipady=10, expand= True, fill = "both", side= "left" )

      # box 2
      box2 = tk.Label(chld[p], text="Box 2", bg="red", fg="white")

      box2.pack( ipadx=10, ipady=10, expand = True, fill = "both", side = "left")
            
#1a

def fSmpl_5(p):#1a

      print(f"L80 p {p}, chld[p] {chld[p]}\n")
            
      ''' When to use the pack geometry manager
      The geometry manager is suitable for the following:
      Placing widgets in a top-down layout.
      Placing widgets side by side
      See the following example: '''

      if fSme_clas(p):#2
            return 
      #2
            
      chld[p] = tk.Toplevel(prnt)
      chld[p].title(f"sample {p+1}")
      chld[p].geometry("400x300")
      chld[p].resizable(False, False)
      #this will show only in app menu close  
      chld[p].protocol("WM_DELETE_WINDOW", lambda : fClose(p))      
      
      tk.Label(chld[p], text="Box 1", bg="red", fg="white" ).pack( ipadx=10, ipady=10, fill = "x" )

      tk.Label(chld[p], text="Box 2", bg="green", fg="white").pack( ipadx=10, ipady=10, fill = "x")
      
      tk.Label(chld[p], text="Box 3", bg="blue", fg="white").pack( ipadx=10, ipady=10, fill = "x")      

      tk.Label(chld[p], text="Left", bg="cyan", fg="black").pack( ipadx=10, ipady=10, expand = True, \
      fill = "both", side = "left")

      tk.Label(chld[p], text="Center", bg="magenta", fg="black").pack( ipadx=10, ipady=10, expand = True, \
      fill = "both", side = "left")

      tk.Label(chld[p], text="Right", bg="yellow", fg="black").pack( ipadx=10, ipady=10, expand = True, \
      fill = "both", side = "left")

      ''' Summary
      Use Tkinter pack geometry manager to arrange widgets in a top-down layout or side by side.
      Use the fill, expand, and side options of pack geometry manager to control how widgets arranged. '''

#1a

prnt = tk.Tk()
prnt.title("pack comands")
prnt.geometry("400x300")
prnt.resizable(False, False)

frme = tk.Frame(prnt, bg = "white")
chld=list([])
fInt_chld(10)

prnt.protocol("WM_DELETE_WINDOW", fPrnt_close)
tk.Button(frme, text = "sample 1", command = lambda : fSmpl_1(0))\
.grid(row = 0, column = 0, pady = 5)

tk.Button(frme, text = "sample 2", command = lambda: fSmpl_2(1))\
.grid(row = 0, column = 1, pady = 5)

tk.Button(frme, text = "sample 3", command = lambda: fSmpl_3(2))\
.grid(row = 0, column = 2, pady = 5)

tk.Button(frme, text = "sample 4", command = lambda: fSmpl_4(3))\
.grid(row = 0, column = 3, pady = 5)

tk.Button(frme, text = "sample 5", command = lambda: fSmpl_5(4))\
.grid(row = 1, column = 0, pady = 5, columnspan = 4, sticky = tk.N )


frme.pack(expand = True)

prnt.mainloop()

