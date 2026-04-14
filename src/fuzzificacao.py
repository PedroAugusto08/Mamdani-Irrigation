from funcoes_pertinencia import triangular

def fuzzificar(umidade: float, temperatura: float, chuva: float):
    
    # Umidade
    u_baixa = triangular(umidade, 0, 0, 50)
    u_media = triangular(umidade, 25, 50, 75)
    u_alta = triangular(umidade, 50, 100, 100)
    
    # Temperatura
    t_fria = triangular(temperatura, 0, 0, 25)
    t_media = triangular(temperatura, 20, 25, 30)
    t_quente = triangular(temperatura, 25, 50, 50)
    
    # Chuva
    c_baixa = triangular(chuva, 0, 0, 50)
    c_media = triangular(chuva, 25, 50, 75)
    c_alta = triangular(chuva, 50, 100, 100)
    
    return {
        "u_baixa": u_baixa,
        "u_media": u_media,
        "u_alta": u_alta,
        "t_fria": t_fria,
        "t_media": t_media,
        "t_quente": t_quente,
        "c_baixa": c_baixa,
        "c_media": c_media,
        "c_alta": c_alta
    }