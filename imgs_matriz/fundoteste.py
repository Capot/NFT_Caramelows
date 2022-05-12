import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/1fundo/fundo1.png'


class Fundo1:

    def __init__(self, x, y):
        branco = 255

        fundo_r = 251
        fundo_g = 236
        fundo_b = 93

        fundoescuro_r = 241
        fundoescuro_g = 226
        fundoescuro_b = 83

        def geraPixels(matriz,
                       fundo,
                       fundoescuro):
            i = 0
            for i in range(0, 60):

                matriz[i:i+1, 0:i+1] = fundo+i
                # matriz[42:50, 0:60] = fundoescuro
                i = i + 1

            return matriz

        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r,
                       fundo_r,
                       fundoescuro_r)

        g = geraPixels(g,
                       fundo_g,
                       fundoescuro_g)

        b = geraPixels(b,
                       fundo_b,
                       fundoescuro_b)

        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        img = plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        # plt.savefig(pasta, bbox_inches='tight', pad_inches=0)
        plt.show()


fundo = Fundo1(5, 4)
