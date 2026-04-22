from fuzzificacao import fuzzificar
from regras import aplicar_regras
from defuzzificacao import defuzzificar


def executar_sistema(umidade: float, temperatura: float, chuva: float) -> float:
    """
    Executa o sistema fuzzy completo.
    """

    print("\n=== ENTRADAS ===")
    print(f"Umidade: {umidade}")
    print(f"Temperatura: {temperatura}")
    print(f"Chuva: {chuva}")

    # Fuzzificação
    f = fuzzificar(umidade, temperatura, chuva)

    print("\n=== FUZZIFICAÇÃO ===")
    for k, v in f.items():
        print(f"{k}: {v:.3f}")

    # Regras
    r = aplicar_regras(f)

    print("\n=== ATIVAÇÃO DAS REGRAS ===")
    for k, v in r.items():
        print(f"{k}: {[round(x,3) for x in v]}")

    # Defuzzificação
    resultado = defuzzificar(r)

    print("\n=== RESULTADO FINAL ===")
    print(f"Irrigação: {resultado:.2f}%")

    return resultado


def main():
    # Teste exemplo
    executar_sistema(umidade=30, temperatura=32, chuva=20)


if __name__ == "__main__":
    main()