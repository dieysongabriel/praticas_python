#Conversor de Medidas

def calcMedida():
    medida = float(input('Digite uma medida em metros: '));
    cm = round(medida * 100, 1);
    mm = round(medida * 1000, 1);
    print(f'{medida} Metros equilave á {cm}cm e a {mm}mm');


calcMedida();