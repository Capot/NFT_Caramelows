import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/4oculos/ciclope2.png'

class OculosCiclope2:

    def __init__(self, x, y):
        branco = 255

        ciclopearmacao1_r = 220
        ciclopearmacao1_g = 220
        ciclopearmacao1_b = 220

        ciclopearmacao2_r = 200
        ciclopearmacao2_g = 200
        ciclopearmacao2_b = 200

        ciclopelente1_r = 34
        ciclopelente1_g = 139
        ciclopelente1_b = 34

        ciclopelente2_r = 50
        ciclopelente2_g = 205
        ciclopelente2_b = 50

        def geraPixels(matriz,
                       ciclopearmacao1,
                       ciclopearmacao2,
                       ciclopelente1,
                       ciclopelente2):

            matriz[0:15, 0:60] = branco

            matriz[15, 0:12] = branco
            matriz[15, 12:24] = ciclopearmacao2
            matriz[15, 24:60] = branco

            matriz[16, 0:11] = branco
            matriz[16, 11:13] = ciclopearmacao2
            matriz[16, 13:24] = ciclopearmacao1
            matriz[16, 24:25] = ciclopearmacao2
            matriz[16, 25:60] = branco

            matriz[17, 0:10] = branco
            matriz[17, 10:12] = ciclopearmacao2
            matriz[17, 12:26] = ciclopearmacao1
            matriz[17, 13:14] = ciclopelente2
            matriz[17, 14:23] = ciclopelente1
            matriz[17, 23:26] = ciclopearmacao1
            matriz[17, 26:60] = branco

            matriz[18, 0:10] = branco
            matriz[18, 10:11] = ciclopearmacao2
            matriz[18, 11:13] = ciclopearmacao1
            matriz[18, 13:14] = ciclopelente1
            matriz[18, 14:16] = ciclopelente2
            matriz[18, 16:23] = ciclopelente1
            matriz[18, 23:26] = ciclopearmacao1
            matriz[18, 26:60] = branco

            matriz[19, 0:11] = branco
            matriz[19, 11:12] = ciclopearmacao2
            matriz[19, 12:24] = ciclopearmacao1
            matriz[19, 24:25] = ciclopearmacao2
            matriz[19, 25:60] = branco

            matriz[20, 0:12] = branco
            matriz[20, 12:14] = ciclopearmacao2
            matriz[20, 14:21] = ciclopearmacao1
            matriz[20, 21:24] = ciclopearmacao2
            matriz[20, 24:60] = branco

            matriz[21:50, 0:60] = branco

            return matriz

        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       ciclopearmacao1_r,
                       ciclopearmacao2_r,
                       ciclopelente1_r,
                       ciclopelente2_r)

        g = geraPixels(g,
                       ciclopearmacao1_g,
                       ciclopearmacao2_g,
                       ciclopelente1_g,
                       ciclopelente2_g)

        b = geraPixels(b,
                       ciclopearmacao1_b,
                       ciclopearmacao2_b,
                       ciclopelente1_b,
                       ciclopelente2_b)


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b


        plt.figure(figsize=(x, y))
        plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches=0)

        # plt.show()

# base = OculosCiclope2(5, 4)