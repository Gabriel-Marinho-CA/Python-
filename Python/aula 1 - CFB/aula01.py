# Artibuindo variaveis, ele é divido por linhas, da pra atribuir maiis de uma variavel em um mesmo nome ex: nome = gabriel nome = 123, pra ysar isso na mesma linha tem que usar o ;#

Nome = "Gabriel"
Curso = "Ciencia da cc"
print(Nome + " do curso " + Curso) #concatenação = ' + '#

if 10>2:
    print('maior')  #Delimitador de blocos é o espaço no caso o recuo, aqui podemos ver que o "Fim" nao esta com recuo logo esta fora do bloco, é como se fosse fora das {}
    print("Aula 02")
print("Fim")


num1=num2=res=0

def cn():
   global canal    #conseguimos definir uma variavel global dentro de uma função fazenddo global (nome da var) ; var = expressao

   canal = "CFB cruso"
   
cn()
print(canal)

x= 1 #int
x= "Cfb Cursos" #string
x=15.6 # float
x=True # bool

print("Valor : " + str(x))  #Aqui estamos forçando a var tipo inteiro a virar uma string#
print(type(x)) #Aqui estamos vendo qual é o tipo da var type(var)
print ("Tipo: " + str(type(x))) # Aqui estamos concatenando o comando de ver o tipo com uma string, para isso precisamos usar str() antes#

#------------------#

z = ["carro","navio","Aviao", 1 , 58.3, False ] #lista ou array

print("Valor :" +  str(z[4]))
print("Tipo: " + str(type(z)))

c = ("carro","navio","Aviao", 1 , 58.3, False) # Tupla é fechada não podemos modificar os items de uma tupla 

print("Valor c[4] ="+ str(c[4]))
print("Tipo: " + str(type(c)))

v = range(0,100,10) # cria um lista com a quantidade de indices, partino de n valores no caso de n em n. ( de x, á y, de n em n )

print("Valor = "+ str(v[4]))
print("Tipo: " + str(type(v)))

b={ #dicionario ( Dict) é como se eu definice chaves ex : a chave "Canal" tem o valor CFB cursor".
    "canal" : "CFB Cursos",
    "Curso" : "Curso de python",
    "nome" : "Gabriel"
}
print("Valor = "+ str( b["nome"]))
print("Tipo: " + str(type(b)))

m = {5,7,4,6,3,2,2,3} # set ele tem um funcao que alem de ordenar em ordem crescente ele não repete valores

print("Valor = "+ str(m))
print("Tipo: " + str(type(m)))

m = frozenset({5,8,6,7,53,3,3,3}) # Ele bloqueia o set, nao deixa alterar
print("Valor = "+ str(m))
print("Tipo: " + str(type(m)))
