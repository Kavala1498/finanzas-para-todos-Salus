def hacer_pregunta(pregunta, opciones):
    print(pregunta)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    while True:
        try:
            respuesta = int(input("Selecciona una opción (1-4): "))
            if 1 <= respuesta <= 4:
                return respuesta
            else:
                print("Por favor, selecciona una opción válida (1-4).")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def calcular_perfil_riesgo(puntaje):
    if 10 <= puntaje <= 15:
        return "Conservador"
    elif 16 <= puntaje <= 25:
        return "Moderado"
    elif 26 <= puntaje <= 35:
        return "Agresivo"
    elif 36 <= puntaje <= 40:
        return "Muy Agresivo"
    else:
        return "Perfil no determinado"

def main():
    preguntas = [
        "¿Cuál es tu edad?",
        "¿Cuál es tu horizonte de inversión?",
        "¿Cuál es tu principal objetivo de inversión?",
        "¿Cómo reaccionarías si tu inversión perdiera valor en el corto plazo?",
        "¿Qué porcentaje de tus ingresos estás dispuesto a invertir?",
        "¿Cuál es tu experiencia previa en inversiones?",
        "¿Cómo describirías tu conocimiento sobre inversiones?",
        "¿Qué nivel de volatilidad estás dispuesto a aceptar en tus inversiones?",
        "¿Cuál es tu situación financiera actual?",
        "¿Qué tipo de rendimiento esperas de tus inversiones?"
    ]

    opciones = [
        ["Menos de 25 años", "25 - 35 años", "36 - 50 años", "Más de 50 años"],
        ["Menos de 1 año", "1 - 3 años", "3 - 5 años", "Más de 5 años"],
        ["Preservar el capital", "Generar ingresos estables", "Crecimiento moderado del capital", "Maximizar el crecimiento del capital"],
        ["Vendería inmediatamente para evitar más pérdidas", "Esperaría un poco para ver si se recupera, pero vendería si la situación no mejora", "Mantendría la inversión, confiando en que se recuperará a largo plazo", "Aprovecharía para invertir más, ya que los precios están bajos"],
        ["Menos del 10%", "10% - 20%", "20% - 30%", "Más del 30%"],
        ["Ninguna experiencia", "Alguna experiencia con productos de bajo riesgo (cuentas de ahorro, CDTs)", "Experiencia moderada con productos de riesgo medio (fondos de inversión, bonos)", "Amplia experiencia con productos de alto riesgo (acciones, derivados)"],
        ["Básico", "Intermedio", "Avanzado", "Experto"],
        ["Muy bajo (prefiero estabilidad)", "Bajo (alguna volatilidad es aceptable)", "Moderado (puedo manejar fluctuaciones significativas)", "Alto (estoy cómodo con alta volatilidad)"],
        ["Tengo deudas significativas y pocos ahorros", "Tengo algunas deudas pero también algunos ahorros", "Tengo pocas deudas y ahorros moderados", "Tengo pocas deudas y ahorros considerables"],
        ["Rendimientos bajos pero seguros", "Rendimientos moderados con algún riesgo", "Rendimientos altos con riesgo moderado", "Rendimientos muy altos con alto riesgo"]
    ]

    puntaje_total = 0

    print("Bienvenido al Cuestionario de Perfil de Riesgo")
    for i in range(len(preguntas)):
        respuesta = hacer_pregunta(preguntas[i], opciones[i])
        puntaje_total += respuesta

    perfil = calcular_perfil_riesgo(puntaje_total)
    print(f"\nTu puntaje total es: {puntaje_total}")
    print(f"Tu perfil de riesgo es: {perfil}")

    if perfil == "Conservador":
        print("Recomendaciones: CDTs, bonos gubernamentales, depósitos a plazo fijo.")
    elif perfil == "Moderado":
        print("Recomendaciones: Fondos de inversión de renta fija, bonos corporativos, letras del tesoro.")
    elif perfil == "Agresivo":
        print("Recomendaciones: Papeles comerciales, obligaciones bancarias, títulos de deuda pública.")
    elif perfil == "Muy Agresivo":
        print("Recomendaciones: Inversiones en renta fija de alto rendimiento, combinadas con otros instrumentos de mayor riesgo.")

if __name__ == "__main__":
    main()