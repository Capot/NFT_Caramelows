import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/8brinquedos/bolinha2.png'


class Brinquedo2:

    def __init__(self, x, y):
        branco = 255

        bolinha_r = 0
        bolinha_g = 0
        bolinha_b = 128

        bolinhadetalhe_r = 100
        bolinhadetalhe_g = 149
        bolinhadetalhe_b = 237

        def geraPixels(matriz,
                       bolinha,
                       bolinhadetalhe):

            matriz[0:42, 0:60] = branco

            matriz[42, 0:4] = branco
            matriz[42, 4:5] = bolinhadetalhe
            matriz[42, 5:6] = bolinha
            matriz[42, 6:60] = branco

            matriz[43, 0:3] = branco
            matriz[43, 3:5] = bolinha
            matriz[43, 5:6] = bolinhadetalhe
            matriz[43, 6:7] = bolinha
            matriz[43, 7:60] = branco

            matriz[44, 0:2] = branco
            matriz[44, 2:3] = bolinhadetalhe
            matriz[44, 3:6] = bolinha
            matriz[44, 6:7] = bolinhadetalhe
            matriz[44, 7:8] = bolinha
            matriz[44, 8:60] = branco

            matriz[45, 0:2] = branco
            matriz[45, 2:3] = bolinha
            matriz[45, 3:4] = bolinhadetalhe
            matriz[45, 4:7] = bolinha
            matriz[45, 7:8] = bolinhadetalhe
            matriz[45, 8:60] = branco

            matriz[46, 0:3] = branco
            matriz[46, 3:4] = bolinha
            matriz[46, 4:5] = bolinhadetalhe
            matriz[46, 5:7] = bolinha
            matriz[46, 7:60] = branco

            matriz[47, 0:4] = branco
            matriz[47, 4:5] = bolinha
            matriz[47, 5:6] = bolinhadetalhe
            matriz[47, 6:60] = branco

            matriz[48, 0:60] = branco
            matriz[49, 0:60] = branco

            return matriz


        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       bolinha_r,
                       bolinhadetalhe_r, )

        g = geraPixels(g,
                       bolinha_g,
                       bolinhadetalhe_g,
                       )

        b = geraPixels(b,
                       bolinha_b,
                       bolinhadetalhe_b,
                       )


        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        # plt.savefig(pasta, bbox_inches='tight', pad_inches = 0)

        # plt.show()


# base = Brinquedo2(5, 4)