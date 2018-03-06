import numpy
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image
from math import cos, sin

def getGrayColor(rgb):
    return rgb[0]

def setGrayColor(color):
    return [color,color,color];

img = Image.open('Lena.png')
img = numpy.asarray(img)

# copy list not reference
thr = deepcopy(img)


count = 0 
sum = 0

for i in range(len(img)):
    for j in range(len(img[i])):
        count = count + 1
        sum += getGrayColor(img[i][j])
k = sum / count
print(k)

for i in range(len(img)):
    for j in range(len(img[i])):
        color = getGrayColor(img[i][j])
        if(color < k):
            thr[i][j] = setGrayColor(0) 
        elif(color >= k):
            thr[i][j] = setGrayColor(255)


plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(thr)


plt.show()
