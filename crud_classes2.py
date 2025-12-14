###imports
from dataclasses import dataclass, asdict
import datetime
import json, os

###clases

@dataclass
class cliente():
    nombre: str
    edad: int
    documento: int
    hora_registro: datetime.datetime

##Funciones


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def confirmacion():
    input('ingrese enter para continuar')

def guardar_historial(lista):
    with open('personas.json','w', encoding='utf-8') as archivo:
        lista_adicts = []
        for c in lista:
            d = asdict(c)
            d["hora_registro"] = c.hora_registro.isoformat()
            lista_adicts.append(d)
        json.dump(lista_adicts, archivo, indent=4)



def cargar_personas():
    try:
        with open('personas.json', 'r', encoding='utf-8') as archivo:
            lista_dicts = json.load(archivo)
            return [
                cliente(
                    d["nombre"],
                    d["edad"],
                    d["documento"],
                    datetime.datetime.fromisoformat(d["hora_registro"])
                )
                for d in lista_dicts
            ]
    except FileNotFoundError:
        return []







###crud

def crear_cliente():
    while True:
        try:
            nombre= str(input('\ningrese el nombre del usuario: '))
            edad= int(input('ingrese su edad: '))
            documento= int(input('ingrese su numero de documento: '))
            hora_registro=datetime.datetime.now()
            return cliente(nombre,edad,documento,hora_registro)
        except:
            print('\n tipo de dato invalido, por favor revise sus tipos de datos.')
            confirmacion()
            continue

def actualizar_cliente(lista):
    while True:
        mostrar_cliente(lista)
        try:
            opcion=int(input('selecione la opcion a modificar: '))
            indice=opcion-1
            if indice <0 or indice >= len(lista):
                print('usuario inexistente, por favor ingrese uno valido')
                continue
            persona_sel=lista[indice]
            actualizar_cliente_datos(persona_sel, lista)
            break
        except ValueError:
            print('tipo de dato erroneo, por favor ingrese un numero valido')
            confirmacion()
            continue



def actualizar_cliente_datos(persona_sel, lista):
    while True:
        try:
            opcion=int(input('''selecione el dato que desea modificar:
0. cancelar operacion  
1. modificar nombre 
2. modificar edad
3. modificar documento
'''))
        except ValueError:
            print('tipo de dato erroneo, por favor ingrese un numero')
            confirmacion()
            continue
        if opcion==0:
            print('salir de las modificaciones.')
            guardar_historial(lista)
            break
        elif opcion==1:
            persona_sel.nombre=input('ingrese el nuevo nombre: ')
        elif opcion==2:
            persona_sel.edad=int(input('ingrese la nueva edad: '))
        elif opcion==3:
            persona_sel.documento= int(input('ingrese el nuevo documento: '))
        else:
            print('opcion invalida, revise su eleccion')
            continue






def mostrar_cliente(lista):
    if lista==[]:
        print('No existen clientes, cree nuevos clientes')
        confirmacion()
    else:
        for i,p in enumerate (lista, start=1):
            print(f'{i}. cliente:{p.nombre} \n edad: {p.edad} \n numero de documento: {p.documento}\n fecha de creacion: {p.hora_registro}.')


def eliminar_clientes(lista):
    mostrar_cliente(lista)
    while True:
        try:
            opcion=int(input('ingrese el usuario que desea modificar: '))
            indice=opcion-1
            if indice<0 or indice>= len(lista):
                print('numero de usuario incorrecto, ingrese un usuario valido')
                confirmacion()
                continue
            lista.pop(indice)
            print('usuario eliminado con exito')
            break
        except ValueError:
            print('tipo de dato erroneo, por favor revise el tipo de dato ingresado')
            confirmacion()
            guardar_historial(lista)
            continue



###menu


clientes=cargar_personas()

while True:
    try:
        opcion=int(input('''\n selecione la opcion, con su opcion numerica:
0.salir del sistema.
1.crear usuario
2.actualizar usuario
3.mostrar usuarios
4.eliminar usuarios
:'''))
    except ValueError:
        print('tipo de dato erroneo, por favor revise el uso de letras')
        confirmacion()
        limpiar_pantalla()
        continue

    if opcion==0:
        print('tenga un buen dia :)')
        guardar_historial(clientes)
        break

    elif opcion==1:
        nuevo=crear_cliente()
        clientes.append(nuevo)
        print('usuario creado con exito')
        confirmacion()
        limpiar_pantalla()

    elif opcion==2:
        actualizar_cliente(clientes)
        confirmacion()
        limpiar_pantalla()


    elif opcion==3:
        mostrar_cliente(clientes)
        confirmacion()
        limpiar_pantalla()


    elif opcion==4:
        eliminar_clientes(clientes)
        confirmacion()
        limpiar_pantalla()


    else:
        print('opcion invalida, por favor revise ingresar numeros')
        confirmacion()
        limpiar_pantalla()
        continue


