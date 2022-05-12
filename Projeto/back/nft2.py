import cv2 as cv
import numpy as np
import random as rd

imgBase = cv.imread("frita.jpeg")

img2 = cv.imread("chapeu/chapeu2.jpg")
img3 = cv.imread("flor/flor1.jpg")

img2 = cv.resize(img2, dsize=(300, 300), interpolation=cv.INTER_CUBIC)
img3 = cv.resize(img3, dsize=(200, 200), interpolation=cv.INTER_CUBIC)

itens = (img2, img3)


# print ("Altura (height): %d pixels" % (imgBase.shape[0]))
# print ("Largura (width): %d pixels" % (imgBase.shape[1]))
# print ("Canais (channels): %d" % (imgBase.shape[2]))
# print("")
# print ("Altura (height): %d pixels" % (img3.shape[0]))
# print ("Largura (width): %d pixels" % (img3.shape[1]))
# print ("Canais (channels): %d"      % (img3.shape[2]))

def composicao(fundo, frente, pos_H, pos_W):
    # pega altura e largura das imagens
    fundoH, fundoW, _ = fundo.shape
    frenteH, fundoW, _ = frente.shape

    sobraH, sobraW, = fundoH - frenteH, fundoW - frenteH

    # parte do cenário do fundo em que a imagem será adicionada
    crop = fundo[pos_H:frenteH + pos_H, pos_W:fundoW + pos_W]

    # Transformamos o foreground em imagem com tons de cinza e criamos uma máscara binária da mesma com a binarização (cv2.threshold)
    frentecinza = cv.cvtColor(frente, cv.COLOR_BGR2GRAY)
    ret, mascara = cv.threshold(frentecinza, 240, 255, cv.THRESH_BINARY)

    # Agora aplicamos uma operação de AND binário na imagem recortada 'crop'. No caso, realizar a operação binária entre a mesma imagem não terá efeito. Só que, com a inclusão da máscara no terceiro parâmetro, os pixels pretos de mascara serão ignorados e, portanto, ficarão escuros. Com isso temos a marcação em que vamos incluir o foreground posteriormente.
    backWithMask = cv.bitwise_and(crop, crop, mask=mascara)
    foreWithMask = cv.bitwise_not(mascara)
    foreWithMask = cv.bitwise_and(frente, frente, mask=foreWithMask)

    # Faremos a composição entre 'frente' e 'fundo', compondo o foreground na imagem extraída do background.
    combinedImage = cv.add(foreWithMask, backWithMask)

    # Adicionamos a imagem gerada no background final.
    copyImage = fundo.copy()
    copyImage[pos_H:frenteH + pos_H, pos_W:fundoW + pos_W] = combinedImage

    return copyImage


def randomico(itens):
    for i in range(0, 10):

            comp = composicao(imgBase, rd.choice(itens), 110, 90)
            cv.imwrite(f"imgs/caramelo#{i}.jpg", comp)

### teste de imagem ###
#randomico(itens)
comp=composicao(imgBase, img2, 110, 90)

cv.imshow("NFT", comp)
#cv.imshow("NFT", imgBase)
cv.waitKey()

