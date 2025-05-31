
def eh_par(n): return n % 2 == 0;
def test_par(): assert eh_par(8) and not eh_par(5);

def inverter(s): return s[::-1];
def test_inverter(): assert inverter('amor') == 'roma';

def palindromo(s): return s.lower.replace(' ', '') == s.lower().replace(' ', '')[::-1]
def test_palindromo(): assert palindromo('Ame a ema');