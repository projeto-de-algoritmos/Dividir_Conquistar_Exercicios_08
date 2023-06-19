# ========================================================================================================================
# Beecrowd - 1295 - Problema dos Pares Mais Proximos - Nivel 9
# ========================================================================================================================
# Teoria: Dividir e Conquistar
# Algoritmo utilizado: Algoritmo do par de pontos mais proximo
# ========================================================================================================================
import math

# Funçao que calcula a distancia entre dois pontos utilizando a distancia euclidiana
def calcular_distancia(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Funcao que encontra a mediana das medianas de forma recursiva
# Divide o conjunto de numeros em grupos de 5, ordena, determina a mediana
def encontrar_mediana(pontos, k):
    if len(pontos) <= 5:
        return sorted(pontos, key=lambda ponto: ponto[0])[k-1]

    subconjuntos = [pontos[i:i+5] for i in range(0, len(pontos), 5)]
    medianas = [encontrar_mediana(subconjunto, (len(subconjunto) // 2) + 1) for subconjunto in subconjuntos]
    mediana_das_medianas = encontrar_mediana(medianas, (len(medianas) // 2) + 1)

    menores = [ponto for ponto in pontos if ponto[0] < mediana_das_medianas[0]]
    iguais = [ponto for ponto in pontos if ponto[0] == mediana_das_medianas[0]]
    maiores = [ponto for ponto in pontos if ponto[0] > mediana_das_medianas[0]]

    if k <= len(menores):
        return encontrar_mediana(menores, k)
    elif k <= len(menores) + len(iguais):
        return mediana_das_medianas
    else:
        return encontrar_mediana(maiores, k - len(menores) - len(iguais))

# algoritmo de par de pontos mais proximo usando a mediana das medianas
def encontrar_distancia_minima(pontos):
    n = len(pontos)
    if n < 2:
        return float('inf')

    if n <= 3:
        # Calcula diretamente a distância entre todos os pontos
        distancia_minima = float('inf')
        
        for i in range(n):
            for j in range(i+1, n):
                distancia = calcular_distancia(pontos[i], pontos[j])
                if distancia < distancia_minima:
                    distancia_minima = distancia
        return distancia_minima
        
    # Encontra a mediana em relação à coordenada x
    mediana_x = encontrar_mediana(pontos, (n // 2) + 1)

    # Divide os pontos em duas metades com base na mediana_x
    metade_esq = [ponto for ponto in pontos if ponto[0] < mediana_x[0]]
    metade_dir = [ponto for ponto in pontos if ponto[0] > mediana_x[0]]

    # Encontra a distância mínima em cada metade
    distancia_esq = encontrar_distancia_minima(metade_esq)
    distancia_dir = encontrar_distancia_minima(metade_dir)

    # Encontra a distância mínima entre pontos de metades diferentes
    distancia_minima = min(distancia_esq, distancia_dir)

    # Encontra os pontos que estão a uma distância menor ou igual a distancia_minima da mediana_x
    pontos_mediana = [ponto for ponto in pontos if abs(ponto[0] - mediana_x[0]) <= distancia_minima]

    # Ordena os pontos em relação à coordenada y
    pontos_mediana.sort(key=lambda ponto: ponto[1])

    # Calcula a distância mínima considerando apenas pontos próximos à mediana
    tamanho_mediana = len(pontos_mediana)
    for i in range(tamanho_mediana):
        for j in range(i+1, min(i+7, tamanho_mediana)):
            distancia = calcular_distancia(pontos_mediana[i], pontos_mediana[j])
            if distancia < distancia_minima:
                distancia_minima = distancia

    return distancia_minima
    
# Dado um conjunto de pontos em um espaço bidimensional, 
# voce devera encontrar a distancia entre os pontos mais proximos.
while True:
    n = int(input())
    if n == 0:
        break
    
    pontos = []
    for _ in range(n):
        entrada = input().split()
        coord_x = float(entrada[0])
        coord_y = float(entrada[1])
        pontos.append((coord_x, coord_y))
    
    resultado = encontrar_distancia_minima(pontos)
    if (resultado == float('inf')):
        print("INFINITY")
    elif resultado < 10000:
            print("{:.4f}".format(resultado))
    else:
        print("INFINITY")
    
