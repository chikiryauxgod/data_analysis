import matplotlib.pyplot as plt
import numpy as np
from scipy.datasets import face


def print_img(img):
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()

    
face_img = face() # default
print_img(face_img)

face_img = face(gray=True) # inverted 
face_img = face_img - 50
print_img(face_img)

crop_face = face(gray=True)
crop_face = crop_face[100:-100, 100:-100]
print_img(crop_face)


circle = face(gray=True)
sy, sx = circle.shape
y, x = np.ogrid[0:sy, 0:sx]
centerx, centery = (660, 300)
mask = (y- centery)**2 + (x - centerx)**2 >= 230**2
circle[mask] = 0
print_img(circle)