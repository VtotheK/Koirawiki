import tkinter as tk
from tkinter import ttk
import os

class Mainwindow(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        
        self.bg_col="darkgrey"
        self.lbl_bg="white"
        
        self.window_layout()
        self.fci()
        self.rotu()
        self.rotukuva()
        self.rotukuvaus()

    def fcivalinta(self,eventobject):
        print(self.fcivalikko.get())

    def rotuvalinta(self,eventobject):
        print(self.rotuvalikko.get())

    
        
    def asetakuva(self):
        pass

    def window_layout(self):
        self.valikkoframe = tk.Frame(height=650,width=332,bg=self.bg_col,relief=tk.GROOVE)
        self.valikkoframe.grid(row=0,column=0,pady=50,padx=20)
        self.tietoframe = tk.Frame(height=650,width=658,bg=self.bg_col,relief=tk.GROOVE)
        self.tietoframe.grid(row=0,column=1,pady=50,padx=0)
        self.valikkoframe.grid_propagate(0)
        self.tietoframe.grid_propagate(0)
        otsikko = tk.Label(master=self.valikkoframe,
                text="KOIRAWIKI",
                relief=tk.SOLID,
                bg=self.lbl_bg,
                padx=10)
        otsikko.config(font=("Roman",38,"bold"))
        otsikko.place(relx=.5,rely=.05,anchor="center")

    def fci(self):
        fci_otsikko = tk.Label(master=self.valikkoframe,
                text="FCI-ryhmä",
                bg=self.bg_col)

        fci_otsikko.place(relx=.5,rely=.3,anchor="center")
        fci_otsikko.config(font=("Roman",14))

        self.fcivalikko = ttk.Combobox(master=self.valikkoframe,state="readonly",values=("kurwa","mac","spps"))
        self.fcivalikko.place(relx=.5, rely=.36,anchor="center")
        self.fcivalikko.bind("<<ComboboxSelected>>",self.fcivalinta)

    def rotu(self):
        rotu_otsikko = tk.Label(master=self.valikkoframe,
                text="Valitse rotu",
                bg=self.bg_col)
        rotu_otsikko.place(relx=.5,rely=.5,anchor="center")

        self.rotuvalikko = ttk.Combobox(master=self.valikkoframe,state="readonly",values=("doge1","doge2","doge3"))
        self.rotuvalikko.place(relx=.5,rely=.56,anchor="center")
        self.rotuvalikko.bind("<<ComboboxSelected>>",self.rotuvalinta)

    def rotukuva(self):
        self.canv = tk.Canvas(master=self.tietoframe,width=654, height=400)
        self.canv.grid(row=0,column=0)

    def rotukuvaus(self):
        rotu_alkupera           = tk.Label(master=self.tietoframe,text="Rodun alkuperä:",bg=self.bg_col)
        rotu_kayttotarkoitus    = tk.Label(master=self.tietoframe,text="Rodun alkuperäinen käyttötarkoitus:",bg=self.bg_col)
        sakakorkeus             = tk.Label(master=self.tietoframe,text="Säkäkorkeus:",bg=self.bg_col)
        paino                   = tk.Label(master=self.tietoframe,text="Paino:",bg=self.bg_col)

        rotu_alkupera.grid(row=1,column=0,sticky="w")
        rotu_kayttotarkoitus.grid(row=2,column=0,sticky="w")
        sakakorkeus.grid(row=3,column=0,sticky="w")
        paino.grid(row=4,column=0,sticky="w")
