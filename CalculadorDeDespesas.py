print('CALCULADORA DE DESPESAS')
bancos = int(input('Quantos bancos você está com a fatura aberta?:'))
faturaTotal = []
guardadoTotal = []
for contador in range (bancos):
    fatura = float(input('Digite quanto está sua fatura do banco {}: '.format(contador + 1)))
    faturaTotal.append(fatura)
print('Você tem algum dinheiro guardado?\n1 = sim\n2 = não')
escolha = int(input(''))
if escolha == 1:
    QuantidadeGuardado = int(input('Em quantos locais você tem dinheiro guardado?:'))
    for contadorDois in range(QuantidadeGuardado):
        guardado = float(input('Digite quanto está guardado no {}° local: '.format(contadorDois + 1)))
        guardadoTotal.append(guardado)
elif escolha == 2:
    print('Certo')
else:
    print('Opção invalida')

resultado = sum(faturaTotal) - sum(guardadoTotal)

if resultado <= 0:
    print('Você tem nenhuma divida e tem {} reais sobrando'.format(resultado))
elif resultado > 0:
    print('Você tem uma divida de {} reais'.format(resultado))