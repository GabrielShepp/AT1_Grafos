import numpy as np


def criaMatriz(Inst):
    print("Abrindo o arquivo:", Inst, "\n\n")
    local = 'C:/Users/gabri/AT1/Instancias/' + Inst + ".txt" #salvando o local do arquivo

    with open(local, "rb") as m:
        matriz = np.genfromtxt(m, dtype='int64')#transformando os dados do DataSet em Matriz
    return matriz#Retornado a matriz para que possa ser utilizada


Instancia = input("Digite o nome do arquivo\n")#Pedindo ao usuário que entre com o nome do arquivo
Matx = criaMatriz(Instancia)
Linhas = Matx.shape[0]
Colunas = Matx.shape[1]

print("A matriz possui " + str(Linhas) + " linhas e " + str(Colunas) + " colunas")
Resultados = "C:/Users/gabri/AT1/Resultado/Resultado"#Local do arquivo para que os Resultado sejam salvos
with open(Resultados, "w") as R:
    R.write("O nome do arquivo é:  "+Instancia
            +"\nLinhas:  "+ str(Linhas)
            +"\nColunas:  "+ str(Colunas))#Salvando os resultados no Arquivo

