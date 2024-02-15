"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribuciones
 *
 * Dario Correal
 """

import config as cf
import sys
import gc
# TODO importar la libreria threading (parte 2)
import controller
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x libros por promedio")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("5- Ordenar los libros por ISBN")
    print("6- Desordenar los libros por ISBN")
    # TODO agregar opciones al menu (parte 2)
    print("0- Salir")


def loadData():
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    books, authors, tags, book_tags = controller.loadData(control)
    return books, authors, tags, book_tags


def printAuthorData(author):
    if author:
        print("Autor encontrado: " + author["name"])
        print("Promedio: " + str(author["average_rating"]))
        print("Total de libros: " + str(size(author["books"])))
        for book in iterator(author["books"]):
            print("Titulo:", book["title"], "ISBN:", book["isbn13"])
    else:
        print("No se encontro el autor")


def printBestBooks(books):
    size = size(books)
    if size:
        print(" Estos son los mejores libros: ")
        for book in iterator(books):
            print("Titulo:", book["title"], "ISBN:",
                  book["isbn13"], "Rating:", book["average_rating"])
    else:
        print("No se encontraron libros")


def printSortResults(sort_books, sample=3):
    if is_empty(sort_books):
        print("La lista esta vacia!!!...")
    else:
        size = size(sort_books)
        if size <= sample*2:
            print("Los", size, "libros ordenados son:")
            for book in iterator(sort_books):
                print("Titulo:", book["title"], "ISBN:", book["isbn13"],
                      "Rating:", book["average_rating"])
        else:
            print("Los", sample, "primeros libros ordenados son:")
            i = 1
            while i <= sample:
                book = get_element(sort_books, i)
                print("Titulo:", book["title"], "ISBN:", book["isbn13"],
                      "Rating:", book["average_rating"])
                i += 1

            print("Los", sample, "últimos libros ordenados son:")
            i = size - sample + 1
            while i <= size:
                book = get_element(sort_books, i)
                print("Titulo:", book["title"], "ISBN:", book["isbn13"],
                      "Rating:", book["average_rating"])
                i += 1


def printSearchResults(book):
    if book is not None:
        print("El libro es: ")
        for key in book.keys():
            print("\t'" + key + "': ", book[key])
    else:
        print("El libro no se encuentra en la lista!!!")


# Se crea el controlador asociado a la vista
control = newController()


# configurando el limite de recursion
default_limit = 1000

# variables utoles para el programa
# opciones de true
bool_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")


def menu_cycle():

    """
    Menu principal
    """
    working = True
    # configurando si usa algoritmos recursivos
    rec = True

    # ciclo del menu
    while working:
        printMenu()
        # liberar memoria
        gc.collect()
        inputs = input("Seleccione una opción para continuar\n")
        if int(inputs) == 1:
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg = loadData()
            print("Libros cargados: " + str(bk))
            print("Autores cargados: " + str(at))
            print("Géneros cargados: " + str(tg))
            print("Asociación de Géneros a Libros cargados: " + str(bktg))

        elif int(inputs) == 2:
            number = input("Buscando los TOP ?: ")
            books = controller.getBestBooks(control, int(number))
            printBestBooks(books)

        elif int(inputs) == 3:
            authorname = input("Nombre del autor a buscar: ")
            author = controller.getBooksByAuthor(control, authorname)
            printAuthorData(author)

        elif int(inputs) == 4:
            label = input("Etiqueta a buscar: ")
            book_count = controller.countBooksByTag(control, label)
            print("Se encontraron: ", book_count, " Libros")

        elif int(inputs) == 5:
            result = controller.sortBooks(control)
            delta_time = f"{result[0]:.3f}"
            sorted_list = result[1]
            size = lt.size(sorted_list)
            print("===== Los libros ordenados por ISBN son: =====")
            print("Para", size, "elementos, tiempo:", str(delta_time), "[ms]")
            printSortResults(sorted_list)

        elif int(inputs) == 6:
            result = controller.shuffleBooks(control)
            delta_time = f"{result[0]:.3f}"
            shuffled_list = result[1]
            size = size(shuffled_list)
            print("===== Los libros desordenados por ISBN son: =====")
            print("Para", size, "elementos, tiempo:", str(delta_time), "[ms]")
            printSortResults(shuffled_list)

        elif int(inputs) == 7:
            # TODO modificar opcion 7 del menu (parte 2)
            pass

        elif int(inputs) == 8:
            # TODO modificar opcion 8 del menu (parte 2)
            pass

        elif int(inputs) == 9:
            # TODO modificar opcion 9 del menu (parte 2)
            pass

        elif int(inputs) == 10:
            # TODO modificar opcion 10 del menu (parte 2)
            pass

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            # confirmar salida del programa
            end_str = "¿desea salir del programa? (s/n): "
            opt_usr = input(end_str)
            # diferentes opciones de salida
            if opt_usr in bool_lt_opt:
                working = False
                print("\nGracias por utilizar el programa.")
    sys.exit(0)


# main del ejercicio
if __name__ == "__main__":
    # TODO modificar main para actualizar el límite de recursion de memoria (parte 2)
    menu_cycle()
