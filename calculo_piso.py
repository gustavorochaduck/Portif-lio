# Mensagem de Bem vindo
print('Bem vindo')
print('Esse aplicativo Calcula a uma área exata com o valor do piso ')

# Coleta de dados
print('Por favor apenas digite os valores')
piso = int(input('Valor do metro quadrado: '))
# L = int(input('Digite a Largura: '))
# A = int(input('Digite a Altura:'))
M = int(input('Digite o tamanho da área em Metros Quadrados'))
# A = Altura - L = largura - piso = Valor do piso - M = Metros Quadrados

# Calculo
# c1 = A * L
# c2 = piso * c1
c3 = piso * M

# Resposta

print(f'O valor ficou: R${c3}')

# Coleta de dados 2

v = int(input('Escreva o valor da hora de trabalho: ') )
h = int(input('Horas trabalhadas: '))

# Calculo 2

c4 = v * h
c5 = c4 + c3
# Resposta

print(f'O valor para o Cliente fica: R${c5}')
print(f'Valor da hora de trabalho: R${c4}')
print(f'Valor do piso: R${c3}')
