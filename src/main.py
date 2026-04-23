from fuzzificacao import fuzzificar
from regras import aplicar_regras
from defuzzificacao import defuzzificar
from graficos import gerar_graficos_base, plotar_saida_agregada


def executar(umidade: float, temperatura: float, chuva: float, gerar_grafico=False, nome_grafico="saida_agregada.png") -> float:
    # Executa o sistema fuzzy completo.
    print("\n=== ENTRADAS ===")
    print(f"Umidade: {umidade}%")
    print(f"Temperatura: {temperatura}°C")
    print(f"Chuva: {chuva}%")

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


def ler_float(mensagem, minimo, maximo):
    # Lê um valor float do usuário com validação.
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"Valor deve estar entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def main():
    print("Sistema de Irrigação Fuzzy (Mamdani)\n")

    gerar_graficos_base()

    umidade = ler_float("Digite a umidade do solo (0 a 100)%: ", 0, 100)
    temperatura = ler_float("Digite a temperatura (0 a 40)°C: ", 0, 40)
    chuva = ler_float("Digite a probabilidade de chuva (0 a 100)%: ", 0, 100)

    gerar = input("Deseja gerar gráfico da saída? (s/n): ").lower() == 's'

    executar(
        umidade=umidade,
        temperatura=temperatura,
        chuva=chuva,
        gerar_grafico=gerar,
        nome_grafico="saida_agregada_manual.png"
    )


if __name__ == "__main__":
    main()