import PIL
print("PIL version ", PIL.__version__)
from PIL import Image

import numpy
import math
import random

import tkinter as tk
from tkinter import filedialog

ecran = tk.Tk()
ecran.withdraw()

fichierImage = filedialog.askopenfilename(initialdir = "./desktop/",title = "Choisir un fichier image", filetypes = (("fichiers jpeg","*.jpg"),("fichiers jpeg","*.jpeg"),("all files","*.*")))
if not fichierImage:
    exit()

import os
fichier = os.path.basename(fichierImage)
path = os.path.dirname(fichierImage)
nomImage = os.path.splitext(fichier)[0]
#print(nomImage)
ext = os.path.splitext(fichier)[1]
#print(ext)

img = Image.open(path + "/" + nomImage + ext)
print(img.format, img.size, img.mode)
largeur,hauteur = img.size

#Variable d'ajustement de la taille des pixels
tailleNouveauPixel = 100

#Calcul du nombre de pixel pour couvrir la largeur et la hauteur
nbNouveauPixelLargeur = math.floor(largeur / tailleNouveauPixel)
nbNouveauPixelHauteur = math.floor(hauteur / tailleNouveauPixel)

#Calcul de la nouvelle largeur et de la nouvelle hauteur qui sont des multiples du nombre de pixel
nouvelleLargeur = nbNouveauPixelLargeur*tailleNouveauPixel
nouvelleHauteur = nbNouveauPixelHauteur*tailleNouveauPixel
print("La nouvelle largeur de l'image est " + str(nouvelleLargeur))
print("La nouvelle hauteur de l'image est " + str(nouvelleHauteur))

#Calcul du nombre de pixel entre les nouvelles largeur/hauteur et les largeur/hauteur de l'image initiale
ecartLargeur = largeur - nouvelleLargeur
ecartHauteur = hauteur - nouvelleHauteur
print("l'écart en largeur est de " + str(ecartLargeur) + " pixels")
print("l'écart en hauteur est de " + str(ecartHauteur) + " pixels")

#Ajustement de la largeur de l'image pour avoir un nombre rond de nouveaux pixels
if largeur % tailleNouveauPixel != 0 : #Pour savoir si un ajustement de la taille est nécessaire ou non
    if ecartLargeur % 2 == 0 :
       left = ecartLargeur / 2
       right = largeur - ecartLargeur / 2
    else: 
       left = math.floor(ecartLargeur / 2)
       right = largeur - math.ceil(ecartLargeur / 2)
else:
    left = 0
    right = largeur

#Ajustement de la hauteur de l'image pour avoir un nombre rond de nouveaux pixels
if hauteur % tailleNouveauPixel != 0 : 
    if ecartHauteur % 2 == 0 : 
        top = ecartHauteur / 2
        down = hauteur - ecartHauteur/2
    else:
        top = math.floor(ecartHauteur/2)
        down = hauteur - math.ceil(ecartHauteur/2)
else : 
    top = 0
    down = hauteur

area = (left, top, right, down)
nouvelleImage = img.crop(area)
#nouvelleImage.show()

for i in range(nbNouveauPixelLargeur) :
    for j in range(nbNouveauPixelHauteur) :
        r = 0
        g = 0
        b = 0
        for k in range(tailleNouveauPixel) :
            for l in range (tailleNouveauPixel) :
                pixel = img.getpixel((k+i*tailleNouveauPixel,l+j*tailleNouveauPixel))
                r = r + pixel[0]
                g = g + pixel[1]
                b = b + pixel[2]
        r = round(r / (tailleNouveauPixel*tailleNouveauPixel))
        g = round(g / (tailleNouveauPixel*tailleNouveauPixel))
        b = round(b / (tailleNouveauPixel*tailleNouveauPixel))
        for k in range(tailleNouveauPixel) :
            for l in range(tailleNouveauPixel):
                nouvelleImage.putpixel((k+i*tailleNouveauPixel,l+j*tailleNouveauPixel), (int(r),int(g),int(b)))

nouvelleImage.show()




