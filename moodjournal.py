import pygame
pygame.init()
import simpleimage
from tkinter import*
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
root = Tk()
root.geometry("700x403")

bg = PhotoImage(file = "image (4).png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
pygame.mixer.music.load("comfy vibes.mp3") #Loading File Into Mixer
pygame.mixer.music.play(loops = -1) #Play music
l=Label(root, text="Rate your day from 1 to 4",fg="black", bg='#ffc5fb')
l.pack()
e= Entry(root, width=50, bg="#ffdafc",fg='grey')
e.pack()
e.insert(0, "(rating)")
l=Label(root, text="How was your day, explain a bit ?",fg="black", bg='#ffc5fb')
l.pack()
o= Entry(root, width=50, bg="#ffdafc",fg='grey')
o.pack()
o.insert(1, "(day)")



def rating():
    
    l=['','images/sad.jpg','images/neutral.jpg','images/happy.jpg','images/veryhappy.jpg']
    lemote=['','😢','😐','🙂','😆']
    #rating=int(input("Rate your day from 1 to 4 : \n"))
    #story=str(input("How was your day, explain a bit ? \n"))
    #USER INPUTS
    rating=int(e.get())
    story=str(o.get())
    img = Image.open(l[rating])
    I1 = ImageDraw.Draw(img)
    today = datetime.today()
    todayformat = str(today.strftime("%B %d, %Y %H:%M:%S")) #STORE CURRENT TIME
    myFont = ImageFont.truetype('Arial.ttf', 30)#text font settings
    Font2 = ImageFont.truetype('Arial.ttf', 20)
    I1.text((10, 7), todayformat, font=myFont, fill =(0,128,255))#store time as text in img
    I1.text((5, 40),story,font=Font2, fill =(255,150,160))#store your day in img
    img.show()
    img.save("mood/"+lemote[rating]+str(today.strftime("%d-%m-%Y-%H-%S"))+".jpg")#saves it in mood folder
    
myButton = Button(root, text="SUMBIT!" , command=rating, fg="#ff26e4", bg='#fcc529')
myButton.pack()
root.mainloop() 




#if __name__ == '__main__':
    #main()
