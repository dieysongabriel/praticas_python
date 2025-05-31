
def total_compras(d): return sum(d.values())
def test_compras(): assert total_compras({"maçã":2, "pêra":3}) == 5

def fatorial(n): return 1 if n == 0 else n * fatorial(n - 1)
def test_fatorial(): assert fatorial(5) == 120

def repetir(t, v): return t * v
def test_repetir(): assert repetir("oi", 3) == "oioioi"

def quadrados(l): return list(map(lambda x: x**2, l))
def test_quadrados(): assert quadrados([1, 2, 3]) == [1, 4, 9]
