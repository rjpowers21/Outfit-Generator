from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
import random

class WardrobeApp:

    def __init__(self, root):
        #create window
        self.root = root
        self.root.geometry('938x715')
        self.root.resizable(False, False)

        self.defineImages()
        self.createLabels()
        self.createButtons()

        #store the pictures in the 'tops' folder in a variable. do the same for the 'bottom' folder
        self.topPics = [str("tops/") + file for file in os.listdir("tops/") if not file.startswith('.')]
        self.bottomPics = [str("bottoms/") + file for file in os.listdir("bottoms/") if not file.startswith('.')]


        #save single top/bottom
        self.topPicPath = self.topPics[0]
        self.bottomPicPath = self.bottomPics[0]

        #create and resize top and bottom images
        self.topPicLabel = self.resizeClothes(self.topPicPath)
        self.bottomPicLabel = self.resizeClothes(self.bottomPicPath)

        #place top and bottom images on screen
        self.topPicLabel.place(x=360, y=40)
        self.bottomPicLabel.place(x=365, y=390)

    def defineImages(self):
        self.borderPic = PhotoImage(file = 'buttons/window.png')
        self.rewindPic = PhotoImage(file = 'buttons/rewind.png')
        self.rewindPic2 = PhotoImage(file = 'buttons/rewindClick.png')

        self.playPic = PhotoImage(file = 'buttons/play.png')

        self.forwardPic = PhotoImage(file = 'buttons/foward.png')
        self.forwardPic2 = PhotoImage(file = 'buttons/fowardClick.png')


        self.dressMePic = PhotoImage(file = 'buttons/dress.png')
        self.dressMePic2 = PhotoImage(file = 'buttons/clicked.png')
        self.backgroundPic = PhotoImage(file = 'buttons/print.png')

    def createLabels(self):
        #create Labels self.borderPic
        self.window1_label = Label(image=self.borderPic)
        self.window1_label.place(x=240, y=10)

        self.rewind_label = Label(image=self.rewindPic)
        self.rewind_label.place(x=240, y=292)

        self.play_label = Label(image=self.playPic)
        self.play_label.place(x=389, y=292)

        self.foward_label = Label(image=self.forwardPic)
        self.foward_label.place(x=544, y=292)

        self.rewind_label2 = Label(image=self.rewindPic)
        self.rewind_label2.place(x=240, y=640)

        self.play_label2 = Label(image=self.playPic)
        self.play_label2.place(x=392, y=640)

        self.foward_label2 = Label(image=self.forwardPic)
        self.foward_label2.place(x=544, y=660)

        self.window2_label = Label(image=self.borderPic)
        self.window2_label.place(x=240, y=360)

        self.dress_label1 = Label(image=self.dressMePic)
        self.dress_label1.place(x=0, y=605)

        self.dress_label2 = Label(image=self.dressMePic)
        self.dress_label2.place(x=697, y=605)

        self.print_label1 = Label(image=self.backgroundPic)
        self.print_label1.place(x=0, y=0)

        self.print_label2 = Label(image=self.backgroundPic)
        self.print_label2.place(x=694, y=0)

        #place labels
        self.window1_label.image = self.borderPic
        self.rewind_label.image = self.rewindPic
        self.play_label.image = self.playPic
        self.foward_label.image = self.forwardPic
        self.dress_label1.image = self.dressMePic
        self.print_label1.image = self.backgroundPic

    def createButtons(self):
        self.top_prev_button = tk.Button(self.root, image= self.rewindPic, command=self.getNextTop)
        self.top_prev_button.place(x=240, y=292)

        self.top_next_button = tk.Button(self.root, image=self.forwardPic, command=self.getPrevTop)
        self.top_next_button.place(x=544, y=292)

        self.bottom_prev_button = tk.Button(self.root, image=self.rewindPic, command=self.getNextBttm)
        self.bottom_prev_button.place(x=240, y=640)

        self.bottom_next_button = tk.Button(self.root, image=self.forwardPic, command=self.getPrevBttm)
        self.bottom_next_button.place(x=544, y=640)

        self.create_outfit_button = tk.Button(self.root, image=self.dressMePic, command=self.createOutfit)
        self.create_outfit_button.place(x=0, y=605)

    #resizes clothing image to fit screen
    def resizeClothes(self, path):
        file = Image.open(path)
        resized = file.resize((220, 220), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(resized)
        label = tk.Label(self.root, image=pic, anchor=tk.CENTER)
        #weird tkinter quirk
        label.image = pic
        return label

        #general fn that will allow us to move front and back
    def getNextPiece(self, currentImage, category, goForward = True):

        #if we know where the curr item index is in a category, then we find the pic before/after it

        #get first and last index
        currentIndex = category.index(currentImage)
        finalIndex = len(category)-1

        #define the next index depending on the current index and direction
        nextIndex = 0

        if goForward and currentIndex == finalIndex:
            #if the current index is the end, the next index is the first
            nextIndex = 0
        elif not goForward and currentIndex == 0:
            #if we are at the first index and we are moving backwards, the next index is the last
            nextIndex = finalIndex
        else:
            #increment the next index normally if we are not at one of the edge cases
            goForward = 1 if goForward else -1
            nextIndex = currentIndex + goForward

        #get next image
        nextImage = category[nextIndex]

        #reset and update the image based on the nextImage path
        if currentImage in self.topPics:
            label = self.topPicLabel
            self.topPicPath = nextImage
        elif currentImage in self.bottomPics:
            label = self.bottomPicLabel
            self.bottomPicPath = nextImage

        #use update function to change image
        self.updatePic(nextImage, label)

    def getNextTop(self):
        self.getNextPiece(self.topPicPath, self.topPics)
        self.topPrevPressed()

    def getPrevTop(self):
        self.getNextPiece(self.topPicPath, self.topPics, goForward=False)
        self.topNextPressed()

    def getNextBttm(self):
        self.getNextPiece(self.bottomPicPath, self.bottomPics)
        self.bottomPrevPressed()

    def getPrevBttm(self):
        self.getNextPiece(self.bottomPicPath, self.bottomPics, goForward=False)
        self.bottomNextPressed()

    def updatePic(self, newPath, label):
        #create picture using the given path
        file = Image.open(newPath)
        resized = file.resize((220, 220), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(resized)

        #use the label to update the picture
        label.configure(image=pic)
        label.image = pic

    def createOutfit(self):

        #randomly select a top and bottom
        topIndex = random.randint(0,len(self.topPics) - 1)
        bttmIndex = random.randint(0,len(self.bottomPics) - 1)

        #update image using selected images
        self.updatePic(self.topPics[topIndex], self.topPicLabel)
        self.updatePic(self.bottomPics[bttmIndex], self.bottomPicLabel)

        #change color of button
        self.outfitPressed()

    #helper functions to change color of Buttons when pressed

    def outfitPressed(self):
        self.create_outfit_button.config(image = self.dressMePic2)
        self.create_outfit_button.after(200,self.returnOutfit)

    def returnOutfit(self):
        self.create_outfit_button.config(image=self.dressMePic)

    def topPrevPressed(self):
        self.top_prev_button.config(image = self.rewindPic2)
        self.top_prev_button.after(200,self.returntopPrev)

    def returntopPrev(self):
        self.top_prev_button.config(image=self.rewindPic)

    def topNextPressed(self):
        self.top_next_button.config(image = self.forwardPic2)
        self.top_next_button.after(200,self.returntopNext)

    def returntopNext(self):
        self.top_next_button.config(image=self.forwardPic)

    def bottomPrevPressed(self):
        self.bottom_prev_button.config(image = self.rewindPic2)
        self.bottom_prev_button.after(200,self.returnbottomPrev)

    def returnbottomPrev(self):
        self.bottom_prev_button.config(image=self.rewindPic)

    def bottomNextPressed(self):
        self.bottom_next_button.config(image = self.forwardPic2)
        self.bottom_next_button.after(200,self.returnbottomNext)

    def returnbottomNext(self):
        self.bottom_next_button.config(image=self.forwardPic)

if __name__ == '__main__':
    root = Tk()
    app = WardrobeApp(root)

    root.mainloop()
