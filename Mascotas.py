def main():
    mascotas = {}
    while True:
        print("*** MENÚ PRINCIPAL ***")
        print(" 1.- Registrar mascota. ")
        print(" 2.- Listar todas las mascotas. ")
        print(" 3.- Buscar por tipo de animal. ")
        print(" 4.- Salir. ")

        opcion = input("Elija una opción: ")

        match opcion:
            case '1':
                registrar_mascota(mascotas)
            case '2':
                listar_mascotas(mascotas)
            case '3':
                tipo_animal(mascotas)
            case '4':
                print("Finalizando programa...")
                break
            case _:
                print("Ingrese una opción válida.")


def registrar_mascota(mascotas):
    nombre = input("Ingrese el nombre de la mascota: ").lower()
    if nombre in mascotas:
        print("Error: Nombre repetido.")
        return  
    
    tipo = input("Ingrese el tipo de animal (Perro/Gato/Otro): ").lower()
    if tipo not in ('perro', 'gato', 'otro'):
        print("Error: Respuesta inválida. Solo se puede 'Perro', 'Gato' o 'Otro'")
        return  

    try:
        edad = int(input("Ingrese la edad de su mascota: "))
        if edad < 1:
            print("Error: Debe ingresar una edad válida.")
            return  
    except ValueError:
        print("Debe ingresar un número.")
        return  

    
    mascotas[nombre] = {"Tipo": tipo, "Edad": edad}
    print("¡Mascota registrada con éxito!")


def listar_mascotas(mascotas):
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
    else:
        print("Lista de mascotas:")
        for nombre, datos in mascotas.items():
            print(f"{nombre} : Tipo: {datos['Tipo']}, Edad: {datos['Edad']}")
            #print(f"Nombre: {mascotas[nombre]['Nombre']}, Tipo: {mascotas[nombre]['Tipo']}, Edad: {mascotas[nombre]['Edad']}")


def tipo_animal(mascotas):
    tipoA = input("Ingrese tipo de animal a buscar (Perro/Gato/Otro): ").lower()
    if tipoA not in ('perro' 'gato' 'otro'):
        print("Error: Debe ingresar un tipo válido.")
        return
    else:
        encontrados = 0
        for nombre, datos in mascotas.items():
        #mascotas[nombre]["Tipo"].lower() == tipoA:
            if datos['Tipo'].lower() == tipoA:
                print(f"{nombre} : Edad: {datos['Edad']}")
                #print(f"Nombre: {mascotas[nombre]['Nombre']}, Edad: {mascotas[nombre]['Edad']}")
                encontrados += 1

    if encontrados == 0:
        print("No se encontraron mascotas de ese tipo.")


main()