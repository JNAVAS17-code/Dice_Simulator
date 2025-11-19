import random

def diceroll(sides):
    """Lanza un dado con el número de caras especificado."""
    return random.randint(1, sides)

def menu():
    """Muestra el menú de opciones al usuario."""
    # Dictionary with preset dice options (key: user input, value: (name, sides))
    dados ={'1':('d6',6),'2':('d20',20), '3':('d4',4),'4':('salir',0)} 
    # Display menu options
    print("Seleccione el tipo de dado a lanzar:")
    print("1. Dado de 6 caras (d6)")
    print("2. Dado de 20 caras (d20)")
    print("3. Dado de 4 caras (d4)")
    print("C. Dado personalizado")
    # Get user input
    print("4. Salir")
    op=input("Ingrese su opción (1-4 o c): ")
    # Check if input matches a preset dice
    if  op in dados:
        return dados[op]
    # Handle custom dice option
    elif op in ('c', 'personalizado', 'custom'):
        while True:
            nombre = 'dado personalizado'
            caras_str = input("Número de caras (entero > 1): ").strip()
            # Try to convert user input to integer
            try:
                sides = int(caras_str)
                # Validate that sides is greater than 1
                if sides > 1:
                    break
                print("Introduce un entero mayor que 1.")
            except ValueError:
                # Handle non-integer input
                print("Entrada inválida. Introduce un número entero.")
        return (nombre,sides)
    # Handle invalid input
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        return menu() # Recursively call menu until valid input is provided
        
    

def main():
    """Función principal para ejecutar el programa de lanzamiento de dados."""
    while True:
        # Get dice type and sides from menu
        nombre,sides = menu()
        # Check if user selected exit option
        if nombre == 'salir':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        # Get number of dice to roll from user
        cantidad = int(input("¿Cuántos desea lanzar? "))
         # Roll the dice 'cantidad' times and print each result
        for _ in range(cantidad):
            resultado = diceroll(sides)
            print(f"Resultado del lanzamiento: {resultado}")
main()


