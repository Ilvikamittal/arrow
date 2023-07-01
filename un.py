from tkinter import*
from PIL import ImageTk,Image
root=Tk()

root.title("arrow")
root.geometry("500x500")
root.configure(background="green")

earth_img=ImageTk.PhotoImage(Image.open("earth.jpg"))
venus_img=ImageTk.PhotoImage(Image.open("venus.jpg"))
mercury_img=ImageTk.PhotoImage(Image.open("mercury.jpg"))

label_p=Label(root,text="planet")
label_p.place(relx=0.3,rely=0.1,anchor=CENTER)

planet_name=Label(root)
planet_name.place(relx=0.5,rely=0.4,anchor=CENTER)

planet_img=Label(root)
planet_img.place(relx=0.5,rely=0.5,anchor=CENTER)

planet_info=Label(root)
planet_info.place(relx=0.5,rely=0.9,anchor=CENTER)

def info1():
    print("Hi")
    
    

info=Button(root,text="show planet info",command=info1)
info.place(relx=0.5,rely=0.2,anchor=CENTER)



root.mainloop()