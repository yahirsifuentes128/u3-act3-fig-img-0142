import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2

# yahir sifuentes NC = 0142 
print("yahir sifuentes NC 0142")
print("UIII Act3 colocar puntos a una imagen en blanco y negro con va ")
mi_imagen = cv2.imread("pele.jpg")
plt.imshow(mi_imagen)
plt.title("pele y yahir sifuentes 0142")
plt.show()
print("+-+-+-+- puntos en la imagen +-+-+-+-")
plt.imshow(mi_imagen)
x = [ 100,100,300,340]
y = [ 100,400,500,300]
plt.scatter(x,y, s=20,c="red")
plt.show()

