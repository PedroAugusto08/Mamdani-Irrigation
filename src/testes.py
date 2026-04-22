from main import executar_sistema
from graficos import gerar_graficos_base


def executar_testes():
    gerar_graficos_base()

    print("\n" + "=" * 50)
    print("TESTE 1 - Solo seco, temperatura alta, pouca chuva")
    print("=" * 50)
    executar_sistema(
        umidade=20,
        temperatura=35,
        chuva=10,
        gerar_grafico=True,
        nome_grafico="saida_agregada_teste1.png"
    )

    print("\n" + "=" * 50)
    print("TESTE 2 - Condições intermediárias")
    print("=" * 50)
    executar_sistema(
        umidade=50,
        temperatura=24,
        chuva=40,
        gerar_grafico=True,
        nome_grafico="saida_agregada_teste2.png"
    )

    print("\n" + "=" * 50)
    print("TESTE 3 - Solo úmido, chuva alta")
    print("=" * 50)
    executar_sistema(
        umidade=85,
        temperatura=22,
        chuva=80,
        gerar_grafico=True,
        nome_grafico="saida_agregada_teste3.png"
    )


if __name__ == "__main__":
    executar_testes()