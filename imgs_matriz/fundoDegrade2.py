import numpy as np
import matplotlib.pyplot as plt

pasta = 'imgs_geradas/1fundo/fundodegrade2.png'


class FundoDegrade2:

    def __init__(self, x, y):

        fundo_r = 47
        fundo_g = 79
        fundo_b = 79

        def geraPixels(matriz, fundo):

            for i in range(0, 60):
                matriz[i:i+1, i:i+1] = fundo+i

                for j in range(0, 60):
                    matriz[i:j + 1, i:j + 1] = fundo+i
                    for z in range(0, 60):
                        matriz[j:z + 1, z:z + 1] = fundo + i

            matriz[42:50, 0:60] = fundo
            return matriz

        r = np.zeros((50, 60), dtype=np.float32)
        g = np.zeros((50, 60), dtype=np.float32)
        b = np.zeros((50, 60), dtype=np.float32)

        # Linha x Coluna X layers  matriz nula
        m = np.zeros((50, 60, 3), 'uint8')

        r = geraPixels(r, fundo_r)

        g = geraPixels(g, fundo_g)

        b = geraPixels(b, fundo_b)

        # #atribui matriz as camadas de m
        m[:, :, 0] = r
        m[:, :, 1] = g
        m[:, :, 2] = b

        plt.figure(figsize=(x, y))
        img = plt.imshow(m, interpolation='nearest')
        plt.axis('off')
        plt.savefig(pasta, bbox_inches='tight', pad_inches=0)
        # plt.show()


# fundo = FundoDegrade2(5, 4)
