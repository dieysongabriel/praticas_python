

from datetime import datetime, timedelta, date

today = date.today();

niver = date(2026, 4, 14);

dias = niver - today;
print(f'Faltam {dias} para o seu próximo aniversário');