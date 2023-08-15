def entrada_vacia_numeros(mensaje):
    while True:
        try:
            etd = int(input(mensaje))
            if etd == 0 :
                print('No puede dejar vacío este campo, ingrese algo')
            else:
                return etd
        except ValueError:
            print('Entrada inválida, Ingrese un número válido.')

def entrada_vacia_flot(mensaje):
    while True:
        try:
            etdf = float(input(mensaje))
            if etdf == 0 :
                print('No puede dejar vacío este campo, ingrese algo')
            else:
                return etdf
        except ValueError:
            print('Entrada inválida, Ingrese un número válido.')

def entrada_vacia_texto(msj):
    while True:
        etdv = input(msj)
        if len(etdv) == 0 :
            print('No puede dejar vacío este campo, ingrese algo')
            
        elif not etdv.isalpha():
            print('El campo debe contener solo letras, ingrese nuevamente')  
        else:
            return etdv

nombre = entrada_vacia_texto('Ingrese su nombre: ')
apellido_paterno = entrada_vacia_texto('Ingrese su apellido paterno: ')
apellido_materno = entrada_vacia_texto('Ingrese su apellido materno: ')
edad = entrada_vacia_numeros('Ingrese su edad: ')
estatura = entrada_vacia_flot('Ingrese su estatura con decimales : ')
peso = entrada_vacia_flot('Ingrese su peso con decimales: ')

imc = peso / estatura **2

print(f"Tu nombre es : {nombre} {apellido_paterno} {apellido_materno}, Edad: {edad} años , Tu estatura es : {estatura} mts y pesas : {peso} kg ")
print(f"Tu índice de masa corporal es : {imc}")
