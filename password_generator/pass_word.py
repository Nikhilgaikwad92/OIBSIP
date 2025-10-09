from tkinter import *
from tkinter import messagebox
from random import randint
from PIL import Image, ImageTk

root = Tk()
root.title('Random Password Generator')
root.geometry("500x300")

icon_image = Image.open(r"C:\Users\nikhi\Downloads\globe.png")
icon_tk = ImageTk.PhotoImage(icon_image)

root.iconphoto(True, icon_tk)

def new_rand():
    pw_entry.delete(0,END)
    
    pw_length = int(my_entry.get())
    my_password = ""
    for x in range(pw_length):
        
        my_password += chr(randint(33,126))
    pw_entry.insert(0,my_password)
        
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Welcome to Random password Generator App .",  "Copied Successfully To Clipboard")

lf = LabelFrame(root, text="How Many Characters Do You Want In Your Password?", font=("helvetica", 20))
lf.pack(pady=20)

my_entry = Entry(lf, font=("helvetica", 24))
my_entry.pack(pady=20,padx=20)

pw_entry = Entry(root, text="", font=("helvetica", 24),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Password", command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button = Button(my_frame,text="Copy To Clipboard",command=clipper)
clip_button.grid(row=0,column=1,padx=10)    

root.mainloop()