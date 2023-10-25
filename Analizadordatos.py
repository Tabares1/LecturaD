from typing import Dict,Any

class Analizador_datos:
    
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.eventos_servidor = {}
        self.total_eventos = 0

    def procesar_eventos(self) -> Dict[str, Any]:
        with open(self.nombre_archivo, 'r' ,encoding="utf-8") as df:
        
            for linea in df:
                if 'Tipo de evento' in linea:
                    self.total_eventos += 1
                    servidor = linea.find('Servidor: ')
        resultado = {
            "eventos_tipo": self.eventos_servidor,
            "numero_eventos": self.total_eventos
                }
        return resultado