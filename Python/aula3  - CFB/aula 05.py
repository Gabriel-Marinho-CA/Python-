import random
num_i = 10
num_f = 5.2
num_c = 1j

x=int(num_f) #Podemos converver tipos inteiros em float e tipos float em inteiros, ex: 
# 10 em float é 10.0 , 5.2 em int é 5

print("Valor : " + str(x) + " - Tipo: " + str(type(x)))

num_r = [ #List / Array começa no 0
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
    random.randrange(0,60),
]

print("Valor 1: " + str(num_r[0]))
print("Valor 2: " + str(num_r[1]))
print("Valor 3: " + str(num_r[2]))
print("Valor 4: " + str(num_r[3]))
print("Valor 5: " + str(num_r[4]))
print("Valor 6: " + str(num_r[5]))
print("--------------------------------------------")

curso = " Curso de Python "

print(curso[9:15]) # Do caractere 9 ao 15

print(str(curso.lower())) # Deixa tudo em minusculo

print(str(curso.strip())) #Strip tira os espaços

print(curso.strip().lower()) #unindo os 2

print(curso.upper()) # Maiusculo
 
print(curso.replace("Python","C#")) # Substitui uma palavra pela outra

a = curso.split(" ") #meio que divide as string em partes de acordo com oque voce quer separar por parametro ex: separar por espaços, por ponto etc... , no caso [1] = curso [2] = de [3] = python


print("Tamanho: " + str(len(curso))) 

print(a[3])

print("------------------------------------")

texto = "Curso de Python"
palavra = "python"

res = palavra.upper() not in texto.upper () #apresenta um valor booleano in =  está, not in = nao esta
print(res)

print("---------------------------------")

curso1 = "Curso de Python"
canal = "CFB Cursos"

res = curso1 + " do canal " + canal
print (res)

print("--------------------------")
cidade =  "Belo Horizonte"
dia = 15
mes = " Dezembo "
ano = 2019
data = "{}, de {} de {} de {} \n {}" # Um outro jeito de fazer a concatenacao das variaveis sem uas o +, onde esta o {} é onde vai a variavel. atraves da tag var.format(var1,var2,var3,...)

print(data.format(cidade,dia,mes,ano,canal)) # O \n é uma quebra de linha

# Alguns caracteres de scape : 
# \' \" \n \r \t \b
