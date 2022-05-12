from imgs_matriz import BaseImg
from imgs_matriz import coleira1
from imgs_matriz import coleira2
from imgs_matriz import coleira3
from imgs_matriz import coleira4
from imgs_matriz import coleira5
from imgs_matriz import oculos1
from imgs_matriz import oculos2
from imgs_matriz import oculos3
from imgs_matriz import oculosciclope1
from imgs_matriz import oculosciclope2
from imgs_matriz import oculosciclope3
from imgs_matriz import oculosTapaOlho
from imgs_matriz import fundo1
from imgs_matriz import fundo2
from imgs_matriz import fundo3
from imgs_matriz import fundo4
from imgs_matriz import fundo5
from imgs_matriz import fundoDegrade1
from imgs_matriz import fundoDegrade2
from imgs_matriz import fundoDegrade3
from imgs_matriz import cigarro1
from imgs_matriz import cigarro2
from imgs_matriz import cigarroCharuto1
from imgs_matriz import cigarroCachimbo1
from imgs_matriz import brinquedo1
from imgs_matriz import brinquedo2


class GeraAderecos():

    def __init__(self, x, y):
        # x = 5
        # y = 4

        BaseImg.BaseImg(x, y)

        fundo1.Fundo1(x, y)
        fundo2.Fundo2(x, y)
        fundo3.Fundo3(x, y)
        fundo4.Fundo4(x, y)
        fundo5.Fundo5(x, y)
        fundoDegrade1.FundoDegrade1(x, y)
        fundoDegrade2.FundoDegrade2(x, y)
        fundoDegrade3.FundoDegrade3(x, y)

        coleira1.Coleira1(x, y)
        coleira2.Coleira2(x, y)
        coleira3.Coleira3(x, y)
        coleira4.Coleira4(x, y)
        coleira5.Coleira5(x, y)

        oculos1.oculos1(x, y)
        oculos2.oculos2(x, y)
        oculos3.oculos3(x, y)

        oculosciclope1.OculosCiclope1(x, y)
        oculosciclope2.OculosCiclope2(x, y)
        oculosciclope3.OculosCiclope3(x, y)

        oculosTapaOlho.TapaOlho(x, y)

        cigarro1.Cigarro1(x, y)
        cigarro2.Cigarro2(x, y)
        cigarroCharuto1.Charuto(x, y)
        cigarroCachimbo1.Cachimbo1(x, y)

        brinquedo1.Brinquedo1(x, y)
        brinquedo2.Brinquedo2(x, y)


# geraimgs = GeraAderecos(5, 4)
