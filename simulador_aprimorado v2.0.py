from time import sleep
from random import choice

# ANSI Cores
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
CYAN = '\033[96m'

# Explosão ASCII
explosion = f"""{RED}
      _.-^^---....,,--       
  _--                  --_  
 <                        >)
 |                         | 
  \._                   _./  
     ```--. . , ; .--'''       
           | |   |             
        .-=||  | |=-.   
        `-=#$%&%$#=-'   
           | ;  :|    
  _____.,-#%&$@%#&#~,._____
{RESET}
"""

# Introdução
print(CYAN + '-='*20)
print('           🚀 NUCLEAR MISSILE LAUNCH PROTOCOL 🚀')
print('-='*20 + RESET)

# Input do jogador
resposta = input(YELLOW + 'LAUNCH MISSILE? (Y/N): ' + RESET).lower().strip()

# Se a resposta for sim
if resposta == 'y':
    print(YELLOW + '\n[ INITIATING LAUNCH SEQUENCE... ]\n' + RESET)
    sleep(1)

    # Contagem regressiva com cor
    for contagem in range(5, 0, -1):
        print(f'{RED}[ {contagem} ]{RESET}')
        sleep(1)

    # Animação de lançamento
    for i in range(10):
        print(f'{CYAN}🚀 Launching missile' + '.' * (i % 4) + RESET, end='\r')
        sleep(0.3)
    
    print('\n' + RED + '[ MISSILE LAUNCHED! ] 💥' + RESET)
    sleep(2)

    # Sorteio do destino do míssil
    chances = [0, 1]
    dado1 = choice(chances)
    dado2 = choice(chances)

    if dado1 == 0:
        print(GREEN + '[ TARGET ACQUIRED! ] 🎯' + RESET)
        sleep(2)

        if dado2 == 0:
            print(explosion)
            print(GREEN + '[ TARGET DESTROYED! ]' + RESET)
            sleep(2)
            print(GREEN + '[ MISSION ACCOMPLISHED ✅ ]' + RESET)
        else:
            print(RED + '[ MISSILE INTERCEPTED! 💥 ]' + RESET)
            sleep(1)
            print(RED + '[ MISSION FAILED ❌ ]' + RESET)
    else:
        print(RED + '[ MISSILE LOST TARGET! ]' + RESET)
        sleep(1)
        print(RED + '[ MISSION FAILED ❌ ]' + RESET)

elif resposta == 'n':
    print(CYAN + '\n[ LAUNCH CANCELED ]' + RESET)
else:
    print(RED + '\n[ INVALID INPUT – ABORTING ]' + RESET)
