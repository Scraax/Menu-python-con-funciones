def main():
    compradores = {}
    while True:
        print("\n**** MENU PRINCIPAL ****")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")
    
        opcion = input("Ingrese opción: ")

        match opcion:
            case '1':
                comprar_entrada(compradores)
            case '2':
                consultar_comprador(compradores)
            case '3':
                cancelar_compra(compradores)
            case '4':
                print("Programa terminado...")
                break
            case _:
                print("Debe ingresar una opción válida!!")


def verificacion_codigo(codigo):
    tiene_mayuscula = False
    tiene_numero = False
    tiene_espacio = False

    if len(codigo) < 6:
        return False
    

    for c in codigo:
        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_numero = True
        if c.isspace():
            tiene_espacio = True
    
    if tiene_mayuscula and tiene_numero and not tiene_espacio:
        return True
    else:
        return False

def comprar_entrada(compradores):
    nombre = input("Ingrese nombre de comprador: ").lower()
    if nombre in compradores:
        print("Error: No se puede repetir nombre de comprador.")

    tipoE = input("Ingrese tipo de entrada (G/V): ").upper().strip()
    if tipoE not in ('G' 'V'):
        print("Error: Solo esta disponible (G O V)")
        return

    while True:
        codigo = input("Ingrese código de confirmación: ")
        if verificacion_codigo(codigo):
            print("Código validado. ¡Entrada registrada con éxito!")
            compradores[nombre] = {"tipo": tipoE, "codigo": codigo}
            break
        else:
            print("Codigo no válido. Intente otra vez.")

        
def consultar_comprador(compradores):
    nombre = input("Ingrese nombre de comprador a buscar: ").lower()
    if nombre in compradores:
        datos = compradores[nombre]
        print(f"Tipo de entrada: {datos['tipo']}, Código: {datos['codigo']}")
    else:
        print("El comprador no se encuentra.")
        return

def cancelar_compra(compradores):
    nombre = input("Ingrese nombre de comprador a cancelar: ").lower()
    if nombre in compradores:
        print("¡Compra cancelada!")
        del compradores[nombre]
    else:
        print("No se pudo cancelar la compra.")

main()