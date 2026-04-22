def aplicar_regras(f: dict) -> dict:
    
    # Regras
    r1 = min(f['u_baixa'], f['t_quente'])   # alta
    r2 = min(f['u_baixa'], f['t_media'])    # média
    r3 = min(f['u_baixa'], f['t_fria'])     # média
    
    r4 = min(f['u_media'], f['t_quente'])   # média
    r5 = min(f["u_media"], f["t_media"])    # media
    r6 = min(f['u_media'], f['t_fria'])     # baixa
    
    r7 = f['u_alta']                        # baixa
    
    r8 = f['c_alta']                        # baixa
    
    r9 = min(f['c_media'], f['u_baixa'])    # média
    r10 = min(f['c_baixa'], f['t_quente'])  # alta
    r11 = min(f["u_media"], f["c_media"])   # media
    
    return {
        "baixa": [r6, r7, r8],
        "media": [r2, r3, r4, r5, r9, r11],
        "alta": [r1, r10]
    }
    
    