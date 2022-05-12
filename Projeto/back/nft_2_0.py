import cv2 as cv
import numpy as np
import random as rd
import os, sys
import time

NFTlista = []

fundo = []
coleira = []
oculos = []
cigarro = []
roupa = []
chapeu = []


# Lê alegorias e armazena endereço em lista
pasta7 = "imgs/7chapeu"
dir7 = os.listdir(pasta7)

for arquivos7 in dir7:
    chapeu.append(pasta7 + "/" + arquivos7)

########################################################################

pasta1 = "imgs/1fundo"
dir1 = os.listdir(pasta1)

for arquivos1 in dir1:
    fundo.append(pasta1 + "/" + arquivos1)

########################################################################

pasta3 = "imgs/3coleira"
dir3 = os.listdir(pasta3)

for arquivos3 in dir3:
    coleira.append(pasta3 + "/" + arquivos3)

########################################################################

pasta4 = "imgs/4oculos"
dir4 = os.listdir(pasta4)

for arquivos4 in dir4:
    oculos.append(pasta4 + "/" + arquivos4)

#########################################################################

pasta5 = "imgs/5cigarro"
dir5 = os.listdir(pasta5)

for arquivos5 in dir5:
    cigarro.append(pasta5 + "/" + arquivos5)

##########################################################################

pasta6 = "imgs/6roupa"
dir6 = os.listdir(pasta6)

for arquivos6 in dir6:
    roupa.append(pasta6 + "/" + arquivos6)


########################################################
########################################################


class NFT:

    def __init__(self, i):
        self.nft = np.array([])
        self.imgBase = cv.imread("imgs/2imgBase/frida.png")

        self.fundo = rd.choice(fundo)
        self.coleira = rd.choice(coleira)
        self.oculos = rd.choice(oculos)
        self.cigarro = rd.choice(cigarro)
        self.roupa = rd.choice(roupa)
        self.chapeu = rd.choice(chapeu)

        self.nft = (
                [self.fundo] +
                [self.coleira] +
                [self.oculos] +
                [self.cigarro] +
                [self.roupa] +
                [self.chapeu])


    def elementos(self, elementosNft, i):
        #print(elementosNft[0:])

        self.fundo = cv.imread(elementosNft[0])
        self.comp = self.composicao(self.imgBase, self.fundo, 0, 0)
        cv.imwrite(f"imgs/NFT/caramelo#{i}.jpg", self.comp)

        self.coleira = cv.imread(elementosNft[1])
        self.comp = self.composicao(self.comp, self.coleira, 0, 0)
        cv.imwrite(f"imgs/NFT/caramelo#{i}.jpg", self.comp)

        self.oculos = cv.imread(elementosNft[2])
        self.comp = self.composicao(self.comp, self.oculos, 0, 0)
        cv.imwrite(f"imgs/NFT/caramelo#{i}.jpg", self.comp)

        self.cigarro = cv.imread(elementosNft[3])
        self.comp = self.composicao(self.comp, self.cigarro, 0, 0)
        cv.imwrite(f"imgs/NFT/caramelo#{i}.jpg", self.comp)

        self.roupa = cv.imread(elementosNft[4])
        self.comp = self.composicao(self.comp, self.roupa, 0, 0)
        cv.imwrite(f"imgs/NFT/caramelo#{i}.jpg", self.comp)

        self.chapeu = cv.imread(elementosNft[5])
        self.comp = self.composicao(self.comp, self.chapeu, 0, 0)
        cv.imwrite(f"imgs/NFT/caramelo#{i}.jpg", self.comp)

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

########################################################
########################################################

def contaNFTs(listaObjetos):
    for nft in listaObjetos:
        print(nft.nft)


i = 0

# Primeiro NFT gerado, não tornar a lista inicial vazia
NFTs = NFT(0)
NFTlista.append(NFTs)

# Gera lista de objetos com a matriz dos NFTs
while len(NFTlista) < 100:
    verificaIgualdade = 0
    NFTs = NFT(i+1)

    # print("NFT na lista {}: {}" .format(i, NFTlista[i].nft))
    # print("NFT gerado: {} " .format(NFTs.nft))
    # print("Lista: {}" .format(len(NFTlista)))
    # contaNFTs(NFTlista)
    # print("------------------------------------")

    for x in NFTlista:
        if x.nft == NFTs.nft:
            verificaIgualdade = verificaIgualdade + 1
            break

    if verificaIgualdade == 0:
        NFTlista.append(NFTs)

print("------------------ FIM ------------------")
contaNFTs(NFTlista)
# print(NFTlista)
print(len(NFTlista))

# Gera Imagens NFTs
numeracao = 0
for geraNFT in NFTlista:
    print(geraNFT.nft)

    # Envia elementos de cada objeto
    geraNFT.elementos(geraNFT.nft, numeracao)
    numeracao = numeracao + 1
    # time.sleep(5)