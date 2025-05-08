


def iniciaFuncao(dizerOi):
    def finalizaFuncao():
        print('Inicializando Função')
        dizerOi();
        print('Finalizando Função');
    return finalizaFuncao;

@iniciaFuncao
def dizerOi():
    print('Oi, tudo bem?');

dizerOi();

