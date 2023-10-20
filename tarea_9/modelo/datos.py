from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:

        total_temperatura = 0
        total_humedad = 0
        total_presion = 0
        total_velocidad_viento = 0
        direcciones_viento = []

        try:
            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    if linea.startswith("Temperatura:"):
                        total_temperatura += float(linea.split(":")[1].strip())
                    elif linea.startswith("Humedad:"):
                        total_humedad += float(linea.split(":")[1].strip())
                    elif linea.startswith("Presion:"):
                        total_presion += float(linea.split(":")[1].strip())
                    elif linea.startswith("Viento:"):
                        viento_info = linea.split(":")[1].strip().split(',')
                        total_velocidad_viento += float(viento_info[0])
                        direcciones_viento.append(viento_info[1])

            num_registros = len(direcciones_viento)
            temperatura_promedio = total_temperatura / num_registros
            humedad_promedio = total_humedad / num_registros
            presion_promedio = total_presion / num_registros
            velocidad_viento_promedio = total_velocidad_viento / num_registros

            direccion_predominante = calcular_direccion_predominante(direcciones_viento)

            return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_predominante)
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no fue encontrado.")
            return (0, 0, 0, 0, "")

def calcular_direccion_predominante(direcciones):
    direccion_grados = {
        "N": 0,
        "NNE": 22.5,
        "NE": 45,
        "ENE": 67.5,
        "E": 90,
        "ESE": 112.5,
        "SE": 135,
        "SSE": 157.5,
        "S": 180,
        "SSW": 202.5,
        "SW": 225,
        "WSW": 247.5,
        "W": 270,
        "WNW": 292.5,
        "NW": 315,
        "NNW": 337.5,
    }

    direcciones_en_grados = [direccion_grados[d] for d in direcciones]
    direccion_promedio_grados = sum(direcciones_en_grados) / len(direcciones_en_grados)

    direcciones_posibles = list(direccion_grados.values())
    direccion_predominante_grados = min(direcciones_posibles, key=lambda x: abs(x - direccion_promedio_grados))

    for direccion, grados in direccion_grados.items():
        if grados == direccion_predominante_grados:
            return direccion
