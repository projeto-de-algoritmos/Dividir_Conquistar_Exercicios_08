# ================================================================================================
# Leetcode - 53 . Maximo Subarray - Nível Medio
# ================================================================================================
# Teoria: Dividir e Conquistar
# Algoritmo utilizado: Algoritmo que divide recursivamente um array pela metade e 
# encontra o valor maximo do array completo
# ================================================================================================
import math

def findMaxSubArray(nums: list[int], left: int, right: int):
    # Condiçao de parada
    if left > right:
      return -math.inf     
    # Determina o meio do array
    meio = (left + right) // 2
    soma_esq = 0 
    soma_dir = 0 
    soma_atual = 0
    # Verifica o maximo lado esquerdo
    for i in range(meio - 1, left - 1, - 1): 
      # Checa o maior valor que conseguiu assumir desde o meio
      soma_esq = max(soma_esq, soma_atual := soma_atual + nums[i]) 
    soma_atual = 0
    # Verifica o maximo do lado direito
    for i in range(meio + 1, right + 1): 
      soma_dir = max(soma_dir, soma_atual := soma_atual + nums[i]) # Checa o maior valor que conseguiu assumir desde o meio
    # chama recursivamente para cada metade
    return max(findMaxSubArray(nums, left, meio - 1), \
               findMaxSubArray(nums, meio + 1, right), soma_esq + soma_dir + nums[meio])

class Solution:
  def maxSubArray(self, nums: list[int]) -> int:
    # chama a funcao recursiva para o array inteiro
    return findMaxSubArray(nums, 0, len(nums) - 1)
