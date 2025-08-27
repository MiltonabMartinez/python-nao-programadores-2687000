# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, 
# ano que conheceu o LinkedIn, ano atual e 
# os cursos realizados no LinkedIn Learning 
# separados por virgula em ordem cronológica
estudante={}

estudante['nome'] = input("Digite seu nome: ")
estudante['anolinkedin']=int (input("Em que ano conheceu o Linkedin: "))
estudante['anoatual']=int(input("Digite o Ano Atual "))
cursos = input("Digite os Cursos feitos por você no LinkedIn separados por virgula em ordem cronológica : ")

estudante ['cursos'] = cursos.split(', ')
# 2. Armazene esses dados em um dicionário

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos=estudante['anoatual']-estudante['anolinkedin']
total_cursos=len(estudante['cursos'])

print(f"Oi {estudante['nome']} desde {estudante['anolinkedin']} voce conhece o Linkedin.Nesses {total_anos},voce realizou {total_cursos} cursos, sendo  o primeiro curso ")

