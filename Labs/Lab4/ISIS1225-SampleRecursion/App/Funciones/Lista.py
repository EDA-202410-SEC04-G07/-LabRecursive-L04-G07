def new_list():
    lista = {
        "elements": [],
        "size": 0
    }

    return lista

def add_last(lista, elem):
    lista["elements"].append(elem)
    lista["size"]+= 1
    return lista