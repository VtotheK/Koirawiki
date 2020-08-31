import tkinter as tk
import json
from tkinter import ttk
import os

class Mainwindow(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        
        self.bg_col="darkgrey"
        self.lbl_bg="white"
        self.lbl_font = ("Roman",14)
        self.window_layout()
        self.fci()
        self.rotu()
        self.rotukuva()
        self.rotukuvaus()
        self.taytafcivalikko()
# HANNAN OSUUS ALKAA

        '''Funktio taytafcivalikko kutsutaan kun ohjelma käynnistetään ensimmäisen kerran.
Funktio fcivalinta kutsutaan aina kun fci alasvetovalikosta valitaan jokin arvo. 
Funktio rotuvalinta kutsutaan aina kun "valitse rotu" alasvetovalikosta valitaan jokin arvo.

JSON-tiedostojen rakenne:
    FCI-ryhmien json (yksi kappale). Yksi kenttä. Avain = "fci-ryhmät". Avaimelle arvoksi lista fci-ryhmistä
    
    Rotujen json tiedostot (esim 3 per fci-ryhmä): Viisi kenttää. Avaimet = "rodun_alkupera" "rodun_kayttotarkoitus" "sakakorkeus" "paino" "kuvaus". Avaimille arvoiksi
    koirarodulle sopivat tiedot

TAVOITE:
    Funktiossa taytavalikot luetaan koirarotujen json tiedostoista FCI-ryhmät, sekä sijoitetaan nämä arvot
    fci-alasvetovalikkoon käyttäjän valittavaksi. Kun käyttäjä valitsee fci-ryhmän, luetaan sen fci-ryhmän 
    kaikki rodut sekä sijoitetaan koirarodut "valitse rotu" alasvetovalikkoon. 
    
    Kannattaa aloittaa vain printtaamalla konsoliin ne fci-ryhmät ja koirarodut ennenkuin aletaan laittamaan
    niiä alasvetovalikkoihin.

OHJELMAN FLOW:
    Funktio taytafcivalikko:
    lisätään joko kovakoodatut fci-ryhmät, tai luetaan ryhät json tiedostosta -> lisätään ryhmät listaan --> lista lisätään alasvetovalikkooni -> valmis
    
    Funktio fcivalinta:
    luetaan käyttäjän valitseman fci-ryhmän kaikki koirarotu json-tiedostot -> lisätään koirarodut listaan -> lista lisätään alasvetovalikkoon -> valmis

    Funktio rotuvalinta:
    luetaan käyttäjän valitseman rodun json-tiedosto -> lisätään muuttujaan json-tiedostossa olevan kuvan polku -> kuva lisätään käyttöliittymään syöttämällä asetakuva-funktioon viime kohdassa mainittu muuttuja -> otetaan json-tiedostosta muut tiedot (rodun alkuperä, paino....) ja syötetään ne vastaavilla funktioilla oikeisiin tekstikenttiin -> valmis '''

    def taytafcivalikko(self):
        #poista pass komento
        #luetaan fci-ryhmä json
        #katsot netistä käskyn kuinka json tiedosto käännetään assosiaatiotauluksi (englanniksi dictionary) :)
        #lisäät fci valikot listaan
        #printataan lista komentoriville
        #kun tämä on tehty niin kirjoitetaan koodi millä lista lisätään alasvetovalikkoon
        pass
    
    def fcivalinta(self,eventobject):
        #tämä kutsutaan kun käyttäjä valitsee fci-ryhmän alasvetovalikosta
        #luetaan fci-ryhmän rotujen json tiedostot ja lisätään rotujen nimet listaan
        #printataan lista(komento jo valmiina)
        #kun tämä on tehty niin kirjoitetaan koodi millä lista lisätään alasvetovalikkoon
        print(self.fcivalikko.get())

    def rotuvalinta(self,eventobject):
        #tämä kutsutaan kun käyttäjä valitsee koirarodun alasvetovaliksota
        #luetaan rodun json tiedosto
        #otetaan tiedot assosiaatiotaulukosta, ja printataan komentoriville
        #kun tämä on tehty niin kirjoitetaan koodi millä kuva ja tiedot lisätään oikeisiin kenttiin
        print(self.rotuvalikko.get())

    def asetakuva(self,polku):
        #kuvan asetusta varten
        #katsotaan myöhemmin
        pass
# HANNAN OSUUS LOPPUU
#kaikki tästä alaspäin on käyttöliittymä koodia
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
        fci_otsikko.config(font=self.lbl_font)

        self.fcivalikko = ttk.Combobox(master=self.valikkoframe,state="readonly")
        self.fcivalikko.place(relx=.5, rely=.36,anchor="center")
        self.fcivalikko.bind("<<ComboboxSelected>>",self.fcivalinta)

    def rotu(self):
        rotu_otsikko = tk.Label(master=self.valikkoframe,
                text="Valitse rotu",
                bg=self.bg_col,
                font=self.lbl_font)
        rotu_otsikko.place(relx=.5,rely=.44,anchor="center")

        self.rotuvalikko = ttk.Combobox(master=self.valikkoframe,state="readonly")
        self.rotuvalikko.place(relx=.5,rely=.50,anchor="center")
        self.rotuvalikko.bind("<<ComboboxSelected>>",self.rotuvalinta)

    def rotukuva(self):
        self.canv = tk.Canvas(master=self.tietoframe,width=656, height=400)
        self.canv.grid(row=0,column=0,columnspan=25,rowspan=1)

    def rotukuvaus(self):
        lblfont = ("Helvetica",16)
        
        f_alkupera = tk.Frame(self.tietoframe,bg=self.bg_col)
        f_kayttotarkoitus = tk.Frame(self.tietoframe,bg=self.bg_col)
        f_sakakorkeus= tk.Frame(self.tietoframe,bg=self.bg_col)
        f_paino= tk.Frame(self.tietoframe,bg=self.bg_col)
        f_rotukuvaus = tk.Frame(self.tietoframe,bg=self.bg_col)
        
        f_alkupera.grid(column=0,row=1,sticky="nsew")
        f_sakakorkeus.grid(column=0,row=3,sticky="nsew")
        f_paino.grid(column=0,row=4,sticky="nsew")
        f_kayttotarkoitus.grid(column=0,row=2,sticky="nsew")
        f_rotukuvaus.grid(column=0,row=5,sticky="nwse")

        rotu_alkupera           = tk.Label(f_alkupera,text="Rodun alkuperä:",bg=self.bg_col,font=lblfont)
        rotu_kayttotarkoitus    = tk.Label(f_kayttotarkoitus,text="Rodun käyttötarkoitus:",bg=self.bg_col,font=lblfont)
        sakakorkeus             = tk.Label(f_sakakorkeus,text="Säkäkorkeus:",bg=self.bg_col,font=lblfont)
        paino                   = tk.Label(f_paino,text="Paino:",bg=self.bg_col,font=lblfont)
        kuvaus                  = tk.Label(f_rotukuvaus,text="Kuvaus",bg=self.bg_col,font=lblfont)

        json_alkupera           = tk.Label(f_alkupera,text="ITÄ-KESKI-MONGOLIA",bg=self.bg_col,font=lblfont)
        json_kayttotarkoitus    = tk.Label(f_kayttotarkoitus,text="Seurustelu/pulloharja",bg=self.bg_col,font=lblfont)
        json_sakakorkeus        = tk.Label(f_sakakorkeus,text="150-2500cm",bg=self.bg_col,font=lblfont)
        json_paino              = tk.Label(f_paino,text="5-1250kg",bg=self.bg_col,font=lblfont)
        json_rotukuvaus         = tk.Text(f_rotukuvaus,height=50,width=55,font=lblfont,bg=self.bg_col,state="disabled")

        rotu_alkupera.grid(row=1,column=0,sticky="w")
        rotu_kayttotarkoitus.grid(row=2,column=0,sticky="w")
        sakakorkeus.grid(row=3,column=0,sticky="w")
        paino.grid(row=4,column=0,sticky="w")
        kuvaus.grid(row=5,column=0,sticky="w")
        json_alkupera.grid(row=1,column=1,sticky="w")
        json_kayttotarkoitus.grid(row=2,column=1)
        json_sakakorkeus.grid(row=3,column=1,sticky="w")
        json_paino.grid(row=4,column=1,sticky="w")
        json_rotukuvaus.grid(row=6,column=0)
        json_rotukuvaus.config(state=tk.NORMAL)
        json_rotukuvaus.insert(tk.INSERT,"BLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLABLA")
        json_rotukuvaus.config(state=tk.DISABLED)
