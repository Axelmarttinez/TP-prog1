nombre = input("Ingrese su nombre: ")
print("Elija una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la Primera Letra en mayúscula")
opcion = input("Ingrese 1, 2 o 3 según su elección: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida. Por favor ingrese 1, 2 o 3.")