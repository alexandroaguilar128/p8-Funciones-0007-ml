# Alexandro Aguilar NC = 0007
print("+-+-+-+-+-+ Ejemplo 1 +-+-+-+-+")

def saludar():
    print("¡Hola, mundo!")

# Llamar a la función
saludar()
# Salida: ¡Hola, mundo!

print("+-+-+-+-+-+ Ejemplo 2 +-+-+-+-+")

def calcular_area(base, altura):  # 1. Definición
    """Calcula el área de un rectángulo a partir de su base y altura."""  # 2. Documentación (opcional)
    # 3. Cuerpo de la función (indentado)
    resultado = base * altura
    return resultado  # 4. Retorno (opcional)

print("+-+-+-+-+-+ Ejemplo 3 +-+-+-+-+")

def formatear_precio(monto, moneda="$"):
    """Formatea un precio agregando el símbolo de moneda"""
    return f"{moneda}{monto}"

print(formatear_precio(100))  # $100
print(formatear_precio(50, "€"))  # €50
print(formatear_precio(25, moneda="£"))  # £25

print("+-+-+-+-+-+ Ejemplo 4 +-+-+-+-+")

def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 7)
print(resultado)  # 28

print("+-+-+-+-+-+ Ejemplo 5 +-+-+-+-+")

def mostrar_alerta(texto):
    print(texto)
    # No hay return

resultado = mostrar_alerta("Bienvenido")
print(resultado)  # None

print("+-+-+-+-+-+ Ejemplo 6 +-+-+-+-+")

def analizar_ventas(ventas):
    """Calcula total, mínimo y máximo de una lista de ventas"""
    total = sum(ventas)
    minimo = min(ventas)
    maximo = max(ventas)
    return total, minimo, maximo  # Devuelve una tupla

# Desempaquetado de valores
total_v, min_v, max_v = analizar_ventas([100, 250, 75, 300, 150])

print(f"Total: {total_v}, Mínimo: {min_v}, Máximo: {max_v}")
# Salida: Total: 875, Mínimo: 75, Máximo: 300

print("Programa realizado por Alexandro Aguilar NC = 0007")
