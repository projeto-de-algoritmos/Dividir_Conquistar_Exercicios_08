# ================================================================================================
# Leetcode - 240 . Pesquise uma Matriz 2D II - Nível Médio
# ================================================================================================
# Teoria: Dividir e Conquistar
# Algoritmo utilizado: Algoritmo que divide recursivamente uma matriz em quatro submatrizes para 
# buscar o valor procurado (target)
# ================================================================================================
class Solution:
    def searchMatrix(self, matrix, target):
        # target - valor procurado na matriz

        if not matrix or not matrix[0]:
            return False
        
        def exploreSubMatrix(linha_i, coluna_i, linha_j, coluna_j):
            if linha_i > linha_j or coluna_i > coluna_j :
                return False
            # condicao de parada - matriz de um elemento
            if linha_i == linha_j and coluna_i == coluna_j:
                return matrix[linha_i][coluna_i] == target
            
            _minimo, _maximo = matrix[linha_i][coluna_i], matrix[linha_j][coluna_j]
            if _minimo <= target <= _maximo:
                # dividindo o tamanho da matriz por 2 nas duas dimensoes
                linha_m, coluna_m = (linha_i + linha_j) // 2, (coluna_i + coluna_j) // 2
                # vamos dividir recursivamente a matriz em 4 submatrizes
                return  exploreSubMatrix(linha_i, coluna_i, linha_m, coluna_m) or \
                        exploreSubMatrix(linha_i, coluna_m + 1, linha_m, coluna_j) or \
                        exploreSubMatrix(linha_m + 1, coluna_i, linha_j, coluna_m) or \
                        exploreSubMatrix(linha_m + 1, coluna_m + 1, linha_j, coluna_j)
            return False
            
        # verifica o tamanho da matriz
        linhas, colunas = len(matrix), len(matrix[0])
        # chama a funcao recursiva para trabalhar com as submatrizes
        # e procurar o valor target
        return exploreSubMatrix(0, 0, linhas - 1, colunas - 1)