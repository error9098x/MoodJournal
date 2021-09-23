import pygame
import random
pygame.init()
import simpleimage
from tkinter import*
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
root = Tk()
root.title("MoodJournal")
root.iconbitmap(r'moodicon.ico')
root.geometry("700x403")
songs=["src/comfy vibes.mp3","src/a stormy night.mp3","src/hard to find words.mp3"]
randomstore=random.randrange(3) #choose random songs
randomsong=songs[randomstore]
images=["src/image (1).png","src/image (2).png","src/image (3).png"]
bg = PhotoImage(file =images[randomstore])
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
pygame.mixer.music.load(randomsong) #Loading File Into Mixer
pygame.mixer.music.play(loops = -1) #Play music
l=Label(root, text="Rate your day from 1 to 4",fg="black", bg='#ffc5fb')
l.pack()
rate= Entry(root, width=50, bg="#ffdafc",fg='grey')
rate.pack()
#e.insert(0, "(rating)")
label=Label(root, text="How was your day, explain a bit ?",fg="black", bg='#ffc5fb')
label.pack()
explain= Entry(root, width=50, bg="#ffdafc",fg='grey')
explain.pack()
#o.insert(1, "(day)")


def myclick():
    label=Label(root, text="Image succesfully stored in mood folder! 😆",fg="black", bg='#ffdafc')
    label.pack()
def rating():
    
    l=['','images/sad (2).jpg','images/neutral (2).jpg','images/happy (2).jpg','images/veryhappy (2).jpg']
    lemote=['','😢','😐','🙂','😆']
    #rating=int(input("Rate your day from 1 to 4 : \n"))
    #story=str(input("How was your day, explain a bit ? \n"))
    #USER INPUTS
    rating=int(rate.get())
    story=str(explain.get())
    img = Image.open(l[rating])
    I1 = ImageDraw.Draw(img)
    today = datetime.today()
    s=[]
    #USER INPUTS
    story=story.strip()
    slist=story.split()
    
    flist=[]
    for i in range(len(slist)//8+1):
        flist.append("")
    c=0
    j=0
    for i in range(len(slist)): #stores sentences in each indices in the list
        c+=1
        if c<=8:
           flist[j]+=slist[i]+' '
        if c==8:
            j+=1
            c=0   
    todayformat = str(today.strftime("%B %d, %Y %H:%M:%S")) #STORE CURRENT TIME
    myFont = ImageFont.truetype('src/Miglia.ttf', 30)#text font settings
    Font2 = ImageFont.truetype('src/Miglia.ttf', 20)
    I1.text((10, 465), todayformat, font=myFont, fill =('#7f82ff')) #store time as text in img
    for i in range(len(flist)):
        
        x=10
        y=40
        I1.text((x, y*i+10),flist[i],font=Font2, fill =('#7f82ff'))#store your day in img
    myclick()   
    img.show()
    img.save("mood/"+lemote[rating]+str(today.strftime("%d-%m-%Y-%H-%S"))+".jpg")#saves it in mood folder
   
myButton = Button(root, text="SUBMIT!" , command=rating, fg="#ff26e4", bg='#fcc529')


myButton.pack()
root.resizable(False, False) 
root.mainloop() 




#if __name__ == '__main__':
    #main()
