import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/3coleira/coleira1.png'


class Coleira1:

    def __init__(self, x, y):
        branco = 255

        coleira_r = 139
        coleira_g = 0
        coleira_b = 0

        coleirafraco_r = 178
        coleirafraco_g = 34
        coleirafraco_b = 34

        contorno_r = 139
        contorno_g = 69
        contorno_b = 19

        amarelo_r = 204
        amarelo_g = 119
        amarelo_b = 34

        amareloqueimado_r = 218
        amareloqueimado_g = 165
        amareloqueimado_b = 32

        sombrancelha_r = 237
        sombrancelha_g = 145
        sombrancelha_b = 33

        olho1_r = 224
        olho2_r = 210

        olho1_g = 225
        olho2_g = 105

        olho1_b = 225
        olho2_b = 30

        nariz_r = 0
        nariz_g = 0
        nariz_b = 0

        vermelho_r = 255
        vermelho_g = 0
        vermelho_b = 0

        sombra_r = 128
        sombra_g = 128
        sombra_b = 128

        sombraclara_r = 211
        sombraclara_g = 211
        sombraclara_b = 211

        def geraPixels(matriz,
                       contorno,
                       amarelo,
                       amareloqueimado,
                       sombrancelha,
                       olho1,
                       olho2,
                       nariz,
                       vermelho,
                       sombra,
                       sombraclara,
                       coleira,
                       coleirafraco):

            for i in range(0, 22):
                matriz[i, 0:60] = branco

            matriz[22, 0:24] = branco
            matriz[22, 24:26] = coleira
            matriz[22, 26:60] = branco

            matriz[23, 0:23] = branco
            matriz[23, 23:26] = coleira
            matriz[23, 26:60] = branco

            matriz[24, 0:23] = branco
            matriz[24, 23:24] = coleira
            matriz[24, 24:25] = coleirafraco
            matriz[24, 25:60] = branco

            matriz[25, 0:23] = branco
            matriz[25, 23:25] = coleira
            matriz[25, 25:60] = branco

            matriz[26, 0:22] = branco
            matriz[26, 22:25] = coleira
            matriz[26, 25:60] = branco

            matriz[27, 0:22] = branco
            matriz[27, 22:23] = coleira
            matriz[27, 23:24] = coleirafraco
            matriz[27, 24:60] = branco

            matriz[28, 0:21] = branco
            matriz[28, 21:24] = coleira
            matriz[28, 24:60] = branco

            matriz[29, 0:21] = branco
            matriz[29, 21:23] = coleira
            matriz[29, 23:60] = branco

            for i in range(30, 50):
                matriz[i, 0:60] = branco

            return matriz

        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       contorno_r,
                       amarelo_r,
                       amareloqueimado_r,
                       sombrancelha_r,
                       olho1_r,
                       olho2_r,
                       nariz_r,
                       vermelho_r,
                       sombra_r,
                       sombraclara_r,
                       coleira_r,
                       coleirafraco_r)

        g = geraPixels(g,
                       contorno_g,
                       amarelo_g,
                       amareloqueimado_g,
                       sombrancelha_g,
                       olho1_g,
                       olho2_g,
                       nariz_g,
                       vermelho_g,
                       sombra_g,
                       sombraclara_g,
                       coleira_g,
                       coleirafraco_g)

        b = geraPixels(b,
                       contorno_b,
                       amarelo_b,
                       amareloqueimado_b,
                       sombrancelha_b,
                       olho1_b,
                       olho2_b,
                       nariz_b,
                       vermelho_b,
                       sombra_b,
                       sombraclara_b,
                       coleira_b,
                       coleirafraco_b)

        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        img = plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches=0)
        # plt.show()


# coleira = coleira1()
