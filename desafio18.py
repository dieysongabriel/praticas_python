

import time

def contagem_regressiva():
    tempo = int(input('Digite o tempo(segundos): '));

    while tempo >= 1:
        print(tempo)
        time.sleep(1)
        tempo -= 1
    print('Tempo esgotado');

contagem_regressiva()