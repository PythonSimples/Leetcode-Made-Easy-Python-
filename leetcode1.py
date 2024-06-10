"""
Autor: Edson Moreira Bastos
Data: 09/06/24
Versão: 1.0 
"""

def two_sum(nums, target):
    num_map = {}  # Criar um mapa hash para armazenar os números e os seus índices
    for i, num in enumerate(nums): # Usar a função enumerate para obter os números e os índices do array
        complement = target - num # Subtrair um número presente no array ao target
        if complement in num_map: # Procurar o complemento no mapa
            return [num_map[complement], i] # Devolver os índices que somam para target
        num_map[num] = i # caso não encontrar adiciona o valor do indice ao mapa hash

# Exemplo de uso:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Saída: [0, 1]



