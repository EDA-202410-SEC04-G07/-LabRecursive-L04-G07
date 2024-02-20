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

