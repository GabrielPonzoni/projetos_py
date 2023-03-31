n = int(input("Digite um número inteiro: "))
for i in range(0, n+1): #i vai de 0 a 10 + 1 -> i começa com 0
    fat = 1
    fat_str = "" #crio uma string vazia
    for j in range(i, 0, -1): #j vai de 0 a 0 na primeira vez depois i ja vale 1,2,3 e assim vai até n+1
        fat *= j #1 x 0 = 1
        fat_str += str(j) + "x" #adiciono os números dentro da string
    fat_str = fat_str[:-1] + "="  #pego a string no finl e removo o último índice com a ferramenta slice(Remove o último "⋅" e adiciona um "=")
    print(f"{i}! = {fat_str} {fat}")
