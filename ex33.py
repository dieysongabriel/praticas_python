
import pdb
def filtrar_palavras(palavras):
    pdb.set_trace()
    return [p for p in palavras if len(p) > 5]

lista = ["gato", "elefante", "cachorro", "pato"]

print(filtrar_palavras(lista));