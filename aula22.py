# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E] Entrar [S] Sair: ')
# if entrada == 'E' or entrada == 'e':
#     senha_digitada = input('Senha: ')
# elif entrada == 'S':
#     print('Até mais!')
# else:
#     print('Opção inválida')

# senha_permitida = '123456'
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Acesso liberado')
# else:
#     print('Acesso negado')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)