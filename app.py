import mainwindow
import tkinter as tk

if(__name__=="__main__"):
    width = 1050
    height = 732
    x = 250
    y = 250
    root = tk.Tk()
    root.geometry("{}x{}+{}+{}".format(width,height,x,y))
    root.title("HAMK koirawiki")
    root.configure(bg="grey")
    #root.resizable(False,False)
    mainwindow.Mainwindow(root)
    root.mainloop()
