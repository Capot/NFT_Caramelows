import cv2 as cv
import numpy as np
import random as rd

chapeu = [cv.imread("vazio.png"), cv.imread("chapeu/chapeu1.jpg"), cv.imread("chapeu/chapeu2.jpg")]
flor = [cv.imread("vazio.png"), cv.imread("flor/flor1.jpg"), cv.imread("flor/flor2.jpg")]

chapeuDimensionado = []
florDimensioando = []


for x in chapeu:
    x = cv.resize(x, dsize=(300, 300))
    chapeuDimensionado.append(x)
#chapeuDimensionado.insert(0, False)


for y in flor:
    y = cv.resize(y, dsize=(200, 200))
    florDimensioando.append(y)
#florDimensioando.insert(0, False)


class NFT:

    def __init__(self, i):
        self.imgBase = cv.imread("frita.jpeg")

        self.chapeu = rd.choice(chapeuDimensionado)
        self.flor = rd.choice(florDimensioando)

        self.elementos()

    def elementos(self):


            self.comp = self.composicao(self.imgBase, self.chapeu, 110, 90)
            cv.imwrite(f"imgs/caramelo#{i}.jpg", self.comp)


            self.comp = self.composicao(self.comp, self.flor, 450, 400)
            cv.imwrite(f"imgs/caramelo#{i}.jpg", self.comp)

    def composicao(self, fundo, frente, pos_H, pos_W):
        # pega altura e largura das imagens
        fundoH, fundoW, _ = fundo.shape
        frenteH, fundoW, _ = frente.shape

        # sobraH, sobraW, = fundoH - frenteH, fundoW - frenteH

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


for i in range(0, 10):
    NFT(i)
    # cv.imshow("NFT", elemento)
    # cv.waitKey()
    pass