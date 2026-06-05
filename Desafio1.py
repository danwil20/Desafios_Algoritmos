import sys

nombre_archivo = sys.argv[1]


with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    for texto in archivo:
        if not texto.strip():
            continue
            
        parte_texto, parte_numero = texto.split(";")
        lista_palabra = parte_texto.split()
        lista_indices = [int(k) for k in parte_numero.split()]
        palabras_en_orden = []
        parejas_ordenadas = sorted(zip(lista_indices, lista_palabra))
        for pareja in parejas_ordenadas:
            palabras_en_orden.append(pareja[1])
        
        oracion_final = " ".join(palabras_en_orden)
        print(oracion_final)