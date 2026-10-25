from clima import obtener_clima

def main() -> None:
    """Ejecuta el programa de consulta del clima."""
    ciudad: str = input("Ingresa el nombre de una ciudad: ").strip()

    try:
        datos = obtener_clima(ciudad)
        clima_actual = datos["current_condition"][0]

        temperatura = clima_actual["temp_C"]
        sensacion = clima_actual["FeelsLikeC"]
        humedad = clima_actual["humidity"]
        descripcion = clima_actual["weatherDesc"][0]["value"]

        print(f"\n--- Clima en {ciudad.title()} ---")
        print(f"Temperatura: {temperatura} °C")
        print(f"Sensación térmica: {sensacion} °C")
        print(f"Humedad: {humedad}%")
        print(f"Descripción: {descripcion}")

    except ValueError:
        print("Error: ingresá un nombre de ciudad válido.")
    except KeyError:
        print("Error: no se pudieron interpretar los datos del clima.")
    except IndexError:
        print("Error: el servicio no devolvió datos completos.")
    except Exception as error:
        print(f"Error al consultar el clima: {error}")


if __name__ == "__main__":
    main()