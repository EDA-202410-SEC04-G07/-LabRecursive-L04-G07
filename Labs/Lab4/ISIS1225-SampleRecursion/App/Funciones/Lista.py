def new_list():
    lista = {
        "elements": [],
        "size": 0,
    }
    
    return lista

def add_last(lista, elem):
    lista["elements"].append(elem)
    lista["size"]+= 1
    return lista
     
def isPresent(lista, elem):
    size = lista['size']
    respuesta = False
    if size > 0:
            
            for keypos in range(1, size+1):
                info = lista['elements'][keypos-1]
                if info == elem:
                    respuesta = True
                    info_respuesta = keypos-1
                    break
            if respuesta == True:
                return info_respuesta
    return 0



def subList(lista, pos, numelem):
    sublista = {
        "elements": [],
        "size": 0,
    }
    elem = pos-1
    cont = 1
    while cont <= numelem:
            sublista['elements'].append(lista['elements'][elem])
            sublista['size'] += 1
            elem += 1
            cont += 1
    return sublista 

def getElement(lista,pos):
    return lista['elements'][pos-1]

def changeInfo(lista, pos, newinfo):
     lista['elements'][pos-1] = newinfo


def sort(lista, sort_crit):
    size = lista["size"]
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = subList(lista, 1, mid)
        rightlist = subList(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sort(leftlist, sort_crit)
        sort(rightlist, sort_crit)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = leftlist["size"]
        rightelements = rightlist["size"]

        while (i <= leftelements) and (j <= rightelements):
            elemi = getElement(leftlist, i)
            elemj = getElement(rightlist, j)
            """compara y ordena los elementos"""
            if sort_crit(elemj, elemi):   # caso estricto elemj < elemi
                changeInfo(lista, k, elemj)
                j += 1
            else:                            # caso elemi <= elemj
                changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            changeInfo(lista, k, getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            changeInfo(lista, k, getElement(rightlist, j))
            j += 1
            k += 1
    return lista

def isEmpty(lista):
    return lista['size'] == 0