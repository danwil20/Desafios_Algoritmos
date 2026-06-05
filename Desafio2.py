import sys

nombre_archivo = sys.argv[1]

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    for texto in archivo:
        if not texto.strip():
            continue 
            
        parte_vinos, letras_recordadas = texto.split("|")
        letras_recordadas = letras_recordadas.strip()
        
        vino = parte_vinos.strip()
        
        cumple_condicion = True      
        for letra in letras_recordadas:
            if vino.count(letra) < letras_recordadas.count(letra):
                cumple_condicion = False
                break
                
        # Imprimimos el resultado exacto
        if cumple_condicion:
            print(vino)
        else:
            print("False")