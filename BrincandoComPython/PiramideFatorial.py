#4. Desenvolva um programa que solicite um número inteiro “n” e imprima na tela o seu fatorial.
#Fatorial é o produto dos números inteiros consecutivos de 1 até um dado inteiro “n”. Utilize tanto
#uma estrutura contada quanto condicional

#estrutura contada
print('-=-' * 30)
n = int(input('Informe um número inteiro para extrairmos seu fatorial: '))
print('-=-' * 30)
count = 0
fatorial = 1 #recebe 1 pois é convenção ele nunca vai ser 0
for i in range(0,n + 1): #se colocar 0 fatorial vai valer 0 dai todo resultado vai dar 0 não funciona! 
  fatorial *= i #=_____ ((f:1 i:1)= 1) (())
  if (fatorial == 0): #evita que ocorra 0 x 0, 0 x 1, 0 x 2...
    fatorial = 1
  print('fatorial de',i,'! =', fatorial)

print('-=-' * 15)

fatorial = 1
i = 0

#estrutura de condicional
while i <= n: #ele faz enquanto a constatação for verdadeiro 
  print('fatorial de',i,'! =', fatorial)
  i += 1 #depois do print pois, ele tem que começar com 0
  fatorial *= i

#modelo com aninhamento 
n = int(input("Digite um número inteiro: "))
for i in range(0, n+1): #i vai de 0 a 10 + 1 -> i começa com 0
    fat = 1
    fat_str = "" #crio uma string vazia 
    for j in range(i, 0, -1): #j vai de 0 a 0 na primeira vez depois i ja vale 1,2,3 e assim vai até n+1
        fat *= j #1 x 0 = 1
        fat_str += str(j) + "x" #adiciono os números dentro da string
    fat_str = fat_str[:-1] + "="  #pego a string no finl e removo o último índice com a ferramenta slice(Remove o último "⋅" e adiciona um "=")
    print(f"{i}! = {fat_str} {fat}")