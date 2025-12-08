import time

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
    """ Muestra el estado actual y la tarifa acumulada. """
    current_fare = calculate_fare(current_stopped, current_moving)
    print("=" * 45)
    print(f"ESTADO ACTUAL: {current_state.upper()} ⏱️")
    print(f"TIEMPO TOTAL MOVIMIENTO: {current_moving:.1f}s | TIEMPO TOTAL DETENIDO: {current_stopped:.1f}s")
    print(f"💰 TARIFA ACUMULADA: €{current_fare:.2f}")
    print("=" * 45)

# --- FUNCIÓN PRINCIPAL ---

def taximeter():
    print("Welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_active = False
    stopped_time = 0
    moving_time = 0
    state = None  # 'stopped' o 'moving'
    state_start_time = 0

    while True:
        # **AÑADIDO:** Muestra el estado inmediatamente si hay un viaje activo,
        # pero solo después de que se ha procesado un comando.
        if trip_active and state is not None:
             # Mostramos el estado actual sin modificar los contadores
             display_fare_status(stopped_time, moving_time, state)

        command = input("> ").strip().lower()

        if command == "start":
            if trip_active:
                print("Error: A trip is already in progress.")
                continue

            trip_active = True
            stopped_time = 0
            moving_time = 0
            state = 'stopped'
            state_start_time = time.time()
            print("Trip started. Initial state: 'stopped'.")

        elif command in ("stop", "move"):
            if not trip_active:
                print("Error: No active trip. Please start first.")
                continue

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
            print(f"State changed to '{state}'.")

        elif command == "finish":
            if not trip_active:
                print("Error: No active trip to finish.")
                continue

            # Acumular el tiempo del último estado antes de finalizar
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            # Muestra el resumen del viaje usando la función de visualización
            display_fare_status(stopped_time, moving_time, "FINALIZADO")

            # Reset las variables
            trip_active = False
            state = None

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")

if __name__ == "__main__":
    taximeter()