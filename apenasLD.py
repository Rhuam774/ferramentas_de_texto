from time import sleep
import re




while True:
    nome_arquivo = input('qual o aquivo? ')
    arquivoA = open(nome_arquivo, 'r')
    arquivoN = open(f'{nome_arquivo}_editado.txt', ('w'))
    filtro = input('palavra chave')

    for lin in arquivoA:
        try:
            if re.findall(filtro, lin, re.IGNORECASE):
                arquivoN.write(lin)
        except Exception as erro :
            print(erro)
    print('bingo!!\n\n')
    sleep(2)

    arquivoA.close()
    arquivoN.close()
