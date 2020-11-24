from tkinter import *
import random

root=Tk()
root.title('Number Guessing Game')
root.geometry('400x400+50+50')

class NumberGuessing:
    num1=IntVar()
    num2=IntVar()
    guessedNumber=IntVar()   #it stores values
    value = None

    def check(self):
        if self.num1.get()==0 or self.num2.get()==0 or self.guessedNumber.get()==0:
            self.ResultLabel.configure(text='Please input all fields')
        else:
            self.value=random.randint(self.num1.get(),self.num2.get()) #it generates a random number
            if self.guessedNumber.get()==self.value:
                self.ResultLabel.configure(text='Wow you are right')
            else:
                self.ResultLabel.configure(text=f'Oops number is {self.value}')



    def __init__(self):
        
        #creating entry boxes
        self.lfont=('Algerian',16)

        self.Label1=Label(root, text='From',font=self.lfont,foreground='red')
        self.Label1.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.entry1=Entry(root, textvariable=self.num1,font=self.lfont,foreground='blue')
        self.entry1.grid(row=0,column=1,padx=5,pady=5)

        self.Label2=Label(root, text='To',font=self.lfont,foreground='red')
        self.Label2.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.entry2=Entry(root, textvariable=self.num2,font=self.lfont,foreground='blue')
        self.entry2.grid(row=1,column=1,padx=5,pady=5)

        self.Label3=Label(root, text='Guess any Number',font=self.lfont,foreground='darkviolet')
        self.Label3.grid(row=2,columnspan=2,pady=10)

        self.entry3=Entry(root, textvariable=self.guessedNumber,font=self.lfont,foreground='darkorchid')
        self.entry3.grid(row=3,columnspan=2,pady=10)

        self.btn = Button(root,text="Check",font=self.lfont,foreground='darkviolet',command=self.check)
        self.btn.grid(row=4,columnspan=2,pady=10)

        self.ResultLabel = Label(root,text='Result',font=self.lfont,foreground='darkorchid')
        self.ResultLabel.grid(row=5,columnspan=2,pady=10)

        self.ResultLabel = Label(root,text='@The Code Scholar',font=self.lfont,foreground='black')
        self.ResultLabel.grid(row=6,columnspan=2,pady=10)

        self.ResultLabel = Label(root,text='Please share your valuable feedback.',font=('Arial',12),foreground='black')
        self.ResultLabel.grid(row=7,columnspan=2,pady=5)


 



        root.mainloop()

a=NumberGuessing()
