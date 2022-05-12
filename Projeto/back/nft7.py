import cv2 as cv
import numpy as np
import random as rd
import os, sys
import time

NFTlista = []

chapeu = []
flor = []

# Lê alegorias e armazena endereço em lista
pasta1 = "chapeu"
dir1 = os.listdir(pasta1)

for arquivos1 in dir1:
    chapeu.append(pasta1 + "/" + arquivos1)

pasta2 = "flor"
dir2 = os.listdir(pasta2)

for arquivos2 in dir2:
    flor.append(pasta2 + "/" + arquivos2)


class NFT:

    def __init__(self, i):
        self.nft = np.array([])
        self.imgBase = cv.imread("frita.jpeg")

        self.chapeu = rd.choice(chapeu)
        self.flor = rd.choice(flor)

        self.nft = ([self.chapeu] + [self.flor])

        # print(self.nft[1])
        # print(self.nft)

        # self.elementos(self.nfts)

    def elementos(self, elementosNft):
        #print(elementosNft[0:])
        self.chapeu = cv.imread(elementosNft[0])
        self.chapeu = cv.resize(self.chapeu, dsize=(300, 300))

        self.comp = self.composicao(self.imgBase, self.chapeu, 110, 90)
        cv.imwrite(f"imgs/caramelo#{i}.jpg", self.comp)

        self.flor = cv.imread(elementosNft[1])
        self.flor = cv.resize(self.flor, dsize=(200, 200))

        self.comp = self.composicao(self.comp, self.flor, 450, 400)
        cv.imwrite(f"imgs/caramelo#{i}.jpg", self.comp)


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


def contaNFTs(listaObjetos):
    for nft in listaObjetos:
        print(nft.nft)

i = 0
NFTs = NFT(0)
# print(NFTs.nft)
NFTlista.append(NFTs)


while len(NFTlista) < 9:

    NFTs = NFT(i+1)
    # NFTlista.append(NFTs)

    print("NFT na lista {}: {}" .format(i, NFTlista[i].nft))
    print("NFT gerado: {} " .format(NFTs.nft))
    print("Lista: {}" .format(len(NFTlista)))
    contaNFTs(NFTlista)
    print("------------------------------------")

    time.sleep(10)

    for x in NFTlista:
        if x.nft != NFTs.nft:
            NFTlista.append(NFTs)
            print("Adiciona NFT na Lista")
            # print(x.nft)
            # time.sleep(5)
            break

        else:
            print("igual")
            # print(x.nft)
            # time.sleep(5)
            break


print("------------------ FIM ------------------")
contaNFTs(NFTlista)
# print(NFTlista)
print(len(NFTlista))