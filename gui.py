# Required Modules 
from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.title("Instagram Reel Downloader By Rochak Education")
root.minsize(600,500)
root.maxsize(600,500)
HEIGHT=500
WIDTH = 600
FONT = font.Font(family="Times New Roman",size ="18", weight="bold")
canvas = Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()


icon_image = PhotoImage(file= "2.png")
root.iconphoto(False, icon_image)

frame = Frame(root,bg="white")
frame.place(relheight=1,relwidth=1)

background_image = ImageTk.PhotoImage(Image.open(r"C:/Users/offic/Documents/Instagram Reel GUI/1.jpg"))
background_label = Label(frame,image=background_image)
background_label.place(relx=-0.25,relwidth=0.7,relheight=1)

label1 =Label(frame, text= "Download Reels in a click !",font=FONT,bd = 5,fg= "#0d1137",bg="white")
label1.place(relx = 0.48, rely = 0.1, relheight =0.1)

FONT = font.Font(family ="Times New Roman", size ="12", weight ="bold")
label2 = Label(frame, text = "Enter link address: ", font =FONT, bd =5, fg= "#e52165",bg="white")
label2.place(relx = 0.48, rely = 0.25, relheight =0.1)

entry = Entry(frame, font = FONT, fg = "#fbad50")
entry.place(relx = 0.48, rely = 0.35,relwidth=0.4, relheight = 0.05)

button1 = Button(root, text = "Download", font = FONT, bg = "pink", fg = "black", activeforeground = "pink", activebackground = "black",command=lambda:download(entry.get()))
button1.place(relx = 0.48,rely = 0.45,relwidth = 0.2, relheight = 0.06)

label2 = Label(frame, text = "Instructions: ", font =FONT, bd =5, fg= "#0d1137",bg="white")
label2.place(relx = 0.48, rely = 0.6, relheight =0.1)

FONT = font.Font(family ="Times New Roman", size ="10", weight ="bold")
TEXT="1.Only public account reels can be downloaded\n2.Enter the link address of reel from the Instagram\n3.This is not meant to be used for mischeif"
label2 = Label(frame, text = TEXT, font =FONT, bd =5, fg= "#cd486b",justify=LEFT,bg="white")
label2.place(relx = 0.48, rely = 0.7, relheight =0.1)



root.mainloop()