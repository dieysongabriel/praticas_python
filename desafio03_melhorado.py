
import heapq


def encontrar_caminhos_mais_rapidos(mapa_caminhos, ponto_inicial):
    menor_custo = {ponto: float('inf') for ponto in mapa_caminhos}
    menor_custo[ponto_inicial] = 0;

    caminhos = {ponto: [] for ponto in mapa_caminhos}
    caminhos[ponto_inicial] = [ponto_inicial]

    fila_prioridade = [(0, ponto_inicial)]

    while fila_prioridade:
        custo_atual, ponto_atual = heapq.heappop(fila_prioridade)


        for vizinho, custo_caminho in mapa_caminhos[ponto_atual]:
            novo_custo = custo_atual + custo_caminho


            if novo_custo < menor_custo[vizinho]:
                menor_custo[vizinho] = novo_custo
                heapq.heappush(fila_prioridade, (novo_custo, vizinho));
    
                caminhos[vizinho] = caminhos[ponto_atual] + [vizinho]

    return menor_custo, caminhos;


mapa = {
    'Casa': [('Loja', 5), ('Escola', 10)],
    'Loja': [('Escola', 3), ('Parque', 7)],
    'Escola': [('Parque', 1)],
    'Parque': []

}

custos, caminhos = encontrar_caminhos_mais_rapidos(mapa, 'Casa');

for destino in custos:
    caminho_str = ' → '.join(caminhos[destino]);
    print(f"Para chegar em {destino}: custo = {custos[destino]}, caminho = {caminho_str}");
                                                 

