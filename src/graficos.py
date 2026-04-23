import os
import numpy as np
import matplotlib.pyplot as plt

from funcoes_pertinencia import triangular
from defuzzificacao import agregar_saida


def garantir_pasta_saida():
    os.makedirs("graficos", exist_ok=True)


def plotar_pertinencia_umidade():
    x = np.linspace(0, 100, 1000)

    baixa = [triangular(v, 0, 0, 50) for v in x]
    media = [triangular(v, 25, 50, 75) for v in x]
    alta  = [triangular(v, 50, 100, 100) for v in x]

    plt.figure(figsize=(10, 5))
    plt.plot(x, baixa, label="Baixa")
    plt.plot(x, media, label="Média")
    plt.plot(x, alta, label="Alta")
    plt.title("Funções de Pertinência - Umidade do Solo")
    plt.xlabel("Umidade (%)")
    plt.ylabel("Grau de pertinência")
    plt.ylim(-0.05, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficos/pertinencia_umidade.png")
    plt.close()


def plotar_pertinencia_temperatura():
    x = np.linspace(0, 40, 1000)

    fria   = [triangular(v, 0, 0, 15) for v in x]
    media  = [triangular(v, 10, 25, 35) for v in x]
    quente = [triangular(v, 25, 40, 40) for v in x]

    plt.figure(figsize=(10, 5))
    plt.plot(x, fria, label="Fria")
    plt.plot(x, media, label="Média")
    plt.plot(x, quente, label="Quente")
    plt.title("Funções de Pertinência - Temperatura")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Grau de pertinência")
    plt.ylim(-0.05, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficos/pertinencia_temperatura.png")
    plt.close()


def plotar_pertinencia_chuva():
    x = np.linspace(0, 100, 1000)

    baixa = [triangular(v, 0, 0, 40) for v in x]
    media = [triangular(v, 30, 50, 70) for v in x]
    alta  = [triangular(v, 60, 100, 100) for v in x]

    plt.figure(figsize=(10, 5))
    plt.plot(x, baixa, label="Baixa")
    plt.plot(x, media, label="Média")
    plt.plot(x, alta, label="Alta")
    plt.title("Funções de Pertinência - Probabilidade de Chuva")
    plt.xlabel("Probabilidade de chuva (%)")
    plt.ylabel("Grau de pertinência")
    plt.ylim(-0.05, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficos/pertinencia_chuva.png")
    plt.close()


def plotar_pertinencia_saida():
    x = np.linspace(0, 100, 1000)

    baixa = [triangular(v, 0, 0, 50) for v in x]
    media = [triangular(v, 25, 50, 75) for v in x]
    alta  = [triangular(v, 50, 100, 100) for v in x]

    plt.figure(figsize=(10, 5))
    plt.plot(x, baixa, label="Baixa")
    plt.plot(x, media, label="Média")
    plt.plot(x, alta, label="Alta")
    plt.title("Funções de Pertinência - Saída (Irrigação)")
    plt.xlabel("Irrigação (%)")
    plt.ylabel("Grau de pertinência")
    plt.ylim(-0.05, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficos/pertinencia_saida.png")
    plt.close()


def plotar_saida_agregada(regras: dict, valor_defuzzificado: float, nome_arquivo="saida_agregada.png"):
    x_saida, mu_saida, grau_baixa, grau_media, grau_alta = agregar_saida(regras)

    base_baixa = [triangular(v, 0, 0, 50) for v in x_saida]
    base_media = [triangular(v, 25, 50, 75) for v in x_saida]
    base_alta  = [triangular(v, 50, 100, 100) for v in x_saida]

    corte_baixa = [min(grau_baixa, v) for v in base_baixa]
    corte_media = [min(grau_media, v) for v in base_media]
    corte_alta  = [min(grau_alta, v) for v in base_alta]

    plt.figure(figsize=(10, 5))
    plt.plot(x_saida, corte_baixa, label="Baixa (cortada)")
    plt.plot(x_saida, corte_media, label="Média (cortada)")
    plt.plot(x_saida, corte_alta, label="Alta (cortada)")
    plt.plot(x_saida, mu_saida, linewidth=2, label="Agregada")
    plt.axvline(valor_defuzzificado, linestyle="--", label=f"Centroide = {valor_defuzzificado:.2f}")

    plt.title("Saída Fuzzy Agregada Antes da Defuzzificação")
    plt.xlabel("Irrigação (%)")
    plt.ylabel("Grau de pertinência")
    plt.ylim(-0.05, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"graficos/{nome_arquivo}")
    plt.close()


def gerar_graficos_base():
    garantir_pasta_saida()
    plotar_pertinencia_umidade()
    plotar_pertinencia_temperatura()
    plotar_pertinencia_chuva()
    plotar_pertinencia_saida()