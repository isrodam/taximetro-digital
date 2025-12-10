import time
import logging # <-- [ISSUE #17] Importamos el módulo de logging

# ----------------------------------------------------
# [ISSUE #17] CONFIGURACIÓN DEL LOGGING
# ----------------------------------------------------
logging.basicConfig(
    level=logging.INFO, # Nivel: Registra INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato: Fecha - Nivel - Mensaje
    handlers=[
        # Guarda el historial en un archivo 'taximetro.log'
        logging.FileHandler("taximetro.log"), 
        # Muestra la salida en la consola
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('TaximetroDigital')

# --- FUNCIONES DE CÁLCULO ---

def calculate_fare(seconds_stopped, seconds_moving):
    """
    Calcula la tarifa total en euros.
    """
    # Tarifas: 0.02 €/s detenido, 0.05 €/s movimiento
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    return fare

# --- FUNCIÓN DE FEEDBACK PARA VISUALIZACIÓN ---

def display_fare_status(current_stopped, current_moving, current_state):
    """ 
    [ISSUE #15] Muestra el estado actual y la tarifa acumulada para el usuario.
    """
    current_fare = calculate_fare(current_stopped, current_moving)
    # [ISSUE #15] Todo el bloque print() es feedback de interfaz de usuario
    print("=" * 45)
    print(f"ESTADO ACTUAL: {current_state.upper()} ⏱️")
    print(f"TIEMPO TOTAL MOVIMIENTO: {current_moving:.1f}s | TIEMPO TOTAL DETENIDO: {current_stopped:.1f}s")
    print(f"💰 TARIFA ACUMULADA: €{current_fare:.2f}")
    print("=" * 45)

# --- FUNCIÓN PRINCIPAL ---

def taximeter():
    # [ISSUE #17] Usamos logger.info en lugar de print para registrar el inicio del programa
    logger.info("APLICACIÓN INICIADA: Welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_active = False
    stopped_time = 0
    moving_time = 0
    state = None  # 'stopped' o 'moving'
    state_start_time = 0

    while True:
        # [ISSUE #15] Llamada a la función de feedback dentro del bucle principal
        if trip_active and state is not None:
            display_fare_status(stopped_time, moving_time, state)

        command = input("> ").strip().lower()

        if command == "start":
            if trip_active:
                # [ISSUE #17] Usamos logger.warning para registrar errores de uso
                logger.warning("Intento de iniciar viaje cuando ya estaba activo.")
                print("Error: A trip is already in progress.")
                continue

            trip_active = True
            stopped_time = 0
            moving_time = 0
            state = 'stopped'
            state_start_time = time.time()
            # [ISSUE #17] Usamos logger.info para registrar el evento clave
            logger.info("EVENTO: Carrera iniciada. Estado inicial: 'stopped'.")
            print("Trip started. Initial state: 'stopped'.") 

        elif command in ("stop", "move"):
            if not trip_active:
                # [ISSUE #17] Usamos logger.warning
                logger.warning("Error: No se puede cambiar de estado sin un viaje activo.")
                print("Error: No active trip. Please start first.")
                continue
            
            # Guardamos el estado anterior para el log
            old_state = state
            
            # 1. Calcular el tiempo transcurrido del estado ANTERIOR
            duration = time.time() - state_start_time

            # 2. Acumular el tiempo al contador correcto
            if state == 'stopped':
                stopped_time += duration
            elif state == 'moving':
                moving_time += duration

            # 3. Cambiar al NUEVO estado
            state = 'stopped' if command == "stop" else 'moving'
            state_start_time = time.time()
            
            # [ISSUE #17] Usamos logger.info para registrar el cambio de estado (clave para trazabilidad)
            logger.info(f"CAMBIO DE ESTADO: De '{old_state}' a '{state}'. Tiempo acumulado en '{old_state}': {duration:.1f}s")
            print(f"State changed to '{state}'.")

        elif command == "finish":
            if not trip_active:
                # [ISSUE #17] Usamos logger.warning
                logger.warning("Error: Intento de finalizar viaje cuando no hay uno activo.")
                print("Error: No active trip to finish.")
                continue

            # Acumular el tiempo del último estado antes de finalizar
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration
            
            final_fare = calculate_fare(stopped_time, moving_time)

            # [ISSUE #15] Muestra el resumen del viaje final al usuario
            display_fare_status(stopped_time, moving_time, "FINALIZADO")
            
            # [ISSUE #17] Usamos logger.info para registrar la finalización y el resultado
            logger.info(f"VIAJE FINALIZADO. Tiempo total (Mov: {moving_time:.1f}s | Det: {stopped_time:.1f}s). Tarifa final: €{final_fare:.2f}")

            # Reset las variables
            trip_active = False
            state = None

        elif command == "exit":
            # [ISSUE #17] Usamos logger.info para registrar el cierre
            logger.info("APLICACIÓN FINALIZADA. El usuario ha salido.")
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")

if __name__ == "__main__":
    taximeter()