from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image as image

root = Tk()
root.geometry("400x500")



def openpic():
    root.filename = filedialog.askopenfilename(title="select", filetypes=(("png files", "*.png"), ("all", "*.*")))
    global picture
    pic = image.open(root.filename)
    resized = pic.resize((400, 450), image.ANTIALIAS)
    picture = ImageTk.PhotoImage(resized)
    lab = Label(frame, image=picture)
    lab.pack()


open = Button(root, text="open", padx=40, pady=10, command=openpic)
frame = Frame(root, width=400, height=450)

frame.pack()
open.pack()

root.mainloop()