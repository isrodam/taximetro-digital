Proceso mental para crear un programa por ejemplo aplicado a este primer proyecto:

- Paso 1: Entender el problema en la vida real. Hablando con el cliente o imaginando que se requiere.
- Paso 2: Preparar lista de requisitos. Usamos comandos o botones. El programa deberá hacer:
            - Saber que ha iniciado un viaje
            - Registrar que se ha detenido
            - Conocer que se vuelve a mover
            - Cuando termina ver cuanto hay que cobrar
            - Terminar para poder empezar un nuevo viaje
- Paso 3: Preguntarme que información necesito guardar en cada momento. Usamos variables.
            - Hay un viaje en curso SI/NO (Vamos a utilizar variable booleana Verdadero/Falso)
            - Calcular segundos totales parado
            - Calcular segundos totales en movimiento
            - Si en este momento esta parado o en movimiento
            - Saber a que hora ha cambiado el estado actual
- Paso 4: Dibujar el flujo del programa:
            
            ```
            Inicio → mostrar bienvenida
                    → esperar comando

            si escribe "start" → pongo viaje_activo = True
                    → estado = parado
                    → guardo la hora actual

            si escribe "stop" o "move" → 
                    1. calculo cuántos segundos pasaron desde la última vez
                    2. sumo esos segundos al contador correcto (parado o movimiento)
                    3. cambio el estado
                    4. guardo la hora nueva

            si escribe "finish" → 
                    1. hago lo mismo que arriba (sumar el último tramo)
                    2. calculo dinero
                    3. muestro resumen
                    4. reseteo todo

            si escribe "exit" → salgo
            ```
- Paso 5: Empezar a escribir el esqueleto vacio, solo la estructura, con while, if/elif:
            ```python
            import time

            def calcular_dinero(parado, movimiento):
                pass  # luego lo lleno

            def taximetro():
                print("Bienvenida...)

                viaje_activo = False
                tiempo_parado = 0
                tiempo_movimiento = 0
                estado = None
                hora_cambio_estado = 0

                while True:
                    comando = input("> ")

                    if comando == "start":
                        # aquí va la lógica
                        pass

                    elif comando in ("stop", "move"):
                        # aquí va la lógica
                        pass

                    elif comando == "finish":
                        # aquí va la lógica
                        pass

                    elif comando == "exit":
                        break

            if __name__ == "__main__":
                taximetro()
            ```
- Paso 6: Ir resolviendo cada vez un bloque
            1. Que funcione start
            2. Que funcione stop y move. Imprimir mensaje.
            3. Añadir calculo de tiempo entre cambios.
            4. Añadir calculo dinero.
            5. Revisar mensajes y formatos
- Paso 7: Tener claro y revisar si hay dudas. Para que usamos y en que momento:
    1. Como guardar en la memoria <- Variables
    2. Decisiones de usuario y acciones que se realizaran <- if/elif
    3. En que momento hay que medir el tiempo <- Antes y despues de cambiar de estado
    4. ¿Que pasa si el usuario hace algo incorrecto? <- Mensaje de error

Resumen pasos a seguir para hacer el código:

1. Entender el problema
2. Listar acciones de usuario <- Comandos o botones
3. Guardar en memoria lo que haga falta recordar <- Variables
4. Dibujar el flujo en papel
5. Escribir el esqueleto vacion usando while + if/elif
6. Ir llenando los bloques e ir probando a cada paso
7. Aclarar en caso de duda lo especificado en el paso 7