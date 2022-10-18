import auxiliares
import os

caminho = "C:\\Users\\marcos\\yolov7\\runs\\detect\\"
pastas = auxiliares.retornaListaDeConteudoNoDiretorio("C:\\Users\\marcos\\imagens")

#Vamos supor que a yolo foi rodada em todos diretórios que temos.

for pasta in pastas:

    exps = auxiliares.retornaListaDeConteudoNoDiretorio("C:\\Users\\marcos\\yolov7\\runs\\detect")

    for exp in exps:

        if os.path.isdir("C:\\Users\\marcos\\isdog\\cut-img\\" + exp):
            print("ok")
        else:
            os.mkdir ("C:\\Users\\marcos\\isdog\\cut-img\\" + exp)

        pastaSalvaImgs = "C:\\Users\\marcos\\isdog\\cut-img\\" + exp

        #Recebendo nomes dos arquivos dentro da pasta.
        imagens = auxiliares.retornaListaDeConteudoNoDiretorio(caminho + exp)
        txts = auxiliares.retornaListaDeConteudoNoDiretorio(caminho + exp + "\\" + "labels")

        #Verificar se isso funciona.
        for txt in txts:
            
            #Contador para saber imagem que estamos trabalhando.
            img = 0

            conteudoArquivo = auxiliares.retornaListaComConteudoDoArquivoDeTexto(caminho + exp + "\\labels\\" + txt)


            infosDeCorte = auxiliares.retornaInformacoesDeCorteDaImagem(conteudoArquivo)

            print(caminho + exp + "\\labels\\" + imagens[img])

            auxiliares.cortaRetanguloIdentificadoPelaYolo(infosDeCorte, caminho + exp + "\\"+ imagens[img], imagens[img], pastaSalvaImgs)

            print("Conteudo arquivo:", conteudoArquivo)

            infosDeCorte = auxiliares.retornaInformacoesDeCorteDaImagem(conteudoArquivo)

            print("Conteudo de corte:", infosDeCorte)

            img += 1

            #auxiliares.cortaRetanguloIdentificadoPelaYolo(infosDeCorte, )

    
        






    #Comparando arquivos para ver se é necessário verificar imagem.


