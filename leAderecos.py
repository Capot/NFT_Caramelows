import os, sys


fundo = []
coleira = []
oculos = []
cigarro = []
roupa = []
chapeu = []
brinquedos = []


# Lê alegorias e armazena endereço em lista
pasta7 = "imgs_geradas/7chapeu"
dir7 = os.listdir(pasta7)

for arquivos7 in dir7:
    chapeu.append(pasta7 + "/" + arquivos7)

########################################################################

pasta1 = "imgs_geradas/1fundo"
dir1 = os.listdir(pasta1)

for arquivos1 in dir1:
    fundo.append(pasta1 + "/" + arquivos1)

########################################################################

pasta3 = "imgs_geradas/3coleira"
dir3 = os.listdir(pasta3)

for arquivos3 in dir3:
    coleira.append(pasta3 + "/" + arquivos3)

########################################################################

pasta4 = "imgs_geradas/4oculos"
dir4 = os.listdir(pasta4)

for arquivos4 in dir4:
    oculos.append(pasta4 + "/" + arquivos4)

#########################################################################

pasta5 = "imgs_geradas/5cigarro"
dir5 = os.listdir(pasta5)

for arquivos5 in dir5:
    cigarro.append(pasta5 + "/" + arquivos5)

##########################################################################

pasta6 = "imgs_geradas/6roupa"
dir6 = os.listdir(pasta6)

for arquivos6 in dir6:
    roupa.append(pasta6 + "/" + arquivos6)

###########################################################################

pasta8 = "imgs_geradas/8brinquedos"
dir8 = os.listdir(pasta8)

for arquivos8 in dir8:
    brinquedos.append(pasta8 + "/" + arquivos8)
