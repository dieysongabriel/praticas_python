

def maiores_25(arquivoEntrada, arquivoSaida):

    with open(arquivoEntrada) as entrada:
        linhas = entrada.readlines()
    
    linhas = linhas[1:]
    maiores = []


    for linha in linhas:
        nome, idade = linha.strip().split(',')
        if int(idade) > 25:
            maiores.append(f'{nome},{idade}\n')
    
    with open(arquivoSaida, 'w') as saida:
        saida.write('nome, idade\n')
        saida.writelines(maiores);

maiores_25('dados.csv', 'maiores.csv');
