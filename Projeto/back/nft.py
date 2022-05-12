import cv2 as cv
import numpy as np
import random as rd

img1 = cv.imread("caramelo.jpg")

img2 = cv.imread("chapeu.jpg")
img3 = cv.imread("flor.jpg")

# corte1 = img2[0:100, 0:200]

img2 = cv.resize(img2, dsize=(275, 183), interpolation=cv.INTER_CUBIC)
img3 = cv.resize(img3, dsize=(275, 183), interpolation=cv.INTER_CUBIC)

compisicao = cv.bitwise_and(img1, img2)

itens = [img2, img3]

print ("Altura (height): %d pixels" % (img1.shape[0]))
print ("Largura (width): %d pixels" % (img1.shape[1]))
print ("Canais (channels): %d"      % (img1.shape[2]))
print("")
print ("Altura (height): %d pixels" % (img3.shape[0]))
print ("Largura (width): %d pixels" % (img3.shape[1]))
print ("Canais (channels): %d"      % (img3.shape[2]))


def randomico(itens):
    print()
    imgnovornd = cv.add(img1, rd.choice(itens))


randomico(itens)
imgnovo = cv.add(img1, img2, img3)

#cv.namedWindow("NFT")

cv.imshow("NFT", imgnovo)
cv.waitKey()

for i in range(0, 100):
    cv.imwrite(f"imgs/caramelo#{i}.jpg", imgnovo)
