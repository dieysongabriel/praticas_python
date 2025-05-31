
def validar_idade(i):
    if i < 0:
        raise ValueError("Idade inválida")
    return True


def validar_email(e): return "@" in e and "." in e
def test_email(): assert validar_email("a@a.com")