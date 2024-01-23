from random import randint
from time import sleep  
print(''' Suas opções
[0] Pedra 
[1] Papel
[2] Tesoura
''')
esc = int(input('Qual a sua jogada?'))
ran = randint(0,2)
if (esc == 0): 
    jg1 ='PEDRA'
if(esc == 1):
    jg1 ='PAPEL'
if (esc == 2):
    jg1 ='TESOURA'
if (ran == 0): 
    jg2 ='PEDRA'
if(ran == 1):
    jg2 = 'PAPEL'
if (ran == 2):
    jg2 = 'TESOURA'  
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POO!!')
print('=+'*14)
print('Sua jogada foi {}!!\nSeu oponente jogou {}!!'.format(jg1,jg2))
print('=+'*14)

if (esc == 0) and (ran == 1):
    print('VOCE PERDEU!! TENTE NOVAMENTE')
elif(esc == 1) and (ran == 2):
    print('VOCE PERDEU!! TENTE NOVAMENTE')
elif (esc == 2) and (ran == 0):
    print('VOCE PERDEU!! TENTE NOVAMENTE')
elif (esc == ran):
    print('EMPATE!! JOGUE NOVAMENTE')
else:
    print('PARABENS!! VOCE GANHOU')
   
