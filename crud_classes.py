import json
from dataclasses import dataclass, asdict

### variables globales

opcion=None





### clases 
@dataclass
class persona():
    nombre: str
    edad: int
    correo : str



### funciones

def confirmacion():
    input('enter para continuar')


def guardar_historial(lista):
    with open('personas.json','w', encoding='utf-8') as archivo:
        lista_adicts=[asdict(p) for p in lista]
        json.dump(lista_adicts, archivo, indent=4)


def cargar_personas():
    try:
        with open('personas.json', 'r', encoding='utf-8') as archivo:
            lista_dicts = json.load(archivo)
            return [persona(**d) for d in lista_dicts]
    except FileNotFoundError:
        return []


### crud
def crear_persona():
    while True:
        try:
            nombre=str(input('ingrese su nombre: '))
            edad=int(input('ingrese su edad, asegure que sea un numero: '))
            correo=str(input('ingrese su correo personal: '))
            p = persona(nombre,edad,correo)
            personas.append(p)
            break
        except ValueError:
            print('tipo de dato invalido, asegurese de que sea correcto')
            continue


def mostrar_personas(lista):
    for i, p in enumerate(lista, start=1):
        print(f'{i}. {p.nombre} {p.edad} {p.correo}')


def modificar_personas(lista):
    mostrar_personas(lista)
    while True:
        print('selecione el usuario a modificar: ')
        try:
            opcion=int(input('\n selecione su opcion, asegurese que sea un numero: '))
            indice=opcion-1
            if indice <0 or indice>= len(lista):
                print('usuario inexistente, asegurese de tener su usuario correcto.')
                confirmacion()
                continue
            persona_sel=lista[indice]
            persona_sel.nombre= input('nuevo nombre:')
            persona_sel.edad= int(input('ingrese su nueva edad: '))
            persona_sel.correo=input('ingrese su nuevo correo: ')
            break
        except ValueError:
            print('tipo de dato incorrecto, use numeros')
            confirmacion()
            continue
    


def borrar_personas(lista):
    while True:
        mostrar_personas(lista)
        try:
            opcion=int(input('ingrese el numero de la persona a modificar: '))
            indice=opcion-1
            if indice<0 or indice>=len(lista):
                print('numero de lista invalido, revise la lista.')
                confirmacion()
                continue
        except ValueError:
            print('tipo de dato incorrecto por favor ingrese un numero: ')
            confirmacion()
            continue
        lista.pop(indice)
        break






###almacenamiento 

personas=cargar_personas()



###menu principal
while True:
    print( '''\n esto es una prueba de crud:
0. salir
1.crear 
2.leer 
3.actualizar
4.borrar. \n''')
    try:
        opcion=int(input('selecione su opcion: '))
    except ValueError:
        print('tipo de dato erroneo, asegurese que sea un numero')
        confirmacion()
        continue

    if opcion==0: 
        print('salida con exito, tenga un buen dia :)')
        guardar_historial(personas)
        break

    elif opcion==1:
        crear_persona()
    elif opcion==2:
        mostrar_personas(personas)
    elif opcion==3:
        modificar_personas(personas)
    elif opcion==4:
        borrar_personas(personas)
    else:
        print('opcion invalida, por favor ingrese una valida')
    confirmacion()
    continue

