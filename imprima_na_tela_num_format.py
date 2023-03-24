#4. Imprima os números 1, 10, 100 e 1000 utilizando um espaço de 7 colunas, alinhando o 
#conteúdo à esquerda, depois centralizando e em seguida alinhando à direita. Para essa 
#atividade, consulte as referências na última página.

print("ALINHADO À ESQUERDA\n")
print(1,2,3,4,5,6,7, sep="")
print("{:<7}".format(1))
print("{:<7}".format(10))
print("{:<7}".format(100))
print("{:<7}".format(1000))

print("\nALINHANDO NO MEIO\n")
print(1,2,3,4,5,6,7, sep="")
print("{:^7}".format(1))
print("{:^7}".format(10))
print("{:^7}".format(100))
print("{:^7}".format(1000))

print("\nALINHANDO À DIREITA\n")
print(1,2,3,4,5,6,7, sep="")
print("{:>7}".format(1))
print("{:>7}".format(10))
print("{:>7}".format(100))
print("{:>7}".format(1000))