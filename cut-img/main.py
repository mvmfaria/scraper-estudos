import auxiliares

pastas = auxiliares.retornaListaDeConteudoNoDiretorio("C:\\Users\\marcos\\imagens")

#Vamos supor que a yolo foi rodada em todos diretórios que temos.

for pasta in pastas:

    exps = auxiliares.retornaListaDeConteudoNoDiretorio("C:\\Users\\marcos\\yolov7\\runs\\detect")

    for exp in exps:

        #Recebendo nomes dos arquivos dentro da pasta.
        imagens = auxiliares.retornaListaDeConteudoNoDiretorio("C:\\Users\\marcos\\yolov7\\runs\\detect" + "\\" + exp)
        txts = auxiliares.retornaListaDeConteudoNoDiretorio("C:\\Users\\marcos\\yolov7\\runs\\detect" + "\\" + exp + "\\" + "labels")

        #Verificar se isso funciona.
        for txt in txts:

            conteudoArquivo = auxiliares.retornaListaComConteudoDoArquivoDeTexto(txt)
            infosDeCorte = auxiliares.retornaInformacoesDeCorteDaImagem(conteudoArquivo)

            auxiliares.cortaRetanguloIdentificadoPelaYolo(infosDeCorte, )

    
        






    #Comparando arquivos para ver se é necessário verificar imagem.


