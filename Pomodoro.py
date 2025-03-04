import time
import winsound    #Es para importar el sonido pero solo para windows

#   Función para realizar la cuentra regresiva
def pomodoro(tiempo_trabajo, tiempo_descanso, num_ciclos):
    for ciclo in range(1, num_ciclos + 1):
        print(f"\n 🟢   Ciclo {ciclo}: Tiempo de trabajo ({tiempo_trabajo} minutos)")
        cuenta_atras(tiempo_trabajo * 60)
        print("\n ⏸️   Descanso corto")
        cuenta_atras(tiempo_descanso * 60)

    print("\n  🎉  ¡Pomodoro completado! ¡Bien hecho Campeón lo hiciste!  🎉👨‍💻")


#   Función para realizar la cuenta regresiva
def cuenta_atras(segundo):
    while segundo:
        min, seg = divmod(segundo, 60)
        print(f"\r ⌛ {min:02d}:{seg:02d}", end="" , flush=True)
        time.sleep(1)
        segundo -= 1
    print("\r⌛  00:00")
    sonido()

#   Función para reproducir un sonido al finalizar el temporizador
def sonido(archivo_sonido="sonido/game-bonus.wav"):
    try:
        winsound.PlaySound(archivo_sonido, winsound.SND_FILENAME)
    except Exception as e:
        print(f" 🚧 Error a reproducir sonido: {e} ")

#   Bloque principal del programa
if __name__ == "__main__":
    print("🍅 Bienvenido al Pomodoro en Consola 🍅")
    tiempo_trabajo = int(input(" ⌛ Ingresa el tempo de trabajo (minutos): "))
    tiempo_descanso = int(input(" ☕ Ingresa el tiempo de descanso (minutos): "))
    num_ciclos = int(input(" 🔁 ¿Cuántos ciclos quieres hacer?: "))

    pomodoro(tiempo_trabajo, tiempo_descanso, num_ciclos)