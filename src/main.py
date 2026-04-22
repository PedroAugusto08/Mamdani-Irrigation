from fuzzificacao import fuzzificar
from regras import aplicar_regras
from defuzzificacao import defuzzificar
from graficos import gerar_graficos_base, plotar_saida_agregada


def executar_sistema(umidade: float, temperatura: float, chuva: float, gerar_grafico=False, nome_grafico="saida_agregada.png") -> float:
    """
    Executa o sistema fuzzy completo.
    """

    print("\n=== ENTRADAS ===")
    print(f"Umidade: {umidade}")
    print(f"Temperatura: {temperatura}")
    print(f"Chuva: {chuva}")

    f = fuzzificar(umidade, temperatura, chuva)

    print("\n=== FUZZIFICAÇÃO ===")
    for k, v in f.items():
        print(f"{k}: {v:.3f}")

    r = aplicar_regras(f)

    print("\n=== ATIVAÇÃO DAS REGRAS ===")
    for k, v in r.items():
        print(f"{k}: {[round(x, 3) for x in v]}")

    resultado = defuzzificar(r)

    print("\n=== RESULTADO FINAL ===")
    print(f"Irrigação: {resultado:.2f}%")

    if gerar_grafico:
        plotar_saida_agregada(r, resultado, nome_grafico)

    return resultado


def main():
    gerar_graficos_base()
    executar_sistema(umidade=30, temperatura=32, chuva=20, gerar_grafico=True)


if __name__ == "__main__":
    main()