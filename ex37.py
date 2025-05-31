
def media(l): return sum(l)/len(l)
def test_media(): assert (media[1, 2, 3]) == 2;

def maior(l): return max(l)
def test_maior(): assert maior([1, 7, 3]) == 7

def remove_repetidos(l): return list(set(l))
def test_remove(): assert sorted(remove_repetidos([1,1,2,3])) == [1,2,3]