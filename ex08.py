
valorProduto = float(input('Qula é o preço do produto? R$'));

valorDesconto = valorProduto * 5 / 100

valorFinal = valorProduto - valorDesconto;

print(f'O produto que custava R${valorProduto}, na promoção com desconto de 5% vai custar R${valorFinal}');