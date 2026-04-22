import numpy as np
from funcoes_pertinencia import triangular

def agregar_saida(regras: dict):
    """
    Realiza a agregação das saídas fuzzy.
    Retorna:
    - x_saida: universo de discurso da saída
    - mu_saida: função de pertinência agregada
    - graus agregados de baixa, media e alta
    """

    grau_baixa = max(regras["baixa"]) if regras["baixa"] else 0.0
    grau_media = max(regras["media"]) if regras["media"] else 0.0
    grau_alta  = max(regras["alta"]) if regras["alta"] else 0.0

    x_saida = np.linspace(0, 100, 1000)
    mu_saida = []

    for x in x_saida:
        baixa = min(grau_baixa, triangular(x, 0, 0, 50))
        media = min(grau_media, triangular(x, 25, 50, 75))
        alta  = min(grau_alta,  triangular(x, 50, 100, 100))

        mu_saida.append(max(baixa, media, alta))

    return x_saida, mu_saida, grau_baixa, grau_media, grau_alta


def defuzzificar(regras: dict) -> float:
    """
    Realiza a defuzzificação pelo método do centroide.
    """

    x_saida, mu_saida, _, _, _ = agregar_saida(regras)

    numerador = sum(x * mu for x, mu in zip(x_saida, mu_saida))
    denominador = sum(mu_saida)

    if denominador == 0:
        return 0.0

    return numerador / denominador