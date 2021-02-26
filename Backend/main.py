from overseerr import overfindid, overnewuser
from jellyfin import embgetuserid, embnewuser
import csv
import tkinter as tk

window = tk.Tk()
maintitle = tk.Label(text="Flex - Media Server Management")

maintitle.pack()
window.mainloop()


todo = input("1 - New user")

if todo == "1":
    name=input("enter name")
    email = input("enter email")
    password = input("enter password")
    print(embnewuser(name,password))
    print(overnewuser(name, email, password))



