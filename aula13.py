nome = 'Gabriel'
idade = 23
altura = 1.83
peso = 105
imc = peso / (altura ** 2)

#f-strings
linha_1 = f'Gabriel tem {idade} anos, pesa {peso} kilos, mede {altura:.2f} e seu IMC é {imc:.2f}'
print(linha_1)
#print('Gabriel tem', idade, 'anos, pesa', peso, 'kilos, mede', altura,
 #    'e seu IMC é:', imc)