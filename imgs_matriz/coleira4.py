import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/3coleira/coleira4.png'


class Coleira4:

    def __init__(self, x, y):

        branco = 255

        coleira_r = 250
        coleira_g = 128
        coleira_b = 114

        coleirafraco_r = 255
        coleirafraco_g = 160
        coleirafraco_b = 122

        def geraPixels(matriz,
                       coleira,
                       coleirafraco):

            matriz[0:22, 0:60] = branco

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

            matriz[30:50, 0:60] = branco

            return matriz


        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       coleira_r,
                       coleirafraco_r)

        g = geraPixels(g,
                       coleira_g,
                       coleirafraco_g)

        b = geraPixels(b,
                       coleira_b,
                       coleirafraco_b)


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y, ))
        plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches=0)

        # plt.show()


# coleira = Coleira4(5 ,4)