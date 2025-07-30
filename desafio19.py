

def conversor():

    print('Conversor de número romano para decimal')
    nr = input('Digite um número romano: ').upper()
    total = 0
    i = 0

    while i < len(nr):
        if nr[i] == 'I':
            if i+1 < len(nr) and nr[i+1] == 'V':
                total += 4
                i += 2
            elif i+1 < len(nr) and nr[i+1] == 'X':
                total += 9
                i += 2
            else:
                total += 1
                i += 1
        elif nr[i] == 'V':
            total += 5
            i += 1
        elif nr[i] == 'X':
            if i+1 < len(nr) and nr[i+1] == 'L':
                total += 40
                i += 2
            elif i+1 < len(nr) and nr[i+1] == 'C':
                total += 90
                i += 2
            else:
                total += 10
                i += 1
        elif nr[i] == 'L':
            total += 50
            i += 1
        elif nr[i] == 'C':
            if i+1 < len(nr) and nr[i+1] == 'D':
                total += 400
                i += 2
            elif i+1 < len(nr) and nr[i+1] == 'M':
                total += 900
                i+= 2
            else:
                total += 100
                i += 1
        elif nr[i] == 'D':
            total +=  500
            i += 1
        elif nr[i] == 'M':
            total += 1000
            i += 1
        else:
            print('Símbolo inválido!')
            break
    print(f'Valor decimal: {total}')



conversor()