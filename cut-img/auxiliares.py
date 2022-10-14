#Importações necessárias.
import os
import cv2


def retornaListaDeConteudoNoDiretorio(path):

    #Gera lista de conteúdo presente na pasta informada.
    contents = os.listdir(path)

    #Retornando lista com todos os conteúdos.
    return contents

def retornaListaComConteudoDoArquivoDeTexto(txt):

    contents = []

    with open(txt) as file:

        #Percorre arquivo linha por linha.
        for line in file:

            #Separa conteúdo da linha por espaços em branco (" "). 
            elements = line.split(" ")

            contents.append(elements)
    
    #Retorna lista com lista(s) de conteúdo.
    return contents



def verificaSeClasseCachorroEstaNoArquivo(txt):

    #Abre arquivo para ler conteúdo.
    with open(txt) as file:

        #Percorre arquivo linha por linha.
        for line in file:

            #Separa conteúdo da linha por espaços em branco (" "). 
            listaValores = line.split(" ")

            #Se o primeiro elemento (identificador de classe) for igual a 16, siginifica que cachorro foi identificado.
            if listaValores[0] == "16": #String ou Int
                return "dog"

                #Essa parte é para o corte de imagem.   
                # for elem in listaValores:
                #     print(elem)

            print("Fim!")

def cortaRetanguloIdentificadoPelaYolo(infos, img):

    #definindo atributos da imagem.
    largura = img.shape[1]
    # print(largura)
    altura = img.shape[0]
    # print(altura)

    x = 0.583333 * largura
    y = 0.5375 * altura
    w = 0.833333 * largura
    h = 0.925 * altura

    #provisório: parâmetros para fazer o corte da imagem, posteriormente utilizaremos os arquivos com os dados.
    starting_x_coordinate = x - (w/2)
    starting_y_coordinate = y - (h/2)
    ending_x_coordinate = x + (w/2)
    ending_y_coordinate = y + (h/2)

    #recorta pedaço da imagem de acordo com os parametros passados
    crop_image = image[round(starting_y_coordinate):round(ending_y_coordinate), round(starting_x_coordinate):round(ending_x_coordinate)]

    #exibe imagem
    cv2.imshow("Cropped", crop_image)

    #não sei o que faz
    cv2.waitKey(0)
