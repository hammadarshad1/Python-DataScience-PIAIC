import os
import numpy as np
from PIL import Image
import matplotlib.pylab as plt

rootDir = '.'
imagesList = []
for dirName, subDirList, fileList in os.walk(rootDir):
    print('Found directory: %s'%dirName)
    imagesList = imagesList+fileList
counter=0
for i in imagesList:
    if i.endswith('.jpg') or i.endswith('.jpeg'):
        im = plt.imread(i)
        image = Image.open(i)
        newImage = image.resize((200,200))
        newImage.save('new{}.jpg'.format(counter))
        counter+=1