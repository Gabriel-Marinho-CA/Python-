

def say_hi(name, age): # o codigo q vai dentro da func é identado
    print ("hello " + name +", you are " + str(age))

say_hi("gabriel", 70)
say_hi("LALA", 30)

#Quando a funcao for chamada ela retorna os parâmetros que nos colocamos 

print ("=========================")

def quadrado(n):
   return n*n*n #Aqui quando a o python vê esse return, qualquer coisa abaixo dele n vai ser exebido, pois ele vê isso e pensa: Preciso retornar isso pra qualquer q seja a chamada
   print("QUADA")

result = quadrado(9)
print(result)
