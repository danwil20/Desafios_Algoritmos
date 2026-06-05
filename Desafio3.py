import sys

def contar_formas_cambio(monto_objetivo, denominaciones):
    num_monedas = len(denominaciones)
    tabla = [[0] * (monto_objetivo + 1) for _ in range(num_monedas + 1)]
    for i in range(num_monedas + 1):
        tabla[i][0] = 1
    for i in range(1, num_monedas + 1):
        moneda_actual = denominaciones[i - 1]
        for j in range(1, monto_objetivo + 1):
            formas_arriba = tabla[i - 1][j]
            formas_atras = 0 if moneda_actual > j else tabla[i][j - moneda_actual]
            tabla[i][j] = formas_arriba + formas_atras
    return tabla[num_monedas][monto_objetivo]

MONEDAS_SISTEMA = [1, 5, 10, 25, 50]

nombre_archivo = sys.argv[1]

with open(nombre_archivo, "r") as archivo:
    for texto in archivo:
        texto = texto.strip()
        if not texto:
            continue  
            
        monto = int(texto)
        
        resultado = contar_formas_cambio(monto, MONEDAS_SISTEMA)
        
        print(resultado)