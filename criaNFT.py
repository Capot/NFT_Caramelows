import cv2 as cv
import numpy as np
import random as rd
import leAderecos as la

base = "imgs_geradas/2imgBase/caramelow.png"

NFTgerados = "NFTs/"
nome = "CARAMELOWS#"

class NFT:

    def __init__(self, i):
        self.nft = np.array([])
        self.imgBase = cv.imread(base)

        # random.choices(lista_nomes, cum_weights=[2, 5, 1, 8], k=10)

        self.fundo = rd.choice(la.fundo)
        self.coleira = rd.choice(la.coleira)
        self.oculos = rd.choices(la.oculos, weights=[8, 1, 1, 1, 1, 1, 1, 1], k=1)
        self.cigarro = rd.choice(la.cigarro)
        self.roupa = rd.choice(la.roupa)
        self.chapeu = rd.choice(la.chapeu)
        self.brinquedos = rd.choice(la.brinquedos)

        self.nft = (
                [self.fundo] +
                [self.coleira] +
                self.oculos +
                [self.cigarro] +
                [self.roupa] +
                [self.chapeu] +
                [self.brinquedos])


    def elementos(self, elementosNft, i):
        #print(elementosNft[0:])

        self.fundo = cv.imread(elementosNft[0])
        self.comp = self.composicao(self.fundo, self.imgBase , 0, 0)
        cv.imwrite(NFTgerados + nome + f"{i}.jpg", self.comp)

        self.coleira = cv.imread(elementosNft[1])
        self.comp = self.composicao(self.comp, self.coleira, 0, 0)
        cv.imwrite(NFTgerados + nome + f"{i}.jpg", self.comp)

        self.oculos = cv.imread(elementosNft[2])
        self.comp = self.composicao(self.comp, self.oculos, 0, 0)
        cv.imwrite(NFTgerados + nome + f"{i}.jpg", self.comp)

        self.cigarro = cv.imread(elementosNft[3])
        self.comp = self.composicao(self.comp, self.cigarro, 0, 0)
        cv.imwrite(NFTgerados + nome + f"{i}.jpg", self.comp)

        self.roupa = cv.imread(elementosNft[4])
        self.comp = self.composicao(self.comp, self.roupa, 0, 0)
        cv.imwrite(NFTgerados + nome + f"{i}.jpg", self.comp)

        self.chapeu = cv.imread(elementosNft[5])
        self.comp = self.composicao(self.comp, self.chapeu, 0, 0)
        cv.imwrite(NFTgerados + nome + f"{i}.jpg", self.comp)

        self.brinquedos = cv.imread(elementosNft[6])
        self.comp = self.composicao(self.comp, self.brinquedos, 0, 0)
        cv.imwrite(NFTgerados + nome + f"{i}.jpg", self.comp)

    def composicao(self, fundo, frente, pos_H, pos_W):
        # pega altura e largura das imagens
        fundoH, fundoW, _ = fundo.shape
        frenteH, fundoW, _ = frente.shape

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
