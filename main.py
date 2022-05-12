#####################################################
#       Geração de NFTs (non-fungible token)        #
#                                                   #
# autor: Daniel Dias da Silva                       #
# 29/03/2022                                        #
#                                                   #
#####################################################

import criaNFT
import suavizacao
import geraAderecos
# Número de NFTs a gerar
n = 20

# Tamanho da imagem
x = 5
y = 4

if __name__ == "__main__":

    # Gera imagens bases a partir das matrizes de imagem, salvando nas pastas
    geraAderecos.GeraAderecos(x, y)

    # Realiza suavização dos adereços gerados
    suavizacao.Suavizacao()

########################################################
########################################################

    def contaNFTs(listaObjetos):
        for nft in listaObjetos:
            print(nft.nft)


    # Inicia criação de vetor com os elementos do objeto de cada NFT
    # Posteriormente cria a imagem do objeto de cada NFT

    NFTlista = []
    i = 0

    # Primeiro NFT gerado, não tornar a lista inicial vazia
    NFTs = criaNFT.NFT(0)
    NFTlista.append(NFTs)

    # Gera lista de objetos com a matriz dos NFTs
    while len(NFTlista) < n:

        verificaIgualdade = 0
        NFTs = criaNFT.NFT(i + 1)

        # Verificar se há igualdade entre as matrizes geradas de cada NFT
        for x in NFTlista:
            if x.nft == NFTs.nft:
                verificaIgualdade = verificaIgualdade + 1
                break

        # Adiciona NFT a lista de vetores de objetos se não existir um igual
        if verificaIgualdade == 0:
            NFTlista.append(NFTs)


    contaNFTs(NFTlista)
    print("------------------ FIM ------------------")
    print(len(NFTlista))

    # Gera a Imagem de cada NFTs
    numeracao = 0

    for geraNFT in NFTlista:

        # Envia elementos de cada objeto
        geraNFT.elementos(geraNFT.nft, numeracao)
        numeracao = numeracao + 1
        # time.sleep(5)

print('NFTs gerados!!')
print('Boa sorte')