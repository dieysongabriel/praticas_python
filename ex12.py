
notaPortugues = float(input('Digite sua nota em português: '));
notaMatematica = float(input('Digite sua nota em matemática: '));
notaGeografia = float(input('Digite sua nota em geografia: '));
notaCiencias = float(input('Digite sua nota em ciências: '));
notaHistoria = float(input('Digite sua nota em historia: '));
notaFisica = float(input('Digite sua nota em fisica: '));


def calcularMedia():

    totalNotas = notaPortugues + notaMatematica + notaGeografia + notaCiencias + notaHistoria + notaFisica;
    media = totalNotas / 6;
    if(media < 5):
        print('Reprovado!');
    elif(media < 6.9):
        print('Recuperação');
    else:
        print('Aprovado');

calcularMedia();