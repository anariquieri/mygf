
print('\033[1;36m Olá , Rayni! estou aqui pra te ajudar a escolher o mel'
      'hor dia\npra pedir a Ana Carolina em namoro!\033[m')

print('\033[1;95m Para evitar explicar as regras e protolos é que es'
      'se programa\nfoi criado! Relaxe e tente a sorte para agradar Ana Carolina!!!\033[m')

diabom = ['02', '07', '11', '12', '16', '20', '28', '30']
diaruim = ['10', '13', '27', '21', '15', '17', '19', '24', '06', '29', '14']
dianeutro = ['01', '03', '04', '05', '08', '09', '18', '21', '22', '23', '25', '26', '31']

mesbom = ['01', '06', '07', '10', '11', '12']
mesruim = ['02', '03', '04', '05']
mesneutro = ['08', '09']

print('-=' * 30)

print('Caso queira facilitar um pouco mais sua escolha:')
print('\033[1;32mDIGITE 1 PARA SABER TODAS AS DATAS BOAS\033[m')
print('\033[1;33mDIGITE 2 PARA SABER TODAS AS DATAS NEUTRAS\033[m')
print('\033[1;31mDIGITE 3 PARA SABER TODAS AS DATAS RUINS\033[m')
print('\033[1;34mDIGITE 0 PARA ESCOLHER SUA PRÓPRIA DATA\033[m')

print('-=' * 30)
c = -1
opção = input('Sua escolha:')
if opção == '1':
    print('\033[1;32mAqui estão todas melhores datas!\033[m')
    while c < 200:
        print((diabom[c + 1]) + '/' + (mesbom[0]))
        print((diabom[c + 1]) + '/' + (mesbom[1]))
        print((diabom[c + 1]) + '/' + (mesbom[2]))
        print((diabom[c + 1]) + '/' + (mesbom[3]))
        print((diabom[c + 1]) + '/' + (mesbom[4]))
        print((diabom[c + 1]) + '/' + (mesbom[5]))
        c += 1
elif opção == '2':
    print('\033[1;33mAqui estão todas as datas neutras!\033[m')
    while c < 100:
        print(dianeutro[c + 1] + '/' + mesneutro[0])
        print(dianeutro[c + 1] + '/' + mesneutro[1])
        c += 1

elif opção == '3':
    print('\033[1;31mAqui estão as PIORES datas\033[m')
    while c < 50:
        print(diaruim[c + 1] + '/' + mesruim[0])
        print(diaruim[c + 1] + '/' + mesruim[1])
        print(diaruim[c + 1] + '/' + mesruim[2])
        print(diaruim[c + 1] + '/' + mesruim[3])
        c += 1
elif opção == '0':
    print('   \033[1;96mParece que você confia no seu taco! '
          'Digite o dia e o mês desejados\ncom a formatação de DOIS '
          'DIGITOS, por exemplo "01/01" e não 1/1, okay?\033[m')
dia = (input('Digite aqui o dia desejado (1 a 31): '))
mes = (input('Digite aqui o mês desejado (1 a 12): '))
data = dia + '/' + mes
print('\033[1;34mData selecionada: {}\033[1;33m \033[m'.format(data))

if dia == '02' or dia == '07' or dia == '11' or dia == '12' or dia == '16' or dia == '20' or dia == '28' or dia == '30':
    print('VOCÊ ESCOLHEU UM ÓTIMO DIA!')
elif dia == '01' or dia == '03' or dia == '04' or dia == '05' or dia == '08' or dia == '09' or dia == '18' or dia == '21' or dia == '22' or dia == '23' or dia == '25' or dia == '26' or dia == '31':
    print('VOCÊ ESCOLHEU UM DIA NEUTRO! É UMA BOA ESCOLHA!')
elif dia == '10' or dia == '27' or dia == '21' or dia == '15':
    print('Esse dia corresponde ao aniversário de algum membro da minha familia! DIA NÃO APROVADO!')
elif dia == '13':
    print('13 traz azar oh sua filha da puta pensa com a cabeça e não c a bct')
else:
    print('Não gostei do dia.')

if mes == '01'or mes == '06' or mes == '07' or mes == '10' or mes == '11' or mes == '12':
    print('A ESCOLHA DO MÊS FOI PERFEITA!')
elif mes == '08' or mes == '09':
    print('VOCÊ ESCOLHEU UM MÊS NEUTRO! É UMA BOA ESCOLHA!')
else:
    print('Não gostei do mês.')
