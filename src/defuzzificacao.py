import numpy as np
from funcoes_pertinencia import triangular

def defuzzificar(regras: dict) -> float:
    """
    Realiza agregação e defuzzificação (método do centroide).
    """

    # Agregação
    grau_baixa = max(regras["baixa"])
    grau_media = max(regras["media"])
    grau_alta  = max(regras["alta"])

    # Universo de saída
    x_saida = np.linspace(0, 100, 1000)
    mu_saida = []

    for x in x_saida:
        baixa = min(grau_baixa, triangular(x, 0, 0, 50))
        media = min(grau_media, triangular(x, 25, 50, 75))
        alta  = min(grau_alta,  triangular(x, 50, 100, 100))

        mu_saida.append(max(baixa, media, alta))

    # Centroide
    numerador = sum(x * mu for x, mu in zip(x_saida, mu_saida))
    denominador = sum(mu_saida)

    if denominador == 0:
        return 0.0

    return numerador / denominador