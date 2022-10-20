import os
import auxiliares

#Definindo caminho até pasta com os "exps".
caminho = "C:\\Users\\marcos\\yolov7\\runs\\detect"

#Rodando comando a partir daqui.
os.system("python detect.py --save-txt --weights yolov7-e6e.pt --source imagens")

#Salvamos em uma lista todos o nome de todas as pastas "exps" que temos no "caminho".
exps = auxiliares.retornaListaDeConteudoNoDiretorio(caminho)

for exp in exps:

    #Contador para alterar entre imagens.
    contadorImagens = 0

    #Cria pasta para salvar imagens.
    os.mkdir(caminho + "\\" + exp + "\\imagens-cortadas")

    #Salva caminho para ser utilizado.
    dirImagensCortadas = caminho + "\\" + exp + "\\imagens-cortadas"

    #Primeiro lemos o as imagens contidas na pasta.
    imagens = auxiliares.retornaListaDeConteudoNoDiretorio(caminho + "\\" + exp)
    
    #Removemos o elemento "labels" da lista.
    imagens.remove("labels") #Se for certeza que "labels" é último elemento, posso trocar para (len - 1).

    #Agora pegamso as os txts dentro de "labels".
    txts = auxiliares.retornaListaDeConteudoNoDiretorio(caminho + "\\" + exp + "\\labels")

    for txt in txts:
        
        #Lendo conteúdo do arquivo de texto.
        conteudoDoTxt = auxiliares.retornaListaComConteudoDoArquivoDeTexto(caminho + "\\" + exp + "\\labels\\" + txt)

        #Percorrendo linhas do arquivos texto.
        for linha in conteudoDoTxt:
            
            #Só corta se for da classe cachorro.
            if linha[0] == "16":
                
                auxiliares.cortaRetanguloIdentificadoPelaYolo(linha, caminho + "\\" + exp + "\\" + imagens[contadorImagens], imagens[contadorImagens], dirImagensCortadas)
        
        #Incrementa contador para pegar próxima imagem.
        contadorImagens += 1