import tkinter as tk
import os
from PIL import Image,ImageTk
from playsound import playsound
base_dir = os.getcwd()
images = os.listdir(base_dir+r"\Clues")
print(os.getcwd())
print(images)
prev = -1
def image():
    with open(r"C:\Users\User\AppData\Local\Project_9\code.txt") as file:
        code = file.readline().replace('\n','')
        global images
        global prev 
        if '{}.png'.format(code) in images and prev != code:
            print(code)
            photo = ImageTk.PhotoImage(Image.open(base_dir+r"\Clues\{}.png".format(code)))
            global pic
            pic.configure(image=photo)
            pic.image = photo
            #playsound(base_dir+'\Audio\{}.mp3'.format(code))
            prev = code
        file.close()
    root.after(1000,image)
    
def act1():
    
    photo = ImageTk.PhotoImage(Image.open(base_dir+r"\Clues\Act1.png"))
    global pic
    pic.configure(image=photo)
    pic.image = photo
    #playsound(base_dir+'\Audio\Act1.mp3')
    root.after(5000,image)
    

def act2():
    photo = ImageTk.PhotoImage(Image.open(base_dir+r"\Clues\Act2.png"))
    global pic
    pic.configure(image=photo)
    pic.image = photo
    #playsound(base_dir+'\Audio\Act2.mp3')
    root.after(5000,image)   
root = tk.Tk()
root.geometry('512x512')
label = tk.Label(root, text="Unlock Decoder")
label.pack()
##tb = tk.Entry(root, width="10")
##tb.pack()
button = tk.Button(root, text="Act 1", command=act1)
button.pack()
button1 = tk.Button(root, text="Act 2", command=act2)
button1.pack()
img = ImageTk.PhotoImage(Image.open(base_dir+r"\Clues\1.png"))
pic = tk.Label(root, image=img)
pic.pack()
image()
root.mainloop()



