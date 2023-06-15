# ========================================================================================================================
# Beecrowd - 1892 - Calouro Vence Veterano? - Nivel 9
# ========================================================================================================================
# Teoria: Dividir e Conquistar
# Algoritmo utilizado: Algoritmo de contagem de inversoes
# ========================================================================================================================

# funcao que calcula a quantidade de inversoes recursivamente
def contarInversoesRecursiva(vetor, ind_esq, ind_dir):
    if ind_dir <= ind_esq:
        return 0

    ind_meio = (ind_esq + ind_dir) // 2

    qtd_inversoes = contarInversoesRecursiva(vetor, ind_esq, ind_meio) + \
                    contarInversoesRecursiva(vetor, ind_meio + 1, ind_dir)

    i = ind_esq
    j = ind_meio + 1
    inv = 0
    vetor_aux = []

    while i <= ind_meio and j <= ind_dir:
        if vetor[i] <= vetor[j]:
            vetor_aux.append(vetor[i])
            i += 1
        else:
            inv += ind_meio - i + 1
            vetor_aux.append(vetor[j])
            j += 1

    while i <= ind_meio:
        vetor_aux.append(vetor[i])
        i += 1

    while j <= ind_dir:
        vetor_aux.append(vetor[j])
        j += 1

    for k in range(ind_esq, ind_dir + 1):
        vetor[k] = vetor_aux[k - ind_esq]

    return qtd_inversoes + inv


# Professor Denis esta curioso para saber se a classificação final de seus N alunos de programaçao
# competitiva segue a ordem de matricula na universidade. Ele pediu a sua ajuda para, dada a 
# classificaçao final, contar quantos pares (i, j) existem tais que i < j e m[i] > m[j], 
# onde 1 ≤ i,j ≤ N e m[i] significa a matricula do aluno que ficou em i-esimo lugar.
if __name__ == '__main__':

    while True:
        try:
            num_alunos = int(input())

            matriculas = []
            for _ in range(num_alunos):
                matricula = input()
                matriculas.append(matricula)

            qtd_inversoes = contarInversoesRecursiva(matriculas, 0, len(matriculas) - 1)

            print(qtd_inversoes)
            
        except EOFError:
            break
