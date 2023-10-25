from Analizadordatos import Analizador_datos

archivo = 'eventos.txt'
proceso = Analizador_datos(archivo)
procesar = Analizador_datos.procesar_eventos

print("resultado", procesar)
