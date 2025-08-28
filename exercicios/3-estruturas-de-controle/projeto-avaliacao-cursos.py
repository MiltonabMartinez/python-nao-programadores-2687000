# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
cursos_linkedin= ['Introduçao a SQL ' ,'ITIL','Python' ,'Formaçao Basica','Fundamentos de Programacao']
curso_git = 'Git e Git Hub: Formacao Basica'
curso_python = 'Python'
curso_itil = 'ITIL'

avaliacoes ={}
if curso_python in cursos_linkedin :
   print(f"O curso esta no catalogo , Por favor avalie o curso")
   avaliacoes [curso_python] = int(input('Qual é a nota que voce da para o curso (0 a 5)?'))

if curso_git in cursos_linkedin :
  print(f"O curso esta no catalogo , Por favor avalie o curso")
  avaliacoes [curso_git] = int(input('Qual é a nota que voce da para o curso (0 a 5)?'))

if curso_itil in cursos_linkedin :
  print("Infelizmente o curso não compoe nosso catalogo")
  avaliacoes [curso_itil] = int(input('Qual é a nota que voce da para o curso (0 a 5)?'))
else:
   print("Infelizmente o curso nao compoe nosso catalogo")
print (avaliacoes)