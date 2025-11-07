numero = int(input("Ingrese un número decimal entre 0 y 99: "))

if numero < 0 or numero > 99:
    print("Número fuera de rango.")
else:
    pesos = [128, 64, 32, 16, 8, 4, 2, 1]
    resultado = ""
    n = numero

    print(f"\nProceso de conversión para {numero}:")
    for p in pesos:
        if n >= p:
            resultado += "1"
            n -= p
            print(f"{n+p} >= {p} → 1  → Nuevo valor: {n}")
        else:
            resultado += "0"
            print(f"{n} < {p} → 0  → Valor se mantiene: {n}")

    print(f"\nNúmero decimal: {numero}")
    print(f"Binario (8 bits): {resultado}")