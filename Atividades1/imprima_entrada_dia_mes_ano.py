#7. Solicite ao usuário o dia, mês e ano do seu nascimento e imprima no terminal a data completa 
#no formato dd/mm/yyyy

dia_nascimento = int(input("Digite o dia do seu nascimento: "))
mes_nascimento = int(input("Digite o mês do seu nascimento: "))
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

print("Você nasceu em {:02d}/{:02d}/{:04d}".format(dia_nascimento,mes_nascimento,ano_nascimento))