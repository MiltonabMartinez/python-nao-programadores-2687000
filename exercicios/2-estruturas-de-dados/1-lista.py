# Crie uma lista apenas com elementos numéricos 
l_numerico = [1, 2, 3, 4, 5]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
l_mista = ['python',4,[1,2,3,4],True ,['seg','ter','qua','qui'] ]

# Imprima na tela apenas os 5 primeiros elementos da lista
print('5 primeiros')
print(len(l_mista))
print(l_mista)
print('=========')
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(l_mista[0:-1:2])
print('slice')
# Remova da lista o último item
print('ultimo')
l_mista.pop()
print('========')
# Insira na lista um novo item
l_mista.append('fortran')
print(l_mista)
# Remova da lista um item específico
l_mista.remove('fortran')
print(l_mista)